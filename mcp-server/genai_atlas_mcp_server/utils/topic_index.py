# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Topic index built from the Atlas llms.txt file.

Parses the llms.txt to build a structured topic hierarchy for browsing.
"""

import asyncio
import re
from typing import Dict, List, Optional

from loguru import logger

from ..config import config
from ..models import TopicEntry
from .fetcher import fetch_url
from .url_utils import resolve_atlas_url

# Section mapping based on URL path prefixes
SECTION_MAP: Dict[str, str] = {
    '1_0_generative_ai_fundamentals': 'GenAI Fundamentals',
    '2_0_technical_foundations': 'Technical Foundations & Patterns',
    '3_0_architecture_and_design': 'Architecture & Design Patterns',
    '4_0_systematic_path': 'Production Framework',
    '5_0_organization_adoption': 'Organization Adoption',
    '6_0_example_application': 'Examples & References',
    '7_0_resource_and_tools': 'Resources & Tools',
    '8_0_isv_focus': 'ISV Focus',
}


def _classify_section(url: str) -> Optional[str]:
    """Classify a topic URL into a section name."""
    for prefix, section in SECTION_MAP.items():
        if prefix in url:
            return section
    return None


class TopicIndex:
    """Index of all Atlas topics from llms.txt."""

    def __init__(self):
        """Initialize an empty topic index."""
        self._topics: List[TopicEntry] = []
        self._loaded = False
        self._lock = asyncio.Lock()

    async def ensure_loaded(self) -> None:
        """Load topics from llms.txt if not already loaded."""
        if self._loaded:
            return
        async with self._lock:
            if self._loaded:
                return
            await self._load()

    async def _load(self) -> None:
        """Internal load logic — must be called under self._lock."""
        logger.info('Loading Atlas topic index from llms.txt...')
        content = await fetch_url(config.llms_txt_url)
        if content is None:
            logger.error('Failed to load llms.txt')
            return

        # Parse markdown links: - [Title](URL)
        pattern = re.compile(r'-\s+\[([^\]]+)\]\(([^)]+)\)')
        for match in pattern.finditer(content):
            title = match.group(1).strip()
            url = match.group(2).strip()

            # Skip generic "Index" entries
            if title == 'Index':
                continue

            # Resolve .md URLs to deployed HTML paths for direct usability
            resolved_url = resolve_atlas_url(url)

            section = _classify_section(url)
            self._topics.append(TopicEntry(title=title, url=resolved_url, section=section))

        self._loaded = True
        logger.info(f'Loaded {len(self._topics)} topics from llms.txt')

    def list_topics(self, section: Optional[str] = None) -> List[TopicEntry]:
        """List all topics, optionally filtered by section.

        Args:
            section: Filter by section name (case-insensitive partial match).

        Returns:
            List of TopicEntry objects.
        """
        if section:
            section_lower = section.lower()
            return [
                t for t in self._topics
                if t.section and section_lower in t.section.lower()
            ]
        return self._topics

    def find_topic(self, path_or_title: str) -> Optional[TopicEntry]:
        """Find a topic by path fragment or title.

        Args:
            path_or_title: A URL path fragment or title to search for.

        Returns:
            The matching TopicEntry, or None.
        """
        query = path_or_title.lower()
        for topic in self._topics:
            if query in topic.url.lower() or query in topic.title.lower():
                return topic
        return None


# Global singleton
_topic_index: Optional[TopicIndex] = None


def get_topic_index() -> TopicIndex:
    """Get the global topic index singleton."""
    global _topic_index
    if _topic_index is None:
        _topic_index = TopicIndex()
    return _topic_index
