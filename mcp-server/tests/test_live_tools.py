# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Live integration tests that call each tool against the real Atlas site.

Run with: uv run pytest tests/test_live_tools.py -v -m live
"""

import pytest

from genai_atlas_mcp_server.tools.get_reference_example import get_reference_example
from genai_atlas_mcp_server.tools.list_diagrams import list_diagrams
from genai_atlas_mcp_server.tools.list_topics import list_topics
from genai_atlas_mcp_server.tools.read_sections import read_sections
from genai_atlas_mcp_server.tools.read_topic import read_topic
from genai_atlas_mcp_server.tools.search import search_atlas
from genai_atlas_mcp_server.utils import fetcher
from genai_atlas_mcp_server.utils.url_utils import validate_atlas_url


@pytest.fixture(autouse=True)
async def _reset_http_client():
    """Reset the shared HTTP client between tests to avoid stale event loop issues."""
    yield
    await fetcher.close_client()


# --- URL validation tests (unit, no network) ---


def test_validate_atlas_url_valid():
    """Valid Atlas URLs should pass."""
    assert validate_atlas_url(
        'https://awslabs.github.io/generative-ai-atlas/topics/foo.html'
    ) is None


def test_validate_atlas_url_rejects_evil_domain():
    """URLs with 'generative-ai-atlas' in a different domain must be rejected."""
    result = validate_atlas_url('https://evil.com/generative-ai-atlas/steal')
    assert result is not None
    assert 'Error' in result


def test_validate_atlas_url_rejects_no_scheme():
    """URLs without a scheme should be rejected."""
    result = validate_atlas_url('awslabs.github.io/generative-ai-atlas/foo')
    assert result is not None


# --- Live tool tests (hit the real Atlas site) ---


@pytest.mark.live
@pytest.mark.asyncio
async def test_search_atlas_live():
    """search_atlas returns ranked results for a real query."""
    results = await search_atlas(query='RAG pipeline', max_results=3)
    assert len(results) > 0
    assert 'title' in results[0]
    assert 'url' in results[0]
    assert 'score' in results[0]
    assert results[0]['score'] > 0


@pytest.mark.live
@pytest.mark.asyncio
async def test_search_atlas_max_results_clamped():
    """max_results <= 0 should be clamped to 1."""
    results = await search_atlas(query='RAG', max_results=0)
    assert len(results) <= 1


@pytest.mark.live
@pytest.mark.asyncio
async def test_read_topic_live():
    """read_topic fetches and converts a real page."""
    result = await read_topic(
        url='https://awslabs.github.io/generative-ai-atlas/topics/2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_7_rag/2_1_7_rag.html',
        max_length=500,
    )
    assert 'RAG' in result or 'Retrieval' in result
    assert 'Error' not in result


@pytest.mark.live
@pytest.mark.asyncio
async def test_read_topic_rejects_bad_domain():
    """read_topic should reject URLs from non-Atlas domains."""
    result = await read_topic(url='https://evil.com/generative-ai-atlas/page.html')
    assert 'Error' in result


@pytest.mark.live
@pytest.mark.asyncio
async def test_read_sections_live():
    """read_sections extracts a real section."""
    result = await read_sections(
        url='https://awslabs.github.io/generative-ai-atlas/topics/2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_7_rag/2_1_7_rag.html',
        section_titles=['TL;DR'],
    )
    assert 'TL;DR' in result or 'Retrieval' in result
    assert 'Error' not in result


@pytest.mark.live
@pytest.mark.asyncio
async def test_read_sections_rejects_bad_domain():
    """read_sections should reject URLs from non-Atlas domains."""
    result = await read_sections(
        url='https://evil.com/generative-ai-atlas/page.html',
        section_titles=['TL;DR'],
    )
    assert 'Error' in result


@pytest.mark.live
@pytest.mark.asyncio
async def test_list_topics_live():
    """list_topics returns topics filtered by section."""
    results = await list_topics(section='examples')
    assert len(results) > 0
    assert all(r['section'] == 'Examples & References' for r in results)


@pytest.mark.live
@pytest.mark.asyncio
async def test_get_reference_example_live():
    """get_reference_example returns architecture-filtered results."""
    results = await get_reference_example(use_case='chatbot', max_results=3)
    assert len(results) > 0
    assert 'title' in results[0]


@pytest.mark.live
@pytest.mark.asyncio
async def test_list_diagrams_live():
    """list_diagrams returns diagram entries with image URLs."""
    results = await list_diagrams(topic='RAG', max_results=3)
    assert len(results) > 0
    assert 'image_url' in results[0]
    assert 'title' in results[0]
