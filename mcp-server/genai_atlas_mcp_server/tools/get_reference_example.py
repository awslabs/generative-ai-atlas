# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference example tool for the GenAI Atlas MCP Server."""

from typing import Any, Dict, List, Optional

from ..utils.search_index import get_search_index


async def get_reference_example(
    use_case: str,
    industry: Optional[str] = None,
    max_results: int = 5,
) -> List[Dict[str, Any]]:
    """Find architecture patterns and reference implementations in the Atlas.

    Searches specifically within the Architecture Patterns (section 3) and
    Examples & References (section 6) content areas for practical implementation
    guidance.

    ## Available Industries
    - "financial" or "fis" — Customer onboarding, AML investigation
    - "retail" — Smart product onboarding
    - "healthcare" — Smart prescription reader
    - "cross-industry" — Customer service assistant, IDP, document management,
      contract analysis, marketing campaigns, analytics platforms

    ## Example Queries
    - use_case="chatbot", industry="financial"
    - use_case="document processing"
    - use_case="multi-agent"
    - use_case="RAG", industry="cross-industry"

    Args:
        use_case: The use case to find patterns for (e.g., "chatbot", "RAG",
                  "document processing", "multi-agent").
        industry: Optional industry filter (e.g., "financial", "retail",
                  "healthcare", "cross-industry").
        max_results: Maximum results to return (default: 5).

    Returns:
        List of matching architecture patterns and reference examples.
    """
    index = get_search_index()
    await index.ensure_loaded()

    # Build a targeted query
    query_parts = [use_case]
    if industry:
        query_parts.append(industry)

    query = ' '.join(query_parts)

    # Search but filter to architecture and example sections only
    all_results = index.search(query, max_results=50)

    architecture_keywords = [
        '3_0_architecture', '3_1_system', '3_1_2_architecture',
        '6_0_example', '6_1_reference', '6_3_case_studies',
    ]

    filtered = []
    for result in all_results:
        url_lower = result.url.lower()
        if any(kw in url_lower for kw in architecture_keywords):
            if industry:
                industry_lower = industry.lower()
                # Map common industry names to URL fragments
                industry_map = {
                    'financial': 'fis',
                    'fis': 'fis',
                    'retail': 'retail',
                    'healthcare': 'healthcare',
                    'cross': 'cross_industry',
                    'cross-industry': 'cross_industry',
                }
                url_fragment = industry_map.get(industry_lower, industry_lower)
                if url_fragment not in url_lower and industry_lower not in url_lower:
                    continue
            filtered.append(result)

        if len(filtered) >= max_results:
            break

    # If no architecture-specific results, fall back to general search with a note
    if not filtered:
        general_results = all_results[:max_results]
        return [
            {**r.model_dump(), '_note': 'No architecture-specific results found; showing general results.'}
            for r in general_results
        ]

    return [r.model_dump() for r in filtered]
