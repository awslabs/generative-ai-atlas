# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""List diagrams tool for the GenAI Atlas MCP Server."""

from typing import Any, Dict, List, Optional

from ..config import config
from ..utils.fetcher import fetch_urls_concurrent
from ..utils.html_converter import extract_diagrams
from ..utils.search_index import get_search_index
from ..utils.url_utils import resolve_atlas_url


async def list_diagrams(
    topic: Optional[str] = None,
    max_results: int = 10,
) -> List[Dict[str, Any]]:
    """Find architecture and flow diagrams in the Atlas.

    Searches Atlas topics for embedded diagrams (architecture diagrams, flow
    charts, process illustrations) and returns their titles, image URLs, and
    surrounding context.

    Users can click the image URLs to view the diagrams directly.

    ## Example Queries
    - topic="RAG" — Find RAG pipeline diagrams
    - topic="fine-tuning" — Find fine-tuning process diagrams
    - topic="multi-agent" — Find multi-agent architecture diagrams
    - topic=None — Browse all available diagrams

    Args:
        topic: Optional topic filter to narrow diagram search
               (e.g., "RAG", "agents", "fine-tuning").
        max_results: Maximum diagrams to return (default: 10, max: 30).

    Returns:
        List of diagram entries with title, image URL, context, and source page.
    """
    max_results = max(1, min(max_results, 30))
    index = get_search_index()
    await index.ensure_loaded()

    # Find relevant pages to scan for diagrams
    if topic:
        results = index.search(topic, max_results=10)
        original_urls = [r.url for r in results]
    else:
        # Scan architecture and example pages which are most likely to have diagrams
        docs = index.get_all_docs()
        diagram_sections = ['3_0_architecture', '6_0_example', '2_3_core']
        original_urls = [
            d.url for d in docs
            if any(s in d.url for s in diagram_sections)
        ][:15]

    # Resolve URLs and fetch concurrently
    resolved_urls = [resolve_atlas_url(u) for u in original_urls]
    html_pages = await fetch_urls_concurrent(
        resolved_urls, max_concurrent=config.max_concurrent_fetches
    )

    all_diagrams: List[Dict[str, Any]] = []

    for original_url, resolved_url, html in zip(original_urls, resolved_urls, html_pages):
        if len(all_diagrams) >= max_results:
            break
        if not html:
            continue

        page_diagrams = extract_diagrams(html, resolved_url)
        for diag in page_diagrams:
            if len(all_diagrams) >= max_results:
                break
            all_diagrams.append({
                'title': diag['title'],
                'image_url': diag['image_url'],
                'context': diag['context'],
                'page_url': original_url,
            })

    return all_diagrams
