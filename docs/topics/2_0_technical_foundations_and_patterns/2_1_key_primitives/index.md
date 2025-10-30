<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Key Primitives

## Overview
This section introduces the key primitives that are the fundamental building blocks for Generative AI applications. Understanding these core components - from prompts and tokens to embeddings and agents - is important for architects and builders to effectively design, implement, and optimize GenAI solutions. These primitives serve as the core vocabulary and toolkit for translating business requirements into functional AI-powered systems.

## Key Topics Covered

This section explores several important aspects of Key Primitives, including:

- **[Prompts and Common LLM Parameters](2_1_1_prompt/2_1_1_prompt.md)**: The primary interface for communicating with LLMs, including instruction design and parameter tuning for optimal responses.

- **[Responses](2_1_2_model_outputs/2_1_2_model_outputs.md)**: Understanding model outputs, including deterministic vs. non-deterministic generation and various output formats.

- **[Context Windows](2_1_3_context_windows/2_1_3_context_windows.md)**: Managing the LLM's effective "memory" during interactions and strategies for handling conversation history.

- **[Tokens](2_1_4_tokens/2_1_4_tokens.md)**: The fundamental units of text processing that serve as the "currency" of GenAI applications, directly impacting cost and performance.

- **[Embeddings](2_1_5_embeddings/2_1_5_embeddings.md)**: Numerical vector representations that capture semantic meaning, enabling machines to understand relationships between concepts.

- **[Vector Databases](2_1_6_vector_databases/2_1_6_vector_databases.md)**: Specialized storage systems for efficiently indexing and retrieving embedding vectors based on similarity.

- **[Retrieval Augmented Generation (RAG)](2_1_7_rag/2_1_7_rag.md)**: Combining external knowledge sources with LLM capabilities to improve factual accuracy and reduce hallucinations.

- **[Fine-Tuning and Model Adaptation](2_1_8_fine_tuning/2_1_8_fine_tuning.md)**: Adapting pre-trained models for specific use cases through additional training on domain-specific datasets.

- **[Agents](2_1_9_agents/2_1_9_agents.md)**: Autonomous systems that extend LLMs with planning, reasoning, memory, and tool-use capabilities for complex problem-solving.

- **[GenAI Integration Patterns](2_1_10_genai_integration_patterns/2_1_10_genai_integration_patterns.md)**: Common architectural patterns for connecting primitives, from simple chains to agent-based systems.

- **[Model Context Protocol (MCP)](2_1_11_mcp/mcp.md)**: A standardized protocol enabling LLMs to securely access external data sources and tools in real-time.

## Why It Matters
Understanding these key primitives is important for building effective GenAI applications that balance performance, cost, and user experience. By the end of this section, you will:

- Understand how each primitive contributes to the overall functioning of GenAI systems
- Be able to make informed architectural decisions based on the characteristics and trade-offs of different primitives
- Know how to optimize token usage, context management, and retrieval strategies for cost-effective implementations
- Recognize when to apply different techniques like RAG, fine-tuning, or agent architectures based on specific use case requirements
- Understand how to combine these primitives effectively to build production-grade GenAI solutions

These topics build progressively from basic concepts like prompts and tokens to more advanced implementations like agents and integration patterns. While each primitive can be understood independently, their true power emerges when combined strategically to solve complex business problems.

For those new to GenAI, we recommend starting with the fundamentals (prompts, responses, tokens) before progressing to more advanced topics like RAG and agents. Those with existing GenAI experience may benefit from focusing on the integration patterns and practical implementation considerations throughout each topic.

## Contributors

Author/s:

 - Markus Bestehorn - Tech lead Generative AI EMEA 

Primary Reviewers:

 - Yibo Liang - Generative AI Specialist SA 
 - Emily Ransley - Generative AI Specialist SA 

Additional Reviewer/s: 

 - Ana-Maria Olaru - Sr. Program Manager 
 - Andrew Hood - Head of Program Development 
 - Dominic Murphy - Sr Mgr, Applied AI Architecture 
 - Gareth Faires - Sr Generative AI Specialist SA 
