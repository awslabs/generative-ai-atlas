# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for the search index module."""

from unittest.mock import AsyncMock, patch

import pytest

from genai_atlas_mcp_server.utils.search_index import AtlasSearchIndex, _make_snippet, _tokenize


def test_tokenize():
    """Test basic tokenization."""
    assert _tokenize('Hello World') == ['hello', 'world']
    assert _tokenize('RAG pipeline 2024') == ['rag', 'pipeline', '2024']
    assert _tokenize('') == []


def test_make_snippet():
    """Test snippet generation."""
    text = 'This is a long text about RAG pipelines and how they work in production.'
    snippet = _make_snippet(text, ['rag'], max_length=50)
    assert 'RAG' in snippet or 'rag' in snippet.lower()
    assert len(snippet) <= 60  # max_length + ellipsis


def test_make_snippet_no_match():
    """Test snippet when no query terms match."""
    text = 'This is about something else entirely.'
    snippet = _make_snippet(text, ['nonexistent'], max_length=50)
    assert len(snippet) > 0


def test_make_snippet_html_stripped():
    """Test that HTML tags are stripped from snippets."""
    text = '<p>This is <strong>bold</strong> text about RAG.</p>'
    snippet = _make_snippet(text, ['rag'], max_length=100)
    assert '<p>' not in snippet
    assert '<strong>' not in snippet


@pytest.mark.asyncio
async def test_search_index_empty():
    """Test search on empty index."""
    index = AtlasSearchIndex()
    results = index.search('test query')
    assert results == []


@pytest.mark.asyncio
async def test_search_index_load_failure():
    """Test graceful handling of load failure."""
    index = AtlasSearchIndex()
    with patch(
        'genai_atlas_mcp_server.utils.search_index.fetch_json',
        new_callable=AsyncMock,
        return_value=None,
    ):
        await index.ensure_loaded()
    results = index.search('test')
    assert results == []


@pytest.mark.asyncio
async def test_search_index_load_and_search():
    """Test loading and searching the index."""
    mock_data = {
        'docs': [
            {
                'location': 'topics/rag.html',
                'title': 'RAG Pipelines',
                'text': 'Retrieval Augmented Generation is a key pattern.',
            },
            {
                'location': 'topics/agents.html',
                'title': 'AI Agents',
                'text': 'Agents are autonomous systems that use tools.',
            },
        ]
    }
    index = AtlasSearchIndex()
    with patch(
        'genai_atlas_mcp_server.utils.search_index.fetch_json',
        new_callable=AsyncMock,
        return_value=mock_data,
    ):
        await index.ensure_loaded()

    results = index.search('RAG')
    assert len(results) > 0
    assert results[0].title == 'RAG Pipelines'


@pytest.mark.asyncio
async def test_search_index_deduplication():
    """Test that anchor-based entries are merged."""
    mock_data = {
        'docs': [
            {
                'location': 'topics/rag.html',
                'title': 'RAG',
                'text': 'Main content about RAG.',
            },
            {
                'location': 'topics/rag.html#advanced',
                'title': 'Advanced RAG',
                'text': 'Advanced patterns for RAG.',
            },
        ]
    }
    index = AtlasSearchIndex()
    with patch(
        'genai_atlas_mcp_server.utils.search_index.fetch_json',
        new_callable=AsyncMock,
        return_value=mock_data,
    ):
        await index.ensure_loaded()

    docs = index.get_all_docs()
    assert len(docs) == 1
    assert 'Advanced patterns' in docs[0].text
