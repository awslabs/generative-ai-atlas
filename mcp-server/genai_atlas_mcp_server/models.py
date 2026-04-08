# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Data models for the GenAI Atlas MCP Server."""

from typing import List, Optional

from pydantic import BaseModel


class SearchResult(BaseModel):
    """A single search result from the Atlas index."""

    title: str
    url: str
    score: float
    snippet: str


class SearchResponse(BaseModel):
    """Complete search response."""

    query: str
    total_results: int
    results: List[SearchResult]


class TopicEntry(BaseModel):
    """A topic entry from llms.txt."""

    title: str
    url: str
    section: Optional[str] = None


class DiagramEntry(BaseModel):
    """A diagram reference found in Atlas content."""

    title: str
    image_url: str
    context: str
    page_title: str
    page_url: str
