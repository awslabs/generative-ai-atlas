# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Generative AI Atlas MCP Server implementation."""

import os
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from loguru import logger
from mcp.server.fastmcp import FastMCP

from .tools.get_reference_example import get_reference_example
from .tools.list_diagrams import list_diagrams
from .tools.list_topics import list_topics
from .tools.read_sections import read_sections
from .tools.read_topic import read_topic
from .tools.search import search_atlas
from .utils.fetcher import close_client

# Configure logging
logger.remove()
logger.add(sys.stderr, level=os.getenv('FASTMCP_LOG_LEVEL', 'WARNING'))


APP_NAME = 'genai-atlas-mcp-server'

INSTRUCTIONS = """
# Generative AI Atlas MCP Server

This server provides tools to search, browse, and retrieve content from the
Generative AI Atlas — a comprehensive, expert-verified knowledge hub for
GenAI implementation.

## Tool Selection Guide

- **search_atlas**: When you need to find topics about a specific GenAI concept,
  pattern, or technique. Start here when you don't know which page to read.
- **read_topic**: When you have a specific URL and need the full page content.
  Supports pagination for long documents.
- **read_sections**: When you need specific sections from a page (e.g., "TL;DR",
  "Architecture"). More token-efficient than reading the full page.
- **list_topics**: When you want to browse what's available, optionally filtered
  by section (fundamentals, architecture, examples, etc.).
- **get_reference_example**: When you need architecture patterns or industry-specific
  reference implementations. Filters to architecture and example content.
- **list_diagrams**: When you need visual architecture or flow diagrams. Returns
  image URLs and context that users can click to view.

## Best Practices

- Start with search_atlas to find relevant topics, then use read_topic or
  read_sections to get detailed content.
- Use read_sections with "TL;DR" to get quick summaries before reading full topics.
- For long documents, use pagination (start_index) rather than fetching everything.
- Always cite the Atlas URL when providing information to users.
- Use list_topics to discover content areas you might not know about.
"""

@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[None]:
    """Manage server lifecycle — clean up HTTP client on shutdown."""
    try:
        yield
    finally:
        await close_client()


mcp = FastMCP(
    APP_NAME,
    instructions=INSTRUCTIONS,
    lifespan=server_lifespan,
    dependencies=[
        'httpx',
        'beautifulsoup4',
        'markdownify',
        'pydantic',
        'loguru',
    ],
)

# Register all tools
mcp.tool()(search_atlas)
mcp.tool()(read_topic)
mcp.tool()(read_sections)
mcp.tool()(list_topics)
mcp.tool()(get_reference_example)
mcp.tool()(list_diagrams)


def main() -> None:
    """Main entry point for the MCP server."""
    logger.info(f'Starting {APP_NAME}')
    mcp.run()


if __name__ == '__main__':
    main()
