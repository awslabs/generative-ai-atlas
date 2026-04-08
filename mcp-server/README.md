# Generative AI Atlas MCP Server

Model Context Protocol (MCP) server for the [AWS Generative AI Atlas](https://awslabs.github.io/generative-ai-atlas/) — search, browse, and retrieve expert-verified GenAI knowledge directly from your AI coding assistant.

## Features

- **Search Documentation**: Full-text search across 100+ expert-verified GenAI topics with TF-IDF ranking
- **Read Topics**: Fetch and convert Atlas pages to clean markdown with pagination support
- **Read Sections**: Extract specific sections (TL;DR, Architecture, Benefits) without reading entire pages
- **Browse Topics**: Navigate the full topic hierarchy filtered by section
- **Reference Examples**: Find industry-specific architecture patterns and blueprints
- **Diagrams**: Discover architecture and flow diagrams with clickable image URLs

## Content Coverage

The Atlas covers the full GenAI lifecycle:

| Section | Topics |
|---------|--------|
| GenAI Fundamentals | Core concepts, business value, responsible AI |
| Technical Foundations | Prompts, tokens, embeddings, RAG, fine-tuning, agents, MCP |
| Architecture Patterns | System design, chatbots, IDP, multimodal AI, text-to-SQL |
| Production Framework | Business strategy, governance, SDLC, operations |
| Organization Adoption | AI vision, CoEs, change management |
| Examples & References | Financial services, retail, healthcare, cross-industry |
| Resources & Tools | AWS services, agent frameworks, community |
| ISV Focus | COGS, ROI, multi-tenancy, IP protection |

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) package manager

## Installation

### For Kiro

Add to `~/.kiro/settings/mcp.json` (global) or `.kiro/settings/mcp.json` (project):

```json
{
  "mcpServers": {
    "genai-atlas-mcp-server": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/generative-ai-atlas/mcp-server", "genai-atlas-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": ["search_atlas", "list_topics"]
    }
  }
}
```

### For Cursor / Claude Code

```json
{
  "mcpServers": {
    "genai-atlas-mcp-server": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/generative-ai-atlas/mcp-server", "genai-atlas-mcp-server"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      }
    }
  }
}
```

## Tools

### search_atlas

Search across all Atlas content with ranked results.

```python
search_atlas(query="RAG pipeline optimization", max_results=5)
```

### read_topic

Fetch full topic content as markdown with pagination.

```python
read_topic(url="https://awslabs.github.io/generative-ai-atlas/topics/.../2_1_7_rag.html")
```

### read_sections

Extract specific sections from a topic page.

```python
read_sections(url="...", section_titles=["TL;DR", "Architecture"])
```

### list_topics

Browse the topic hierarchy, optionally filtered by section.

```python
list_topics(section="architecture")
```

### get_reference_example

Find architecture patterns and industry reference implementations.

```python
get_reference_example(use_case="chatbot", industry="financial")
```

### list_diagrams

Find architecture and flow diagrams with image URLs.

```python
list_diagrams(topic="multi-agent")
```

## Development

```bash
# Clone the repo
git clone https://github.com/awslabs/generative-ai-atlas.git
cd generative-ai-atlas/mcp-server

# Install dependencies
uv sync

# Run the server locally
uv run genai-atlas-mcp-server

# Run tests
uv run pytest -v

# Lint
uv run ruff check .

# Type check
uv run pyright genai_atlas_mcp_server/
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FASTMCP_LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | WARNING |
| `ATLAS_BASE_URL` | Override the Atlas site URL (for local dev) | `https://awslabs.github.io/generative-ai-atlas` |

## License

Apache-2.0
