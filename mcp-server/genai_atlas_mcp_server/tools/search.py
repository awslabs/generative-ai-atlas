# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Search tool for the GenAI Atlas MCP Server."""

from typing import Any, Dict, List

from ..utils.search_index import get_search_index


async def search_atlas(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """Search the Generative AI Atlas for topics matching a query.

    The Atlas is a comprehensive, expert-verified knowledge hub covering all aspects
    of generative AI implementation — from fundamentals to production patterns.

    Content areas include:
    - **GenAI Fundamentals**: Core concepts, business value, responsible AI
    - **Technical Foundations**: Prompts, tokens, embeddings, RAG, fine-tuning, agents, MCP
    - **Architecture Patterns**: System design, chatbots, IDP, multimodal AI, text-to-SQL
    - **Production Framework**: Business strategy, governance, SDLC, operations
    - **Organization Adoption**: AI vision, CoEs, change management
    - **Examples & References**: Industry blueprints (financial services, retail, healthcare)
    - **Resources & Tools**: AWS services, agent frameworks, community resources
    - **ISV Focus**: COGS, ROI, multi-tenancy, IP protection

    Use this tool to find relevant GenAI topics for any development or architecture question.

    Args:
        query: Search terms to find relevant GenAI topics (e.g., "RAG pipeline",
               "multi-agent architecture", "prompt engineering best practices")
        max_results: Maximum number of results to return (default: 5, max: 20)

    Returns:
        List of search results with title, URL, relevance score, and snippet.
    """
    max_results = max(1, min(max_results, 20))
    index = get_search_index()
    await index.ensure_loaded()

    results = index.search(query, max_results=max_results)
    return [r.model_dump() for r in results]
