<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Tokens: The Currency of LLMs

**Content Level: 100**



## Suggested Pre-Reading

- [Key Primitives](../index.md)

## TL;DR

Tokens are the fundamental units LLMs process - neither words nor characters but something in between.
They function as the "currency" of GenAI applications, determining costs (typically priced per 1,000 tokens), context window limits, and performance characteristics.
Understanding how tokenization works is important for cost planning, performance optimization, and architectural decisions when building production LLM applications, particularly for multilingual or domain-specific use cases.

## Tokens: The Currency of LLMs

Tokens are the fundamental units of text processing in language models.
They represent the smallest pieces of text that a model processes, and are neither characters nor words, but something in between as illustrated below.

### Tokenization Process

Text is broken down into tokens during preprocessing:

1. The model's tokenizer analyzes the input text
2. It divides the text into tokens according to its vocabulary
3. These tokens are converted to numerical IDs for model processing

For example, the sentence "I love machine learning" might be tokenized as: `["I", "love", "machine", "learning"]` or `["I", "_love", "_mach", "ine", "_learn", "ing"]`.
It depends on the actual LLM and its implementation how the prompt is tokenized and this process is typically hidden from the user of the LLM.

### Token Economics

Tokens serve as the primary unit of computational cost for LLM usage:

* Pricing models typically charge per 1,000 or 1,000,000 tokens (input and output counted separately)
* Model capabilities and context windows are defined in terms of token counts
* Token efficiency directly impacts application costs and performance

Different languages and specialized content tokenize differently. For example, English typically requires 1.0-1.5 tokens per word, while East Asian languages like Japanese may require 2-3 tokens per word.

## Making it practical
Understanding tokens is important when building and deploying GenAI applications, particularly for cost management, performance optimization, and application design.

### Cost Planning and Budgeting

When deploying LLM-based applications, token usage directly translates to costs:

- **Calculate expected expenses**: For a customer service chatbot processing 10,000 conversations daily, with an average of 200 tokens per user message and 300 tokens per AI response, you'd consume approximately 5M tokens daily. At $0.01 per 1000 tokens, that's $50 daily or $1,500 monthly.
- **Budget appropriately**: Different models have different pricing tiers. Models with larger context windows or specialized capabilities typically cost more per token, requiring careful cost-benefit analysis. 
- **Track consumption**: Implement token counting in your application monitoring to track actual usage against projections and identify cost optimization opportunities.

### Performance Optimization

Token efficiency directly impacts application responsiveness and user experience:

- **Prompt engineering**: Writing token-efficient prompts can reduce costs and improve performance. For example, replacing "Please provide a comprehensive summary of the following text" (around 10 tokens) with "Summarize:" (1 token) achieves the same result with fewer tokens.
- **Chunking strategies**: When working with large documents, develop efficient chunking approaches that maintain context while minimizing token usage.
- **Response streaming**: Implementing token streaming enables displaying AI responses as they're generated rather than waiting for complete responses, improving perceived performance.

### Application Design Considerations

Token limits influence fundamental application architecture decisions:

- **Context window management**: Design your application with token limits in mind. For a 16K context window model, allocate appropriate space for system prompts, conversation history, and new user inputs.
- **Memory mechanisms**: Implement summarization techniques or vector storage for conversation history when working with long-running conversations that would exceed token limits.
- **Graceful degradation**: Build applications that handle token limit errors gracefully, such as automatically summarizing context when approaching limits.

### Multilingual and Domain-Specific Challenges

Token efficiency varies significantly across languages and specialized domains:

**Internationalization planning**: Budget for higher token usage in East Asian languages. A 500-word document might require ~750 tokens in English but ~1,500 tokens in Japanese or Korean.
**Domain adaptation**: Technical, legal, or scientific content often tokenizes less efficiently due to specialized vocabulary. Account for this when designing applications for specific industries.

By understanding tokens as both a technical concept and the "currency" of LLM operations, you can build more cost-efficient, responsive, and effective GenAI applications while avoiding common pitfalls that lead to performance issues or unexpected costs.

## Further Reading
- [Understanding LLM Context Windows: Tokens, Attention, and Challenges](https://medium.com/@tahirbalarabe2/understanding-llm-context-windows-tokens-attention-and-challenges-c98e140f174d){:target="_blank" rel="noopener noreferrer"}
- [Optimizing costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}

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
