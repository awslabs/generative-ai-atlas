<!--
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Key Terminology

**Content Level: 200**

## Suggested Pre-Reading

- [Natural Language Processing Stanford Lectures](https://web.stanford.edu/class/cs224n/){:target="_blank" rel="noopener noreferrer"}
- [Coursera AI Glossary](https://www.coursera.org/resources/ai-terms){:target="_blank" rel="noopener noreferrer"}
- [HuggingFace LLM](https://huggingface.co/docs/transformers/llm_tutorial){:target="_blank" rel="noopener noreferrer"}
- [Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview){:target="_blank" rel="noopener noreferrer"}
- [Prompt Engineering Guide Introduction](https://www.promptingguide.ai/introduction){:target="_blank" rel="noopener noreferrer"}
- [What is prompt engineering?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-prompt-engineering.html){:target="_blank" rel="noopener noreferrer"}

## TL;DR

Key terminology in prompt engineering breaks down into three categories:

- **Prompt Fundamentals**: Basic building blocks like prompts, system messages, and user messages that form the core of any interaction with AI models

- **Interaction Patterns**: How conversations flow between user and AI, including turns, sequences, and context management

- **Implementation Terms**: Technical concepts used in designing and engineering prompts, including templates and formatting patterns

!!! tip "Think of these as your prompt engineering vocabulary - you'll need these terms to understand the more detailed concepts in later sections."

## Prompt Fundamentals

Prompt engineering is the process of crafting optimal inputs for Large Language Models (LLMs) to generate desired responses. Through effective prompting, LLMs can perform a wide range of tasks including classification, question answering, summarization, text and code generation, creative writing, reasoning, entity extraction, and specialized domain tasks in fields like chemistry, physics, and mathematics.

Despite continuous improvements, LLMs have important limitations to consider. They generate probabilistic outputs that may contain errors and can sometimes hallucinate information. For this reason, their outputs should always be verified and tested, particularly in critical applications.

The appropriateness of LLMs varies significantly by context. In high-risk scenarios like financial math calculations where accuracy is important, LLMs alone are not recommended and should instead be combined with tool calling, code interpreters, or other verification systems. However, in lower-risk applications such as verifying digits drawn by preschoolers, LLMs may perform adequately.

Several factors influence the quality of LLM responses:

    - The structure and clarity of your prompts
    - The specificity and information content you provide
    - Your approach to user interaction and engagement
    - The content style and language choices in your prompts

By thoughtfully crafting prompts with these considerations in mind, you can significantly improve the reliability and usefulness of LLM-generated content for your specific needs.

!!! warning "Unlike fine-tuning, prompt engineering does not modify the model's weights or internal parameters. It only involves crafting better inputs to get desired outputs from the existing model."

## Important Glossary

**Prompt**

A text input or instruction given to a Large Language Model (LLM) or AI system to elicit a specific response or perform a task.

- Can include instructions, context, examples, or questions
- May follow specific formats or patterns
- Examples:
    - "Translate Hello world to Polish"
    - "Write a poem about LLMs"

**Interaction**

A single exchange or a series of exchanges between a user and an LLM.

- Components:
    - System message (optional)
    - User message(s)
    - Assistant message(s)
    - Conversation history (if applicable)
- Types:
    - Single-turn: one prompt, one response
    - Multi-turn: ongoing conversation with context
    - Stateless: each interaction is independent
    - Stateful: maintains conversation history
- Examples:
    - Simple interaction:
        - User: "What's the weather?"
        - Assistant: "I don't have access to real-time weather data."
    - Multi-turn interaction:
        - User: "Let's write a story."
        - Assistant: "I'm ready to help. What kind of story?"
        - User: "A science fiction story."
        - Assistant: "Great choice! Shall we start with the main character?"

!!! info "Each interaction can be limited by the model's maximum input size and may be influenced by system messages, conversation history, and other contextual elements provided."

**System Message**

A specialized instruction or context provided to an LLM that defines its role, behavior, and operating parameters for the subsequent interaction. Usually treated by the model with higher priority than regular prompts.

- Primary purposes:
    - Setting the model's role and behavior
    - Defining conversation context
    - Establishing constraints and rules
    - Setting tone and style of responses
- Implementation methods:
    - As first message in conversation
    - Through dedicated system message parameter
    - As part of conversation context
- Examples:
    - "You are a helpful programming assistant. Always provide code examples in your explanations."
    - "You are a professional translator. Respond only with translations, no explanations unless asked."
    - "You are a math tutor for elementary school students. Use simple language and step-by-step explanations."
    - "Respond as a JSON object with 'result' and 'explanation' fields."

!!! warning "System messages significantly influence model behavior but, like prompt engineering, do not modify the model's weights. Their effectiveness can vary between different LLMs and implementations."

**User Message**

The primary input or query from a user to an LLM during an interaction. Contains the actual task, question, or instruction that the model should respond to.

- Characteristics:
    - Follows after system message in conversation
    - Contains the main task or query
    - Can reference previous context or messages
    - May include various content types (text, code, data)
- Common uses:
    - Asking questions
    - Requesting tasks
    - Providing data for analysis
    - Giving feedback
- Examples:
    - "Translate this sentence to Polish: 'Hello, how are you?'"
    - "Write a function that calculates Fibonacci sequence in Python"

!!! warning "User messages are interpreted in the context of any active system message and previous conversation history, but their priority is typically lower than system messages."

!!! info "User message is a type of prompt. While \"prompt\" is a general term for any input to an LLM, \"user message\" specifically refers to prompts in a conversation format, distinct from system messages and assistant responses. In modern LLM applications, prompts are typically structured as a combination of system and user messages."

**Assistant Message**

The response generated by an LLM based on user input and system instructions.

- Characteristics:
    - Follows user messages in conversation
    - Addresses requested tasks or queries
    - Adheres to system message guidelines
    - Can include text, code, or data formats

!!! info "Analyzing assistant message patterns helps prompt engineers refine their techniques and better predict model behavior."

**Context Window**

The maximum amount of text (measured in tokens) that a language model can process as input in a single interaction, including prompts and conversation history.

- Characteristics:
    - Fixed size, specific to each model
- Includes:
    - (Optional) System message
    - (Optional) Previous conversation history
    - Current user message
- Practical implications:
    - Limits length of conversations
    - Affects memory of previous context
    - Influences cost of API calls
    - May require text chunking for long documents

!!! warning "When exceeded, older content may be truncated, which can lead to loss of important context."

## Tokens and Embeddings

**Token**

The basic unit of text that language models process. Text is broken down into tokens before being processed by the model.

- Characteristics:
    - Can represent words, parts of words, or punctuation
    - Different models use different tokenization methods
    - Token count affects processing cost and context window usage
- Examples:
    - "Hello world" might be tokenized as ["Hello", " world"] (2 tokens)
    - "Bedrock" might be tokenized as ["Bed", "rock"] (2 tokens)

**Embedding**

A numerical vector representation of text that captures semantic meaning, enabling mathematical operations on language.

- Characteristics:
    - High-dimensional vectors
    - Similar concepts have similar embeddings
    - Enable semantic search and similarity comparisons
- Amazon Bedrock embedding models:
    - **Titan Text Embeddings V2**: Improved version with batch inference capabilities
    - **Titan Multimodal Embeddings G1**: Supports both text and images
    - **Cohere Embed English/Multilingual**: Specialized for English or multiple languages

## Interaction Patterns

**Conversation Turn**

A single exchange consisting of a user message and corresponding assistant response.

**Chat Sequence**

A series of conversation turns that build upon each other, maintaining context throughout the interaction.

**Request/Response Flow**

The basic pattern where a user sends a request (prompt) and receives a response from the model.

**Single-turn vs Multi-turn**

- **Single-turn**: Independent interactions without conversation history
- **Multi-turn**: Conversations that maintain context across multiple exchanges

**Context Preservation**

The ability to maintain relevant information from previous parts of a conversation or interaction.

**Role-based Interaction**

Interactions where the model assumes a specific role or persona as defined by system messages.

## Further Reading

1. [LLM Prompt Engineering AWS Glossary](https://docs.aws.amazon.com/prescriptive-guidance/latest/llm-prompt-engineering-best-practices/glossary.html){:target="_blank" rel="noopener noreferrer"}
2. [Prompt Hub](https://www.prompthub.us/blog/prompt-engineering-principles-for-2024){:target="_blank" rel="noopener noreferrer"}
3. [Amazon Titan Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan.html){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author/s:**

* Alicja Kwasniewska - Sr Solution Architect 

**Primary Reviewer:**

* Deepika Kumar - Solution Architect 

**Additional Reviewer:**

* Afia Khan - Associate SA - GenAI 

* Kihyeon Myung - Sr Applied AI Architect 