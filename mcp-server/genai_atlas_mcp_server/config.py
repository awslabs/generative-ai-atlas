# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Configuration settings for the GenAI Atlas MCP Server."""

import os

from pydantic import BaseModel, Field

from . import __version__

# Base URL for the deployed Atlas site (overridable via env var for local dev)
ATLAS_BASE_URL = os.getenv(
    'ATLAS_BASE_URL', 'https://awslabs.github.io/generative-ai-atlas'
)

# URLs for data sources
ATLAS_SEARCH_INDEX_URL = f'{ATLAS_BASE_URL}/search/search_index.json'
ATLAS_LLMS_TXT_URL = f'{ATLAS_BASE_URL}/llms.txt'


class Config(BaseModel):
    """Configuration settings for the MCP server."""

    base_url: str = Field(default=ATLAS_BASE_URL)
    search_index_url: str = Field(default=ATLAS_SEARCH_INDEX_URL)
    llms_txt_url: str = Field(default=ATLAS_LLMS_TXT_URL)
    timeout: float = Field(default=30.0)
    user_agent: str = Field(default=f'genai-atlas-mcp/{__version__}')
    max_concurrent_fetches: int = Field(default=5)


config = Config()
