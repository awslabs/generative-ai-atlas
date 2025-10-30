<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# GenAI Integration Patterns: Connecting the Key Primitives

**Content Level: 100**



## Suggested Pre-Reading

- [Key Primitives](../index.md)
- [Prompt Engineering](../2_1_1_prompt/2_1_1_prompt.md)
- [Embeddings](../2_1_5_embeddings/2_1_5_embeddings.md)
- [Vector Databases](../2_1_6_vector_databases/2_1_6_vector_databases.md)
- [RAG](../2_1_7_rag/2_1_7_rag.md)

## TL;DR

Generative AI applications require thoughtful integration of key primitives through orchestration patterns (simple chains to agent-based systems) and state management approaches (stateless to external memory).
Your choice of patterns significantly impacts application performance, cost, and user experience. Understanding these patterns helps you design effective GenAI solutions tailored to your business requirements while managing the inherent trade-offs between complexity, accuracy, and operational constraints.

## GenAI Integration Patterns: Connecting the Key Primitives

The primitives introduced primitives combine in various patterns to create complete GenAI applications. Common integration patterns include:

Orchestration Patterns

* Simple chain: Direct flow from prompt to model to response
* Agent-based: Models that can plan, use tools, and make decisions across multiple steps
* Retrieval-enhanced: Systems that augment prompts with information from external sources
* Human-in-the-loop: Workflows that incorporate human feedback or approval at critical points

State Management Approaches

* Stateless: Each interaction is independent, with no memory between requests
* Context-carrying: Passing conversation history with each request
* External memory: Storing conversation state in external systems
* Hybrid: Combining approaches based on conversation importance or duration


## Making it practical

Understanding how these integration patterns and state management approaches apply to real business problems will help you make informed architectural decisions for your GenAI applications.
Here's how to apply these patterns in practice:

### Choosing the right orchestration pattern

When deciding which pattern fits your use case, consider these practical guidelines:

- **Simple chains** work well for straightforward, deterministic tasks like content summarization or basic Q&A where the model can directly process input and generate output without intermediate steps. Implement these for quick wins when your use case requires minimal complexity.

- **Agent-based patterns** are appropriate when your application needs to perform complex reasoning, multi-step tasks, or use external tools. For example, a customer service bot that needs to check inventory, pull order history, and then formulate a response, benefits from this approach. However, be aware that this increases complexity and may require more sophisticated prompt engineering.

- **Retrieval-enhanced patterns** are important when accuracy and up-to-date information are a priority. Implement RAG (Retrieval Augmented Generation) when your use case requires specific knowledge beyond the model's training data or when you need to reduce hallucinations. Common examples include technical support, knowledge base querying, or domain-specific applications.

- **Human-in-the-loop workflows** are important for high-stakes domains like healthcare, finance, or legal applications where incorrect outputs could have serious consequences. Consider implementing approval steps, feedback mechanisms, and confidence thresholds to determine when human intervention is required.

### Implementing state management effectively

The state management approach you choose significantly impacts user experience, system performance, and operational costs:

- **Stateless approaches** are simplest to implement and scale but create disjointed experiences for multi-turn conversations. Use these for one-off query systems or when performance and simplicity are prioritized over conversational context.

- **Context-carrying** works well for moderately complex conversations but watch token limits carefully as conversation history grows. Consider implementing context summarization or pruning techniques to manage this growth over time.

- **External memory** requires additional infrastructure but enables long-running conversations and persistent knowledge across sessions. Implement this when user experience depends on recalling previous interactions or when conversations need to span multiple sessions.

- **Hybrid approaches** offer the most flexibility but require more engineering effort. For example, use context-carrying for immediate conversation flow but store important details in external memory for long-term recall. This works well for complex applications like virtual assistants that need both immediate context and historical memory.

### Implementation considerations

When implementing these patterns, keep these practical points in mind:

1. **Cost management**: More complex patterns typically consume more tokens and computational resources. Monitor costs closely, especially for agent-based systems that may make multiple model calls per user interaction.

2. **Latency trade-offs**: Each added component in your architecture introduces latency. Retrieval steps and tool usage add processing time that impacts user experience. Optimize for critical paths and consider asynchronous processing where possible.

3. **Failure handling**: As complexity increases, so does the potential for failures. Implement robust error handling, fallback mechanisms, and monitoring to enable system reliability.

4. **Evaluation methods**: Different patterns require different evaluation approaches. Simple chains can be evaluated with straightforward metrics like accuracy, while agent systems might require task completion rates or multi-step reasoning evaluation.

The business value of these patterns comes from matching the right approach to your specific use case requirements, considering factors like complexity, accuracy needs, user experience expectations, and operational constraints.


## Further Reading
 - [Prompt engineering techniques and best practices: Learn by doing with Anthropic’s Claude 3 on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}
 - [Best practices to build generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/best-practices-to-build-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}
 - [Incorporate offline and online human – machine workflows into your generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/incorporate-offline-and-online-human-machine-workflows-into-your-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}

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
