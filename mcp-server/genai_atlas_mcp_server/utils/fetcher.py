# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""HTTP fetching utilities for the GenAI Atlas MCP Server."""

import asyncio
from typing import List, Optional

import httpx
from loguru import logger

from ..config import config

# Module-level client for connection reuse across calls within the same event loop
_client: Optional[httpx.AsyncClient] = None
_client_lock: Optional[asyncio.Lock] = None


def _get_lock() -> asyncio.Lock:
    """Get or create the asyncio lock for the current event loop."""
    global _client_lock
    if _client_lock is None:
        _client_lock = asyncio.Lock()
    return _client_lock


def _create_client() -> httpx.AsyncClient:
    """Create a new httpx async client."""
    return httpx.AsyncClient(
        headers={'User-Agent': config.user_agent},
        follow_redirects=True,
        timeout=config.timeout,
    )


async def _get_client() -> httpx.AsyncClient:
    """Get or create the shared async HTTP client (async-safe).

    Handles stale clients from closed event loops by recreating them.
    """
    global _client
    if _client is not None and not _client.is_closed:
        return _client
    lock = _get_lock()
    async with lock:
        # Double-check after acquiring lock
        if _client is not None and not _client.is_closed:
            return _client
        _client = _create_client()
        return _client


async def _safe_request(method: str, url: str) -> Optional[httpx.Response]:
    """Make an HTTP request, handling stale client errors.

    Args:
        method: HTTP method ('get').
        url: The URL to fetch.

    Returns:
        The response, or None if the request failed.
    """
    global _client
    client = await _get_client()
    try:
        return await client.get(url)
    except RuntimeError:
        # Client was bound to a closed event loop — recreate it
        logger.debug(f'Recreating HTTP client (stale event loop) for {url}')
        _client = _create_client()
        try:
            return await _client.get(url)
        except httpx.HTTPError as e:
            logger.error(f'HTTP error fetching {url} after client reset: {e}')
            return None
    except httpx.HTTPError as e:
        logger.error(f'HTTP error fetching {url}: {e}')
        return None


async def fetch_url(url: str) -> Optional[str]:
    """Fetch content from a URL.

    Args:
        url: The URL to fetch.

    Returns:
        The response text, or None if the fetch failed.
    """
    response = await _safe_request('get', url)
    if response is None:
        return None
    if response.status_code >= 400:
        logger.error(f'Failed to fetch {url} — status {response.status_code}')
        return None
    return response.text


async def fetch_json(url: str) -> Optional[dict]:
    """Fetch JSON content from a URL.

    Args:
        url: The URL to fetch.

    Returns:
        Parsed JSON as a dict, or None if the fetch failed.
    """
    response = await _safe_request('get', url)
    if response is None:
        return None
    if response.status_code >= 400:
        logger.error(f'Failed to fetch {url} — status {response.status_code}')
        return None
    try:
        return response.json()
    except ValueError as e:
        logger.error(f'Error parsing JSON from {url}: {e}')
        return None


async def fetch_urls_concurrent(urls: List[str], max_concurrent: int = 5) -> List[Optional[str]]:
    """Fetch multiple URLs concurrently with a concurrency limit.

    Args:
        urls: List of URLs to fetch.
        max_concurrent: Maximum concurrent requests.

    Returns:
        List of response texts (None for failed fetches), in same order as input URLs.
    """
    semaphore = asyncio.Semaphore(max_concurrent)

    async def _fetch_one(url: str) -> Optional[str]:
        async with semaphore:
            return await fetch_url(url)

    return await asyncio.gather(*[_fetch_one(url) for url in urls])


async def close_client() -> None:
    """Close the shared HTTP client. Call during server shutdown."""
    global _client
    if _client and not _client.is_closed:
        await _client.aclose()
        _client = None
