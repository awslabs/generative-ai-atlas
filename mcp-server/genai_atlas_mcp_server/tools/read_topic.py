# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Read topic tool for the GenAI Atlas MCP Server."""

from ..utils.fetcher import fetch_url
from ..utils.html_converter import html_to_markdown
from ..utils.url_utils import resolve_atlas_url, try_html_fallback_url, validate_atlas_url


async def read_topic(
    url: str,
    max_length: int = 5000,
    start_index: int = 0,
) -> str:
    """Fetch and read the full content of a specific Atlas topic.

    Retrieves an Atlas documentation page and converts it to clean markdown.
    For long documents, use start_index for pagination.

    ## URL Requirements
    - Must be from the awslabs.github.io/generative-ai-atlas domain
    - Accepts .md URLs (from llms.txt/list_topics) or .html URLs

    ## Handling Long Documents
    If the response indicates truncation, call again with the suggested start_index.
    For very long documents (>30,000 chars), stop reading once you've found the needed info.

    ## Example URLs
    - https://awslabs.github.io/generative-ai-atlas/topics/.../2_1_7_rag/2_1_7_rag.html
    - URLs from search_atlas results or list_topics output

    Args:
        url: URL of the Atlas topic page to read.
        max_length: Maximum characters to return (default: 5000, max: 100000).
        start_index: Character offset for pagination (default: 0).

    Returns:
        Markdown content of the Atlas topic, with pagination info if truncated.
    """
    url_str = str(url)

    # Validate URL domain
    validation_error = validate_atlas_url(url_str)
    if validation_error:
        return validation_error

    max_length = max(1, min(max_length, 100000))
    start_index = max(0, start_index)

    # Resolve .md URLs to deployed HTML paths
    resolved_url = resolve_atlas_url(url_str)

    # Try fetching with the resolved URL
    raw_html = await fetch_url(resolved_url)

    # Fallback: try .html extension directly
    if raw_html is None:
        fallback_url = try_html_fallback_url(url_str)
        if fallback_url:
            raw_html = await fetch_url(fallback_url)

    # Fallback: try appending index.html
    if raw_html is None and not resolved_url.endswith('.html'):
        index_url = resolved_url.rstrip('/') + '/index.html'
        raw_html = await fetch_url(index_url)

    if raw_html is None:
        return f'Error: Failed to fetch {url_str} (tried multiple URL patterns)'

    content = html_to_markdown(raw_html)
    if not content:
        return f'Error: No content extracted from {url_str}'

    original_length = len(content)

    if start_index >= original_length:
        return f'Atlas topic from {url_str}:\n\nNo more content available.'

    end_index = min(start_index + max_length, original_length)
    truncated = content[start_index:end_index]

    result = f'Atlas topic from {url_str}:\n\n{truncated}'

    remaining = original_length - end_index
    if remaining > 0:
        result += (
            f'\n\n---\nContent truncated. {remaining} characters remaining. '
            f'Call read_topic with start_index={end_index} to continue.'
        )

    return result
