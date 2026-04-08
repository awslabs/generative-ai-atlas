# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""HTML to Markdown conversion utilities.

Follows the same pattern as the AWS Documentation MCP server — extracts the
main content area, strips navigation/footer elements, and converts to markdown.
"""

from typing import List

import markdownify
from bs4 import BeautifulSoup, Tag


def html_to_markdown(html: str) -> str:
    """Convert HTML content to clean Markdown.

    Args:
        html: Raw HTML content.

    Returns:
        Cleaned markdown text.
    """
    if not html:
        return ''

    soup = BeautifulSoup(html, 'html.parser')

    # Find main content area (MkDocs Material theme selectors)
    main_content = None
    content_selectors = [
        'article',
        "div[role='main']",
        '.md-content__inner',
        '.md-content',
        'main',
        '#content',
    ]
    for selector in content_selectors:
        content = soup.select_one(selector)
        if content:
            main_content = content
            break

    if not main_content:
        main_content = soup.body if soup.body else soup

    # Remove navigation and non-content elements
    remove_selectors = [
        'nav',
        'header',
        'footer',
        '.md-header',
        '.md-footer',
        '.md-sidebar',
        '.md-tabs',
        '.md-search',
        '.md-top',
        '.headerlink',
        'script',
        'style',
        'noscript',
    ]
    for selector in remove_selectors:
        for element in main_content.select(selector):
            element.decompose()

    content = markdownify.markdownify(
        str(main_content),
        heading_style=markdownify.ATX,
        autolinks=True,
        escape_asterisks=True,
        escape_underscores=True,
        newline_style='SPACES',
    )

    if not content:
        return ''

    return content.strip()


def extract_sections(html: str, section_titles: List[str]) -> str:
    """Extract specific sections from HTML by heading title.

    Args:
        html: Raw HTML content.
        section_titles: List of section titles to extract.

    Returns:
        Markdown content containing only the requested sections.

    Raises:
        ValueError: If no matching sections are found.
    """
    if not html or not section_titles:
        raise ValueError('No content or section titles provided')

    soup = BeautifulSoup(html, 'html.parser')

    # Normalize requested titles
    normalized_titles = {}
    for title in section_titles:
        # Strip pilcrow (¶) and other anchor markers that MkDocs appends to headings
        cleaned = title.strip().replace('¶', '').strip()
        # Normalize common variations (TL;DR vs TL:DR)
        key = ' '.join(cleaned.lower().split())
        key = key.replace(';', ':').replace('–', '-').replace('—', '-')
        normalized_titles[key] = cleaned

    # Find all headings (h2, h3, h4)
    headings = soup.find_all(['h2', 'h3', 'h4'])
    available_sections = []
    matched_html = []
    found = set()

    for heading in headings:
        heading_text = heading.get_text(strip=True)
        # Strip pilcrow from heading text for matching
        heading_clean = heading_text.replace('¶', '').strip()
        available_sections.append(heading_clean)

        normalized = ' '.join(heading_clean.lower().split())
        normalized = normalized.replace(';', ':').replace('–', '-').replace('—', '-')
        if normalized in normalized_titles:
            section_content = [heading]
            heading_level = int(heading.name[1])  # h2 -> 2, h3 -> 3
            for sibling in heading.find_next_siblings():
                if isinstance(sibling, Tag) and sibling.name in ['h1', 'h2', 'h3', 'h4']:
                    sibling_level = int(sibling.name[1])
                    # Stop at same-level or higher (lower number) heading
                    if sibling_level <= heading_level:
                        break
                section_content.append(sibling)

            section_html = ''.join(str(elem) for elem in section_content)
            matched_html.append(section_html)
            found.add(normalized_titles[normalized])

    if not found:
        section_list = ', '.join(f'"{t}"' for t in section_titles)
        if available_sections:
            available = ', '.join(f'"{s}"' for s in available_sections)
            raise ValueError(
                f'No matching sections found: {section_list}. '
                f'Available sections: {available}'
            )
        raise ValueError(
            'This document does not contain subsections. '
            'Use read_topic to get the full document.'
        )

    result_html = ''.join(matched_html)

    # Note missing sections
    if len(found) < len(section_titles):
        missing = [t.strip() for t in section_titles if t.strip() not in found]
        missing_list = ', '.join(f'"{t}"' for t in missing)
        result_html += (
            f'\n\n<p><strong>Note</strong>: '
            f'Sections not found: {missing_list}</p>'
        )

    return html_to_markdown(result_html)


def extract_diagrams(html: str, page_url: str) -> list:
    """Extract diagram/image references from HTML.

    Args:
        html: Raw HTML content.
        page_url: URL of the page (for resolving relative image paths).

    Returns:
        List of dicts with title, image_url, context, page_url.
    """
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    diagrams = []

    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt', '')

        if not src or not alt:
            continue

        # Ensure we're working with strings (bs4 attrs can be lists)
        src_str = src if isinstance(src, str) else str(src[0]) if src else ''
        alt_str = alt if isinstance(alt, str) else str(alt[0]) if alt else ''

        if not src_str or not alt_str:
            continue

        # Skip logos, icons, and tiny images
        alt_lower = alt_str.lower()
        if any(skip in alt_lower for skip in ['logo', 'icon', 'favicon', 'badge', 'avatar']):
            continue

        width = img.get('width', '')
        width_str = width if isinstance(width, str) else str(width[0]) if width else ''
        if width_str and width_str.isdigit() and int(width_str) < 100:
            continue

        # Resolve relative URLs
        if src_str.startswith('./') or not src_str.startswith('http'):
            # Build absolute URL from page URL
            base = page_url.rsplit('/', 1)[0]
            if src_str.startswith('./'):
                src_str = src_str[2:]
            image_url = f'{base}/{src_str}'
        else:
            image_url = src_str

        # Get surrounding context (caption or nearby text)
        context = ''
        parent = img.parent
        if parent:
            # Check for figure caption
            caption = parent.find(['figcaption', 'em', 'center', 'p'])
            if caption and caption != img:
                context = caption.get_text(strip=True)
            elif parent.name in ['div', 'figure']:
                next_elem = parent.find_next_sibling(['p', 'em', 'center'])
                if next_elem:
                    context = next_elem.get_text(strip=True)[:200]

        diagrams.append({
            'title': alt_str,
            'image_url': image_url,
            'context': context,
        })

    return diagrams
