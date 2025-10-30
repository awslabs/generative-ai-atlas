<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Popular Tools, Libraries and Frameworks for AI Agents

**Content Level: 200**

## Suggested Pre-Reading
 - [Core Concepts and Terminology](../../../1_0_generative_ai_fundamentals/1_1_core_concepts_and_terminology/core_concepts_and_terminology.md)
 
## TL;DR

AI Agents represent a transformative approach in Generative AI, supported by a rich environment of **frameworks, libraries** and **tools** that enable AI Agents development, orchestration, evaluation, and deployment. These components facilitate the creation of autonomous AI systems capable of complex reasoning, tool usage, and multi-step task completion. While agent technologies continue to evolve rapidly, this chapter focuses on established patterns and components in AI agent development. Key components span:

* **Frameworks:** Environments that enable agent orchestration, multi-agent collaboration, and complex workflow management
* **Libraries:** Core components that provide building blocks for agent development, tool integration, and memory management
* **Tools:** Utilities that allow agents to access external data, APIs, and resources - including web search, calculators, databases, and third-party services

## Frameworks, Libraries and Tools

The following sections explore the **most common and influential components** in AI agent development — focusing on how frameworks, libraries and tools enable agent creation, orchestration, evaluation, and monitoring. These components form the foundation for building sophisticated AI agents capable of autonomous decision-making, tool usage, and complex task completion. While these categories help organize the discussion, they are not mutually exclusive or exhaustive. The goal here is to provide an **agent development-to-deployment lens** with **common patterns** and **fundamental level concepts**—one that mirrors how developers typically build and deploy AI agents in practice. It's important to note that the perspective and list presented here may become outdated almost daily. Not only is the agent technology landscape evolving rapidly with emerging capabilities, but the speed of development enabled by AI itself has exponentially accelerated the pace that new frameworks, libraries and tools are being built, adopted, improved and replaced.

### Frameworks 

***Frameworks** -  are the foundational software environments used to **develop, orchestrate, and evaluate** AI agents. They range from single-agent frameworks to sophisticated multi-agent orchestration systems. This section will mainly focus on common subcategories of agent frameworks:*

#### **Agentic Frameworks and LLM Orchestration Frameworks**

As GenAI applications become more interactive and multi-modal, orchestration frameworks emerge to coordinate model behavior, tool integration, and memory over long sessions. Those frameworks can be used in multiple use cases including RAG, Automatic Chatbot, Content Generation and Data Analysis. The provided common frameworks go beyond single prompts and responses, enabling LLMs to act as agents within broader workflows. *Note: Customers are choosing agent frameworks based on popularity, ease of use, LLMs supported, and other factors. There's no clear **best** framework today.* 

* **[LangChain](https://www.langchain.com/){:target="_blank" rel="noopener noreferrer"}**: LangChain is a modular framework for composing LLM applications through chains of prompts, tools, memory, and logic. LangChain excels in combining different components into a Chain structure. It’s very good at **simple sequential workflows and quick prototyping**, for example: Document Processing, Chatbots and simple automation. 

* **[LangGraph](https://github.com/langchain-ai/langgraph){:target="_blank" rel="noopener noreferrer"}**: LangGraph uses a graph paradigm for orchestrating Large Language Model (LLM) interactions, implementing stateful workflows through a graph-based architecture. At its core, LangGraph extends the LangChain framework by introducing explicit state management and transition logic, enabling developers to model complex agent behaviors as state machines. 

    This approach offers several significant advantages: it provides clear visibility into agent execution paths, enables sophisticated error handling through explicit state transitions, and allows for granular control over agent behavior patterns. However, organizations implementing LangGraph should carefully consider its operational characteristics. The framework's relative immaturity compared to traditional workflow engines may impact production reliability, while its tight coupling with LangChain creates potential dependency management challenges. Additionally, implementing proper observability across state transitions requires careful architectural consideration, particularly in distributed deployment scenarios. LangGraph supports almost any LLM and model provider through LangChain libraries.

* **[AutoGen](https://microsoft.github.io/autogen/stable//index.html){:target="_blank" rel="noopener noreferrer"}**: AutoGen implements a flexible multi-agent orchestration framework that emphasizes conversational interaction patterns between autonomous agents, introducing a unique approach to agent collaboration through dynamic message passing and role-based execution. At its core, AutoGen enables the creation of persistent agent networks where each agent maintains its own conversation memory and execution context, facilitating complex multi-turn interactions and sophisticated task decomposition. 

    This architecture offers several compelling advantages: it provides native support for human-in-the-loop interactions, implements efficient parallel processing through asynchronous agent communication, and enables dynamic conversation branching through its flexible messaging system. However, organizations implementing AutoGen should carefully consider its operational implications. The framework's conversation-centric design can lead to increased token consumption as context accumulates across multiple agent interactions, while its flexible architecture may require careful guardrail implementation to prevent infinite conversation loops or unintended agent behaviors. Additionally, organizations must implement robust error handling and monitoring strategies to manage the complexity of concurrent agent conversations, particularly in production environments. AutoGen primarily supports OpenAI and Azure OpenAI.

* **[CrewAI](https://docs.crewai.com/introduction){:target="_blank" rel="noopener noreferrer"}**: CrewAI is a collaborative multi-agent orchestration framework that implements a hierarchical team structure for coordinating agents. At its core, Crew AI employs a **"manager-worker"** paradigm, where a designated manager agent decomposes complex tasks and delegates subtasks to specialized worker agents, each optimized for specific functions. CrewAI organizes their multi-agent framework into four concepts: agents, tasks, crews and flows. Each crew contains one or more tasks and one or more agents that solve those tasks. Flows act as a higher-level abstraction that lets developers chain together coding tasks and crews - enabling modular, coordinated and complex multi-step AI workflows. 

    This architecture offers several advantages: it enables sophisticated task decomposition, promotes parallel execution of independent subtasks, and implements native conflict resolution through the manager's oversight. The framework's built-in role system allows organizations to define clear agent responsibilities and interaction patterns, while its task queue management facilitates efficient resource utilization. However, implementations must carefully consider several operational challenges. The framework's approach to state management can lead to increased token consumption due to context preservation across agent interactions, while the hierarchical structure may introduce additional latency through manager-worker communication overhead. Organizations must also implement robust error handling strategies to manage potential failure cascades across the agent hierarchy. It can be difficult to go outside Crew's native paradigm, and it doesn't yet offer an easy way to plug in different building blocks for memory or other capabilities. (As of April 2025, Crew implements local memory only, via SQLite and Chroma, with no way of changing it. That poses challenges running it in a distributed system, and there is s no way to extract the memory into your own memory management system.) Crew offers good support for most LLMs and providers.

* **[Strands Agents](https://strandsagents.com/0.1.x/){:target="_blank" rel="noopener noreferrer"}**: Strands Agents is an open-source, model-driven framework for building AI agents with minimal code developed by Amazon. It natively integrates with AWS services for autonomous workflows. Strands Agents simplifies agent development by allowing developers to define a simple agent with just three components: model, tools and prompt. Strands Agents offers versatile deployment options, accommodating both local development and scalable cloud environments. At its core, the agentic loop enables the language model to autonomously plan actions, invoke tools and process results iteratively until a task is completed, leveraging the advanced reasoning capabilities of modern LLMs. 

    This implementation offers several distinct advantages: The integration with Model Context Protocol (MCP) facilitates seamless connections between agents and various data sources or services. Strands Agents also supports a wide range of models, including models in Amazon Bedrock, Anthropic, Ollama, Meta, and other model providers through LiteLLM. However, as a relatively new framework, the community support is still growing. 

* **[LlamaIndex](https://github.com/run-llama/llama_index){:target="_blank" rel="noopener noreferrer"}**: LlamaIndex's agent framework is a data-centric approach to LLM orchestration, implementing an architecture that tightly integrates retrieval-augmented generation (RAG) with agent behaviors. At its core, LlamaIndex agents leverage the framework's sophisticated data structures and query engines to enable context-aware task execution, with built-in capabilities for recursive retrieval and structured data interaction. 

    This implementation offers several distinct advantages: agents can dynamically access and reason over hierarchical knowledge bases, execute complex query plans against structured and unstructured data sources, and maintain coherent interaction patterns through integrated memory management. However, organizations implementing LlamaIndex agents should carefully consider the operational implications. The framework's deep integration with its underlying data structures, while powerful, can introduce performance overhead during complex retrievals, and the query planning system may require careful tuning to optimize token usage. Additionally, organizations must implement appropriate caching strategies to manage the computational cost of repeated index operations during agent execution. Despite these considerations, LlamaIndex's agent capabilities are particularly well-suited for applications requiring sophisticated data interaction patterns and complex knowledge navigation, especially in scenarios where RAG-based reasoning is central to agent behavior. LlamaIndex supports most LLMs and providers.

* **[Semantic Kernel](https://github.com/microsoft/semantic-kernel){:target="_blank" rel="noopener noreferrer"}**: Semantic Kernel represents Microsoft's architectural approach to LLM integration, implementing a modular framework that bridges traditional software development patterns with AI capabilities. At its core, the framework introduces the concept of "semantic functions" - composable units that combine natural language semantics with structured programming constructs, enabling integration between LLM reasoning and conventional application logic. 

    This architecture offers several significant advantages: it provides native support for popular software development patterns, implements strong typing and interface contracts for AI operations, and enables sophisticated memory management through its context system. However, organizations implementing Semantic Kernel must carefully consider its operational characteristics. The framework's emphasis on .NET integration, while powerful for Microsoft-centric environments, may introduce complexity in polyglot architectures. Its plugin system, though flexible, requires careful attention to versioning and dependency management, particularly when implementing custom semantic functions. Additionally, organizations must implement appropriate abstraction layers to manage the framework's tight coupling with specific LLM providers. Semantic Kernel provides its own plugins for many LLMs and providers.

* **[PydanticAI](https://github.com/pydantic/pydantic-ai){:target="_blank" rel="noopener noreferrer"}**:Pydantic AI's programming model emphasizes defining AI agents through Pydantic models, enabling structured data handling and type validation for both agent inputs and outputs. It leverages Pydantic's robust data validation capabilities to ensure reliable interactions with external tools and APIs. It offers strong type safety, simplified data serialization and deserialization, and enhanced code clarity through declarative model definitions. 
    
    The integration with Pydantic facilitates data exchange between agents and other Python systems. However, it has a potentially steeper learning curve for developers unfamiliar with Pydantic, is newer and not as mature as other frameworks, and a reliance on Pydantic's data modeling paradigm might not suit all agent architectures. Pydantic has growing support for LLMs and providers, and an open integration point to add more.

***Summary of the Agentic and LLM Orchestration Frameworks***

| Framework | Paradigm | Strengths | Weaknesses | LLMs and model providers |
|:--|:--|:--|:--|:--|
| LangChain | Modular, chain-based orchestration | • Rapid Prototyping<br> • Modular design for chaining components | • Can become complex with intricate chains<br> • Have limitation on multi-agent collaboration | Supports most LLms and providers |
| LangGraph | Graph-based workflows | • Supports all workflow patterns<br> • Integrates with other tools and agents through custom graph nodes<br> • Vibrant community (LangChain) | • Graph state handling can be complex<br> • Graph programming can be unintuitive<<br> • Graphs are not type safe, which can lead to bugs that are hard to diagnose | Supports any LLM and model provider available through LangChain |
| AutoGen | Asynchronous multi-agent collaboration | • Supports multiple workflows<br> • Multi-agent support | • Limited observability options<br> • Can be difficult to debug | Primarily OpenAI and Azure OpenAI, with experimental support for Anthropic and Gemini |
| Crew.ai | Role-based collaboration | • Intuitive model of agents, crews, and flows.<br> • Good documentation | • Difficult to customize if the native paradigm doesn't work<br> • Immature, e.g. cannot bring custom memory | Supports most LLMs and providers |
| Strands Agents | Model-driven agent with tool usage and reasoning capabilities | • Simplified agent creation<br> • Flexible deployment across environments | • New and lacking some features | Support most LLMs and providers |
| LlamaIndex | Agent and tool building blocks with custom workflow support | • Several pre-built tools<br> • Several workflow templates<br> • Can deploy an agent as a microservice<br> • LlamaIndex is known for RAG capabilities | • LlamaIndex mostly known for retrieval, not agents<br> • May have performance overhead | Supports most LLMs and providers |
| Semantic Kernel | Skill-based integration | • Strong architecture with support for Python, Java, and C#<br> • Integration with Microsoft environment | • Limited external API integration<br> • Support for memory and tools can be problematic | Connectors for many LLMs and providers |
| Pydantic AI | Python-centric design | • Strong track record of open-source success (makers of Pydantic)<br> • Type-safe programming model | • New and lacking some features | Supports many LLMs and providers, with a simple way to add more |

#### **Retrieval-Augmented Generation (RAG) Evaluation Frameworks**

RAG Evaluation frameworks provide objective methods to assess the performance and reliability of the RAG system. 

* **[RAGAS](https://docs.ragas.io/en/stable/){:target="_blank" rel="noopener noreferrer"}**: An evaluation framework designed specifically for **retrieval-augmented generation (RAG)** pipelines. It assesses both retrieval quality and generation correctness, offering metrics such as faithfulness and context relevance.

#### **Agentic Observability and Tracing Frameworks**

Monitoring generative systems in production is important for enabling safety, responsiveness, and quality. Observability tools enable tracing of inputs, outputs, and intermediate states of AI Agent' reasoning. Some framework also extends to have a dashboard with latency, time span, token usages and human-in-the-loop comments for further performance improving. Here are two common tracing frameworks: 

* **[Langfuse](https://langfuse.com/){:target="_blank" rel="noopener noreferrer"}**: Langfuse is a lightweight service for logging, tracing, and analyzing LLM pipelines. It integrates with popular orchestration frameworks and provides dashboards to visualize prompt flows, latency, and failure cases. Langfuse also incorporates a robust feedback system that enables users to maintain and improve their LLM applications. Users can add detailed comments and annotations to specific traces, providing context and insights into system behavior.

* **[LangSmith](https://www.langchain.com/langsmith){:target="_blank" rel="noopener noreferrer"}**: LangSmith is a full-featured evaluation and observability framework with support for agent debugging, prompt versioning, and interactive logs. It helps developers understand agent behavior and refine system design based on real-world interactions. While it originated within the LangChain environment, LangSmith functions independently and can be integrated with any LLM framework. Langsmith addresses common development challenges like debugging non-deterministic behaviors, monitoring token usage and latency, and evaluating model performance


### Libraries 

***Libraries** – provide essential building blocks for AI agent development, offering components for agent behaviors, tool integration, memory management, and deployment. These libraries simplify the process of creating sophisticated agents capable of complex reasoning and task execution.*

* **[Model Context Protocol (MCP)](https://github.com/modelcontextprotocol){:target="_blank" rel="noopener noreferrer"}**: Model Context Protocol (MCP) is an open protocol that defines standard interfaces for AI agents to interact with external tools, APIs, databases, and content repositories, and bring real-world context into their reasoning. It replaces fragmented, custom integrations with a universal interface for reading files, executing functions, and exchanging contextual information. By making data sources and developer tools uniformly accessible, MCP simplifies building context-aware applications which supports workflows spanning code generation, CRM automation, and document analysis, etc. However, MCP is still in early-stage: remote MCP servers introduce security concerns such as prompt injection, governance limits, and challenges handling scale and discovery as adoption grows.

* **[Agent‑to‑Agent (A2A)](https://github.com/a2aproject){:target="_blank" rel="noopener noreferrer"}**: Agent‑to‑Agent (A2A) Protocol is a complementary open standard library aimed at enabling robust, peer-to-peer collaboration between autonomous AI agents. Unlike MCP focuses on context within an Agent. A2A let autonomous AI agents discover, negotiate, and delegate tasks across diverse frameworks and vendors through a shared communication layer. Built on familiar web technologies like HTTP, SSE, and JSON‑RPC, A2A supports secure exchange of goals, state updates, action requests, and error handling—all wrapped within enterprise-grade authentication, audit logs, and safety controls. 

    The formation of Agent2Agent project is under the Linux Foundation. Google has transferred the A2A protocol specification, SDKs, and developer tooling to this independent entity. With over 100 companies now supporting the protocol, including AWS and Cisco as recent validators, A2A is positioned to break down silos in AI agent communication. This strategic move under the Linux Foundation's neutral governance ensures the protocol remains vendor-agnostic and community-driven, fostering broader adoption and collaborative development. Similar to MCP, A2A remains nascent, and deploying agent meshes introduces architectural complexity, requires careful governance, and needs more maturity in managing discovery, credentialing, and error recovery.

### Tools 

***Agent Tools -** extend the capabilities of GenAI Agents by enabling them to interact with external system and perform actions. These tools allow AI models to access real-world data and execute specific tasks based on the environment. Agents can utilize multiple tools to accomplish complex tasks through reasoning and sequential decision-making.* *This section covers sample agent tools and AWS AI/ML Tools:*

#### Agent Tools

* **[LangChain Tools](https://python.langchain.com/docs/integrations/tools/){:target="_blank" rel="noopener noreferrer"}** : A mature abstraction for exposing functions to models with clear names, descriptions, and JSON-schema’d inputs, supported via LangChain and LangGrpah. Tools can be bundled into “toolkits” and used by agents in both Python and JS runtimes. Users can author tools with simple decorators and support sync/async flows, making them easy to test and reuse across projects. LangChain Tools support a wide range of functionalities such as Search, Code Interpreter, Web Browsing, database, etc. 

* **[Strands Agents Tools](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/tools/tools_overview/){:target="_blank" rel="noopener noreferrer"}** : An open-source SDK from Strands Agents Framework for building production agents with strong AWS integrations. It supports native tooling (including community tool packs for file ops, shell, web/API calls, and orchestration), runs well on AWS (EKS, Lambda, EC2), and offers observability and deployment patterns suited for enterprise use. Strands also plays nicely with MCP tools for standardized connections. 

* **[MCP Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools){:target="_blank" rel="noopener noreferrer"}** : An open standard from Anthropic that lets AI Agents connect external sources for any model providers via a consistent client/server protocol—often described as the “USB-C” for AI integrations. MCP simplifies wiring agents to repos, databases, and services, and is gaining broad application support. Like LangChain Tools and Strands Agents Tools, users can customize MCP tools through `@mcp.tool` decorator.

#### **AWS AI/ML Tools**

AWS also provides a comprehensive suite of managed services and tools specifically designed for AI Agents development and deployment. Tools (like Amazon Q) integrate seamlessly with AWS's broader cloud infrastructure while abstracting much of the underlying complexity of working with foundation models. More information can be founded [here](https://aws.amazon.com/ai/services/){:target="_blank" rel="noopener noreferrer"}


## Making it practical

The frameworks, libraries, and tools introduced in this chapter form the **technical foundation of modern AI agents architectures**. They show up in ways both explicit and subtle, depending on where in the stages of the development lifecycle

* For **Agentic or LLM orchestration**, orchestration frameworks like CrewAI or LangGraph provide structure and flexibility. These become particularly important in assistant-style applications, RAG systems, or multi-modal flows that involve tool calling or memory.
* Once AI Agents solution is live, **observability frameworks** (like Langfuse and LangSmith) are important for enabling robustness and faithfulness. 

Here are two common guidances with Frameworks, Libraries and Tools: 

**RAG Implementation Guidance**

For building enterprise search or knowledge base applications, customers can combine multiple components. customers might use **LangChain or LangGraph framework** to orchestrate the RAG pipeline, connecting vector databases with LLMs . The **RAGAS framework** becomes important here for evaluating retrieval quality and generation faithfulness. Consider using **Amazon Bedrock's knowledge base** feature for managed RAG implementations, or build custom solutions using frameworks like LangChain with Amazon Bedrock's foundation models.

**Multi-Agent System Guidance**

When developing complex workflows like automated research assistants or business process automation, customers will work with **frameworks like AutoGen or CrewAI**. For instance, in a document processing pipeline, customers might create specialized agents for different tasks - one for initial document analysis, another for data extraction, and a third for quality checking. **Amazon Bedrock Agents** can also simplify this by providing managed agent capabilities with built-in integration to AWS services.

## Further Reading

* [Build agentic systems with CrewAI and Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}
* [Fine-tune Meta Llama 3.1 models for generative AI inference using Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/fine-tune-meta-llama-3-1-models-for-generative-ai-inference-using-amazon-sagemaker-jumpstart/){:target="_blank" rel="noopener noreferrer"}
* [Strands Agent](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/){:target="_blank" rel="noopener noreferrer"}
* [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/){:target="_blank" rel="noopener noreferrer"}
* [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/){:target="_blank" rel="noopener noreferrer"}
* [Amazon Q](https://aws.amazon.com/q/){:target="_blank" rel="noopener noreferrer"}
* [Amazon Bedrock](https://aws.amazon.com/bedrock/){:target="_blank" rel="noopener noreferrer"}

## Contributors

Author/s:

 - Di Wu - Deep Learning Architect 
 - Randy DeFauw - Sr. Principal SA 
 - Tanner McRae - Sr. Applied AI Architect 

Primary Reviewers:

- Andrew Baird - Sr. Principal Solutions Architect 
- Don Simpson - Principal Technologist 
- Jagdeep Singh Soni - Sr. AI/ML Spec. SA 
- Fernando Galves - GenAI Solutions Architect 
