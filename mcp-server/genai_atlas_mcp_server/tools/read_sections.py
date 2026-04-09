# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Read sections tool for the GenAI Atlas MCP Server."""

from typing import List

from ..utils.fetcher import fetch_url
from ..utils.html_converter import extract_sections
from ..utils.url_utils import resolve_atlas_url, try_html_fallback_url, validate_atlas_url


async def read_sections(
    url: str,
    section_titles: List[str],
) -> str:
    """Extract specific sections from an Atlas topic by heading title.

    Fetches a page and returns only the requested sections, saving tokens
    when you know which section you need (e.g., "TL;DR", "Architecture",
    "Benefits", "When to use").

    Section matching is case-insensitive and handles whitespace differences.

    ## Common Atlas Section Names
    Most Atlas topics follow a consistent structure:
    - "TL;DR" — Executive summary
    - "Suggested Pre-Reading" — Prerequisites
    - "Architecture" — System architecture details
    - "Benefits" — Business and technical benefits
    - "When to use" — Use case guidance
    - "Making it practical" — Implementation tips
    - "Further Reading" — External references

    ## Example Usage
    ```
    read_sections(
        url="https://awslabs.github.io/.../customer_service_assistant.html",
        section_titles=["Architecture", "Benefits"]
    )
    ```

    Args:
        url: URL of the Atlas topic page.
        section_titles: List of section heading titles to extract.

    Returns:
        Markdown content containing only the requested sections.
    """
    url_str = str(url)

    validation_error = validate_atlas_url(url_str)
    if validation_error:
        return validation_error

    if not section_titles:
        return 'Error: section_titles cannot be empty'

    # Resolve .md URLs to deployed HTML paths
    resolved_url = resolve_atlas_url(url_str)
    raw_html = await fetch_url(resolved_url)

    # Fallback: try .html extension
    if raw_html is None:
        fallback_url = try_html_fallback_url(url_str)
        if fallback_url:
            raw_html = await fetch_url(fallback_url)

    if raw_html is None:
        return f'Error: Failed to fetch {url_str}'

    try:
        markdown = extract_sections(raw_html, section_titles)
    except ValueError as e:
        return (
            f'Error: {e}\n\n'
            f'Tip: Use read_topic(url="{url_str}") to get the full document content instead.'
        )

    return f'Sections from {url_str}:\n\n{markdown}'
