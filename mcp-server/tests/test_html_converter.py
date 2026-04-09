# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tests for the HTML converter module."""

import pytest

from genai_atlas_mcp_server.utils.html_converter import (
    extract_diagrams,
    extract_sections,
    html_to_markdown,
)


def test_html_to_markdown_basic():
    """Test basic HTML to markdown conversion."""
    html = '<article><h1>Title</h1><p>Hello world</p></article>'
    result = html_to_markdown(html)
    assert 'Title' in result
    assert 'Hello world' in result


def test_html_to_markdown_empty():
    """Test empty input."""
    assert html_to_markdown('') == ''
    assert html_to_markdown(None) == ''


def test_html_to_markdown_strips_nav():
    """Test that navigation elements are removed."""
    html = '''
    <article>
        <nav>Navigation</nav>
        <h1>Content</h1>
        <p>Body text</p>
        <footer>Footer</footer>
    </article>
    '''
    result = html_to_markdown(html)
    assert 'Content' in result
    assert 'Body text' in result


def test_extract_sections_basic():
    """Test basic section extraction."""
    html = '''
    <html><body>
    <h2>Introduction</h2>
    <p>Intro text</p>
    <h2>Architecture</h2>
    <p>Architecture details</p>
    <h2>Conclusion</h2>
    <p>Final thoughts</p>
    </body></html>
    '''
    result = extract_sections(html, ['Architecture'])
    assert 'Architecture' in result
    assert 'Architecture details' in result


def test_extract_sections_not_found():
    """Test section not found raises ValueError."""
    html = '<html><body><h2>Existing</h2><p>Text</p></body></html>'
    with pytest.raises(ValueError, match='No matching sections'):
        extract_sections(html, ['NonExistent'])


def test_extract_sections_empty_input():
    """Test empty input raises ValueError."""
    with pytest.raises(ValueError):
        extract_sections('', ['Section'])


def test_extract_diagrams():
    """Test diagram extraction from HTML."""
    html = '''
    <html><body>
    <div style="text-align:center">
        <img src="./assets/architecture.png" alt="System Architecture" width="800"/>
    </div>
    <em>Figure 1: System Architecture</em>
    </body></html>
    '''
    diagrams = extract_diagrams(html, 'https://example.com/topics/page.html')
    assert len(diagrams) == 1
    assert diagrams[0]['title'] == 'System Architecture'
    assert 'architecture.png' in diagrams[0]['image_url']


def test_extract_diagrams_skips_small_images():
    """Test that small images (icons) are skipped."""
    html = '<html><body><img src="icon.png" alt="Icon" width="32"/></body></html>'
    diagrams = extract_diagrams(html, 'https://example.com/page.html')
    assert len(diagrams) == 0


def test_extract_diagrams_empty():
    """Test empty input."""
    assert extract_diagrams('', 'https://example.com') == []
    assert extract_diagrams(None, 'https://example.com') == []
