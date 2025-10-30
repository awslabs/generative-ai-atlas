<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Data Insight Architecture

**Content Level:** 300

## Suggested Pre-Reading

- [Foundation Architecture Components](../../3_1_1_foundation_architecture_components/index.md)
- [Application Engine](../../3_1_1_foundation_architecture_components/3_1_1_2_application_engine/index.md)
- [LLM Gateway](../../3_1_1_foundation_architecture_components/3_1_1_4_llm_gateway/index.md)
- [Tool Gateway](../../3_1_1_foundation_architecture_components/3_1_1_6_tool_gateway/index.md)


## TL;DR

Data Insight Architecture leverages LLMs to translate natural language into queries for data stores, enabling visualization and insight generation without specialized programming knowledge. Success depends on creating appropriate translation layers that account for data store characteristics, applying patterns like RAG and agents for complex scenarios, and establishing feedback loops for continuous improvement.

## Introduction
Organizations face a critical challenge: valuable data exists in structured repositories but remains inaccessible to those who need it most. LLM-powered data insight architecture bridges this gap by providing natural language interfaces to data stores, enabling broader access and accelerating insight generation.

## Core Architectural Pattern

The fundamental pattern introduces an intelligent translation layer between users and data repositories. This architecture consists of three key components:

1. **Interaction Layer**: Processes natural language requests and presents results
2. **Translation Layer**: Converts natural language into query languages and transforms results
3. **Data Store Layer**: Contains repositories and executes queries

## Implementation Variations

Translation mechanisms must adapt to different data repository types. Each type requires specialized approaches:

- **Relational Databases (Text-to-SQL)** implementations focus on schema comprehension, join path determination, and SQL optimization. These systems excel at converting precise questions into structured queries across normalized data models.

- **Business Intelligence Systems (Generative BI)** emphasize semantic mapping, visualization selection, and metric calculation. These implementations bridge business terminology with technical implementation while presenting results in appropriate visual formats.

As environment complexity increases, architectural approaches should evolve accordingly. Simple schemas may use direct translation, while enterprise data warehouses require sophisticated patterns including RAG-enhanced methods and agent-based architectures for accurate results.

## Critical Success Factors

Effective data insight architectures depend on three key elements that work together to enable accurate natural language to query translation.

**Data Context Enhancement** creates the foundation for accurate translation by bridging the gap between business language and technical implementation. Organizations must enrich their schemas with comprehensive business descriptions that translate technical field names and table relationships into terminology users naturally employ. Building comprehensive libraries of example queries becomes essential, showcasing both straightforward questions and complex analytical patterns that demonstrate proper query construction. Creating detailed semantic mappings between business terms and underlying technical structures enables the system to understand when users refer to "revenue" they might mean a calculated field combining multiple database columns, or when they mention "customers" they could be referencing several related tables depending on context.

**Effective Translation Components** improve accuracy through specialized processing that breaks complex translation tasks into manageable steps. Rather than attempting direct natural language to SQL conversion, successful implementations separate intent detection, entity recognition, and query construction into discrete phases. This decomposition enables more precise handling of ambiguous terminology where the same business term might reference different technical concepts depending on context. Each data store type requires appropriate validation techniques—relational databases need SQL syntax and join validation, while business intelligence systems require metric calculation and dimensional consistency checks.

**Continuous Improvement Mechanisms** drive increasing accuracy over time through systematic learning from user interactions and query outcomes. The most successful implementations establish comprehensive feedback collection processes that capture both successful query executions and user corrections when results don't meet expectations. These systems continuously expand their example libraries with proven patterns while refining metadata and semantic mappings based on real-world usage patterns. Regular analysis of translation challenges reveals common failure modes that can be addressed through enhanced documentation, improved example coverage, or refined processing logic.

## Further Reading

- [Text-to-SQL Application](3_1_2_4_1_text_to_sql_application/3_1_2_4_1_text_to_sql_application.md)
- [Generative BI](3_1_2_4_2_generative_bi/3_1_2_4_2_generative_bi.md)
- [Knowledge Base](../../3_1_1_foundation_architecture_components/3_1_1_5_knowledge_base/index.md)
- [Application Engine](../../3_1_1_foundation_architecture_components/3_1_1_2_application_engine/index.md)

## Contributors

**Author**:

* Kihyeon Myung - Senior Applied AI Architect 

**Primary Reviewer**:

* Don Simpson - Principal Technologist 
