# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""URL validation and resolution utilities for the GenAI Atlas MCP Server."""

import re
from typing import Optional
from urllib.parse import urlparse

from ..config import config

# Allowed domains for Atlas URLs
_ALLOWED_DOMAINS = frozenset({
    'awslabs.github.io',
})


def validate_atlas_url(url: str) -> Optional[str]:
    """Validate that a URL belongs to the Atlas site.

    Args:
        url: The URL to validate.

    Returns:
        None if valid, or an error message string if invalid.
    """
    try:
        parsed = urlparse(url)
    except Exception:
        return f'Error: Invalid URL format: {url}'

    if not parsed.scheme or not parsed.netloc:
        return f'Error: URL must be a full URL with scheme and domain: {url}'

    if parsed.netloc not in _ALLOWED_DOMAINS:
        # Also allow the configured base_url domain (for local dev overrides)
        base_parsed = urlparse(config.base_url)
        if parsed.netloc != base_parsed.netloc:
            return (
                f'Error: URL must be from the Generative AI Atlas site '
                f'({config.base_url}), got domain: {parsed.netloc}'
            )

    if '/generative-ai-atlas' not in parsed.path and config.base_url not in url:
        return (
            f'Error: URL must point to the Generative AI Atlas '
            f'({config.base_url}): {url}'
        )

    return None


def resolve_atlas_url(url: str) -> str:
    """Resolve an Atlas URL to its deployed HTML path.

    MkDocs converts markdown files to HTML in various patterns:
    - foo/bar.md -> foo/bar/index.html (directory style, MkDocs default)
    - foo/bar.md -> foo/bar.html (file style)
    - index.md -> index.html

    The llms.txt links use .md extensions, so we need to convert.

    Args:
        url: The URL to resolve.

    Returns:
        The resolved URL.
    """
    if url.endswith('.md'):
        if url.endswith('/index.md'):
            url = url[: -len('/index.md')] + '/'
        else:
            url = url[: -len('.md')] + '/'
    return url


def try_html_fallback_url(url: str) -> Optional[str]:
    """Generate a .html fallback URL from a .md URL.

    Args:
        url: The original URL (should end with .md).

    Returns:
        The .html variant, or None if the URL doesn't end with .md.
    """
    if url.endswith('.md'):
        return re.sub(r'\.md$', '.html', url)
    return None
