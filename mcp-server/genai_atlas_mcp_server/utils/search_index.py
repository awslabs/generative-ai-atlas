# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Search index built from the MkDocs search_index.json.

Loads the pre-built search index from the deployed Atlas site and provides
keyword-based search with TF-IDF-style scoring.
"""

import asyncio
import math
import re
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from loguru import logger

from ..config import config
from ..models import SearchResult
from .fetcher import fetch_json


class SearchDoc:
    """A document in the search index."""

    def __init__(self, location: str, title: str, text: str):
        """Initialize a search document."""
        self.location = location
        self.title = title
        self.text = text
        self.url = f'{config.base_url}/{location}'
        # Pre-compute lowercase searchable text
        self.searchable = f'{title} {title} {text}'.lower()  # title weighted 2x
        self.tokens = _tokenize(self.searchable)
        self.token_counts: Dict[str, int] = defaultdict(int)
        for token in self.tokens:
            self.token_counts[token] += 1


def _tokenize(text: str) -> List[str]:
    """Tokenize text into lowercase words."""
    return re.findall(r'[a-z0-9]+', text.lower())


class AtlasSearchIndex:
    """Search index for the GenAI Atlas content."""

    def __init__(self):
        """Initialize an empty search index."""
        self._docs: List[SearchDoc] = []
        self._doc_freq: Dict[str, int] = defaultdict(int)
        self._loaded = False
        self._lock = asyncio.Lock()

    async def ensure_loaded(self) -> None:
        """Load the search index if not already loaded."""
        if self._loaded:
            return
        async with self._lock:
            if self._loaded:
                return
            await self._load()

    async def _load(self) -> None:
        """Internal load logic — must be called under self._lock."""
        logger.info('Loading Atlas search index...')
        data = await fetch_json(config.search_index_url)
        if data is None:
            logger.error('Failed to load search index')
            return

        docs_data = data.get('docs', [])
        seen_locations: Dict[str, SearchDoc] = {}

        for doc in docs_data:
            location = doc.get('location', '')
            title = doc.get('title', '')
            text = doc.get('text', '')

            if not location or not title or title in ('', 'Home'):
                continue

            # Deduplicate by base page — merge anchor sections into the main page
            base_location = location.split('#')[0]
            if base_location in seen_locations and '#' in location:
                existing = seen_locations[base_location]
                existing.text += f' {text}'
                existing.searchable = (
                    f'{existing.title} {existing.title} {existing.text}'.lower()
                )
                existing.tokens = _tokenize(existing.searchable)
                existing.token_counts = defaultdict(int)
                for token in existing.tokens:
                    existing.token_counts[token] += 1
                continue

            new_doc = SearchDoc(location=base_location, title=title, text=text)
            seen_locations[base_location] = new_doc
            self._docs.append(new_doc)

        # Build document frequency index
        for doc in self._docs:
            unique_tokens = set(doc.tokens)
            for token in unique_tokens:
                self._doc_freq[token] += 1

        self._loaded = True
        logger.info(f'Loaded {len(self._docs)} documents into search index')

    def search(self, query: str, max_results: int = 5) -> List[SearchResult]:
        """Search the index using TF-IDF scoring.

        Args:
            query: The search query.
            max_results: Maximum number of results to return.

        Returns:
            List of SearchResult objects sorted by relevance.
        """
        if not self._loaded or not self._docs:
            return []

        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        num_docs = len(self._docs)
        scored: List[Tuple[float, SearchDoc]] = []

        # Average document length for BM25-style normalization
        avg_doc_len = sum(len(d.tokens) for d in self._docs) / num_docs if num_docs else 1
        k1 = 1.2  # term frequency saturation
        b = 0.75  # length normalization factor

        for doc in self._docs:
            score = 0.0
            doc_len = len(doc.tokens) if doc.tokens else 1
            for token in query_tokens:
                tf = doc.token_counts.get(token, 0)
                if tf == 0:
                    continue
                df = self._doc_freq.get(token, 1)
                idf = math.log((num_docs - df + 0.5) / (df + 0.5) + 1)
                # BM25 term frequency normalization
                tf_norm = (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_len / avg_doc_len))
                score += tf_norm * idf

            # Boost exact title matches
            query_lower = query.lower()
            if query_lower in doc.title.lower():
                score *= 2.0

            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)

        results = []
        for score, doc in scored[:max_results]:
            snippet = _make_snippet(doc.text, query_tokens)
            results.append(
                SearchResult(
                    title=doc.title,
                    url=doc.url,
                    score=round(score, 3),
                    snippet=snippet,
                )
            )
        return results

    def get_all_docs(self) -> List[SearchDoc]:
        """Return all indexed documents."""
        return self._docs


def _make_snippet(text: str, query_tokens: List[str], max_length: int = 300) -> str:
    """Generate a snippet from text, centered around query term matches.

    Args:
        text: The source text.
        query_tokens: Tokens from the search query.
        max_length: Maximum snippet length.

    Returns:
        A text snippet with context around matched terms.
    """
    # Strip HTML tags and entities
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&[a-zA-Z]+;', ' ', clean)  # &amp; &lt; etc.
    clean = re.sub(r'&#\d+;', ' ', clean)  # &#123; etc.
    clean = re.sub(r'\s+', ' ', clean).strip()

    if not clean:
        return ''

    # Find the first occurrence of any query token
    text_lower = clean.lower()
    best_pos = -1
    for token in query_tokens:
        pos = text_lower.find(token)
        if pos >= 0 and (best_pos < 0 or pos < best_pos):
            best_pos = pos

    if best_pos < 0:
        return clean[:max_length] + ('...' if len(clean) > max_length else '')

    # Center the snippet around the match
    start = max(0, best_pos - max_length // 3)
    end = min(len(clean), start + max_length)

    snippet = clean[start:end]
    if start > 0:
        snippet = '...' + snippet
    if end < len(clean):
        snippet = snippet + '...'

    return snippet


# Global singleton
_index: Optional[AtlasSearchIndex] = None


def get_search_index() -> AtlasSearchIndex:
    """Get the global search index singleton."""
    global _index
    if _index is None:
        _index = AtlasSearchIndex()
    return _index
