# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""List topics tool for the GenAI Atlas MCP Server."""

from typing import Any, Dict, List, Optional

from ..utils.topic_index import get_topic_index


async def list_topics(section: Optional[str] = None) -> List[Dict[str, Any]]:
    """Browse the Atlas topic hierarchy.

    Returns all available topics from the Generative AI Atlas, optionally
    filtered by section. Use this to discover what content is available
    before diving into specific topics.

    ## Available Sections
    - "fundamentals" — GenAI core concepts, business value, responsible AI
    - "technical" or "foundations" — Prompts, RAG, fine-tuning, agents, evaluation
    - "architecture" — System design patterns, scalability, security, cost
    - "production" — Business strategy, governance, SDLC, operations
    - "adoption" — AI vision, CoEs, change management
    - "examples" — Industry blueprints, case studies, reference code
    - "resources" or "tools" — AWS services, frameworks, community
    - "isv" — ISV-specific guidance

    Args:
        section: Optional filter — partial match against section names
                 (e.g., "rag", "architecture", "examples"). Case-insensitive.

    Returns:
        List of topics with title, URL, and section classification.
    """
    index = get_topic_index()
    await index.ensure_loaded()

    topics = index.list_topics(section=section)
    return [t.model_dump() for t in topics]
