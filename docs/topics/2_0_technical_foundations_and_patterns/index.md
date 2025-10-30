<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->
# Core Concepts Overview

This chapter provides a comprehensive guide to the core technical building blocks of Generative AI applications. It covers key primitives, integration patterns, model types, and advanced architectural concepts that form the foundation for successful GenAI implementations on AWS. This section is recommended for anyone looking to build reliable, scalable, and cost-effective AI solutions using Amazon's services.

## Key Topics Covered

This section explores several aspects of Technical Foundations and Patterns for Generative AI including:

- **[Key Primitives](2_1_key_primitives/index.md)**: The core components that make up Generative AI systems, from prompts and tokens to advanced concepts like agents and context management

- **[Types of Generative AI Models](2_2_types_of_generative_ai_models_and_capabilities/2_2_types_of_generative_ai_models_and_capabilities.md)**: An overview of the diverse GenAI model landscape and their unique capabilities

- **[Data Engineering in LLM Development](./2_3_core_archtectural_concepts/2_3_1_data_engineering/index.md)**: Fundamental concepts, best practices, and practical implementation of data engineering for LLM instruction tuning and fine-tuning processes, including data quality, acquisition methods, and processing pipelines.

- **[Prompt Engineering](./2_3_core_archtectural_concepts/2_3_2_prompt_engineering/index.md)**: The craft of designing effective inputs to guide AI systems, covering key terminology, tokens and embeddings, core components, context management, temperature control, input/output relationships, composition techniques, and technical limitations.

- **[Retrieval Augmented Generation (RAG)](./2_3_core_archtectural_concepts/2_3_3_RAG(retrieval%20Augmented%20Generation)/index.md)**: Building context-aware applications using ingestion pipelines, retrieval strategies, generation workflows, advanced patterns, performance tuning, and structured RAG implementations.

- **[Fine-Tuning and Model Adaptation](./2_3_core_archtectural_concepts/2_3_4_fine-tuning/index.md)**: Techniques for customizing pre-trained models including full fine-tuning, parameter-efficient methods (PEFT, LoRA, QLoRA), preference alignment (RLHF, DPO, GRPO), and model distillation.

- **[Inference in Generative AI](./2_3_core_archtectural_concepts/2_3_5_inference/index.md)**: Strategies for deploying and serving models in production, covering online inference, asynchronous processing, and model serving architectures using SageMaker, Bedrock, and EKS.

- **[Orchestration Patterns](./2_3_core_archtectural_concepts/2_3_6_orchestration_patterns/index.md)**: Fundamental architectural approaches for coordinating GenAI tasks including fan-out/fan-in for parallel processing, prompt chaining for sequential workflows, and human-in-the-loop for quality assurance.

- **[Agentic Systems](./2_3_core_archtectural_concepts/2_3_7_agents_and_autonomous_systems/index.md)**: Advanced AI systems combining LLMs with external capabilities, covering workflow agents, autonomous agents, multi-agent architectures, security considerations, and evaluation methodologies.

- **[Managing Hallucinations and Guardrails](2_5_managing_hallucinations_and_guardrails/hallucinations_and_guardrails.md)**: A detailed view on challenges with inaccurate content and counter-measures. 

- **[Model Evaluation](2_6_model_evaluation_and_selection_criteria/index.md)**: This section provides a deep dive into evaluation techniques for LLM output, corresponding metrics and how to automate such evaluations. 

- **[Output Customization Taxonomy](2_7_output_customization_taxonomy/customization_taxonomy.md)**: There are different approaches for customizing output of LLMs ranging from RAG to customized model training. This section provides a systematic approach for choosing the right approach to customize LLM output in different scenrios. 


## Why It Matters



By the end of this section, you will:



- Understand the foundational components required for building Generative AI applications

- Be able to select appropriate models and architectural patterns based on use case requirements

- Know how to implement cost-effective and performant GenAI solutions

- Have strategies for mitigating common issues like hallucinations and context limitations



The topics build progressively from basic concepts (key primitives) to advanced implementations (agent systems and orchestration), providing both theoretical knowledge and practical guidance. While each section can be read independently, we recommend starting with [Key Primitives](2_1_key_primitives/index.md) to establish a solid conceptual foundation before moving to architectural patterns.



## Prerequisites
Familiarity with basic AWS services and general machine learning concepts is helpful but not required.
