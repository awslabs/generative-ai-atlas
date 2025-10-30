<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->
# Agentic Systems Overview

Agentic systems represent a fundamental evolution in Generative AI, combining large language models with external capabilities like tools, memory, and retrieval to create AI systems that can either follow predefined workflows or operate autonomously to accomplish complex tasks. These systems extend beyond simple prompt-response interactions to enable dynamic decision-making, multi-step reasoning, and orchestrated problem-solving at scale. Understanding agentic systems is important for architects and developers looking to build sophisticated AI applications that can adapt, learn, and execute tasks with varying degrees of autonomy.

## Key Topics Covered

This section explores several key aspects of agentic systems, including:

 - **[What Is An Agentic System?](2_3_7-1_getting_started/what_is_an_agentic_system.md)**: Understanding the fundamental concepts of agentic AI, distinguishing between workflows, autonomous agents, and hybrid systems.

 - **[Design Patterns for Workflow Agentic Systems](2_3_7-3_workflow_agents/design_patterns.md)**: Exploring common patterns like prompt chaining, routing, parallelization, orchestrator, and evaluator for building workflow-based agentic systems.

 - **[Understanding Autonomous Agents](2_3_7-4_autonomous_agents/understanding_autonomous_agents.md)**: Deep dive into agents that orchestrate themselves, including ReAct, ReWOO, and Plan-and-Solve approaches, along with their tools, memory, and retrieval capabilities.

 - **[Multi-Agent Architectures](2_3_7-5_multi_agent_systems/multi_agent_architectures.md)**: Coordinating multiple specialized agents to perform complex tasks more effectively than single general-purpose agents.

 - **[Testing and Evaluation](2_3_7-6_reference_architectures/testing_and_evaluation.md)**: Methodologies for evaluating agent performance, including task success rate, LLM-as-a-Judge approaches, and assertion-based testing.

## Why It Matters

Agentic systems represent the next frontier in applied Generative AI, moving beyond simple chatbots to create intelligent systems capable of complex reasoning and autonomous action. As organizations seek to automate sophisticated workflows and enable AI-driven decision-making, understanding the spectrum from workflow-based to fully autonomous agents becomes important for making informed architectural decisions. The choice between different agentic patterns directly impacts system performance, cost, reliability, and the ability to maintain appropriate human oversight in high-stakes applications.

By the end of this section, you will:

- Understand the fundamental differences between workflows, autonomous agents, and hybrid agentic systems
- Be able to select and implement appropriate design patterns for workflow-based agentic systems
- Know how to architect autonomous agents with proper orchestration, tools, memory, and retrieval capabilities
- Understand how to design and implement multi-agent systems that leverage specialized agents for complex tasks
- Know how to evaluate and test agentic systems using metrics like task success rate and assertion-based approaches
- Understand the trade-offs between different agentic approaches regarding latency, cost, error rates, and complexity

These topics build progressively from foundational concepts to advanced implementations. While workflow patterns provide predictable, controlled execution suitable for well-defined tasks, autonomous agents offer flexibility for complex, dynamic scenarios. Multi-agent architectures combine these approaches, enabling sophisticated systems that balance autonomy with reliability. Throughout, security and evaluation considerations ensure these powerful systems remain trustworthy and aligned with business objectives.

**Prerequisites**: Readers should have a solid understanding of [GenAI Primitives](../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/index.md), particularly [prompts](../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_1_prompt/2_1_1_prompt.md), [LLM parameters](../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_1_prompt/2_1_1_prompt.md), and [integration patterns](../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_10_genai_integration_patterns/2_1_10_genai_integration_patterns.md). Familiarity with [RAG](../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_7_rag/2_1_7_rag.md) and basic prompt engineering concepts will be helpful for understanding agent retrieval and tool use capabilities.

