<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Online Inference

**Content Level: 200**

## Suggested Pre-Reading

 * [Responses: Understanding Model Outputs](../../../2_1_key_primitives/2_1_2_model_outputs/2_1_2_model_outputs.md)
 * [Key Primitives](../../../2_1_key_primitives/index.md)

## TL;DR

Online inference in Generative AI involves real-time processing of prompts to generate immediate responses, which is important for interactive applications like chatbots and content generation tools. This approach requires careful balance of model performance, resource utilization, and response quality to meet user expectations for immediate, coherent responses. Understanding these concepts is important for building production-ready applications that deliver responsive user experiences.

## Understanding Online Inference

Online inference enables real-time interaction between users and Generative AI models, processing individual requests as they arrive to support interactive applications. AI chatbots enable natural conversations, while real-time tools assist content creators with immediate feedback. Creative professionals use AI for text completion, code generation, and image creation, enhancing their creative process. In business, online inference powers 24/7 customer service automation, rapid document generation, and real-time data analysis for decision-making. These applications showcase how online inference delivers immediate, valuable outputs across creative, technical, and business domains.
Online inference consists of three interconnected stages: prompt processing, content generation, and response management.

* **Prompt processing**: The journey begins with prompt processing, where real-time tokenization efficiently converts user inputs into model-readable tokens. This process works in tandem with context management, which maintains conversation flow by tracking previous exchanges. Throughout this stage, input validation and safety checks screen prompts for inappropriate content and enable security compliance, creating a protective foundation for the interaction.
* **Content generation**: As the process moves into content generation, the model constructs responses through token-by-token generation, making incremental decisions about each content piece. This generation occurs alongside stream-based delivery, allowing users to receive content immediately rather than waiting for complete responses. During this phase, quality monitoring continuously checks the generated content for accuracy and coherence, enabling real-time adjustments when needed.
* **Response management**: The final stage, response management, refines and safeguards the output. The system formats the generated content into user-friendly presentations while applying content filtering to screen for inappropriate material. Robust error handling mechanisms work throughout the process to manage any issues that arise, ensuring reliable system performance and a smooth user experience. 

These three stages work in harmony to create a seamless, secure, and efficient online inference system that delivers high-quality AI outputs in real-time. 

## Making it Practical

Imagine a customer service representative waiting for an AI response while a client grows impatient, or a developer losing their flow while waiting for code suggestions. Delays can break the natural rhythm of interaction and diminish the value of even the most sophisticated AI solutions. The ability to generate high-quality, contextually relevant content in real-time while managing resources efficiently is key to providing value to users. 
Achieving optimal performance requires a thoughtful, multi-faceted approach. Smart prompt engineering keeps conversations focused and efficient. Careful system architecture enables smooth information flow across geographic distances. Caching strategies and intelligent routing help balance the complex trade-offs between speed, quality, and cost. The journey to AI responsiveness is ongoing, requiring continuous monitoring and refinement. 

Let's break down how models process and generate text using an example. Consider this prompt: "The quick brown fox jumps over the lazy"

### Prefill and Key-Value (KV) Cache

When the model first receives this input, it performs what we call the "prefill" phase. During prefill, the model processes the entire input sequence at once, computing attention patterns between all the words. This is computationally intensive because each word needs to understand its relationship with every other word in the sequence.
The key-value (KV) cache is where the magic happens for subsequent token generations. Instead of recomputing these attention patterns from scratch for each new word, the model stores the previously computed key-value pairs in memory. Think of it like a chef who keeps their commonly used ingredients within arm's reach rather than walking to the pantry each time they need something. When the model needs to generate the next word (likely "dog" in our example), it can reference this cache instead of recalculating everything from scratch. This dramatically speeds up the generation process. In practical terms, this could mean the difference between an application responding in 100ms versus 500ms.

### Model Parallelism: Divide and Conquer

Modern language models are massive. They often exceed the memory capacity of a single GPU. Model parallelism solves this by splitting the model across multiple devices, similar to how a large company distributes work across different departments. Consider a model with several billion parameters. Running this on a single GPU would be impossible, but we can split it across multiple GPUs. For instance, if we have 8 GPUs, we could distribute the model's neural network layers across them. While one GPU processes the first part of the network, another can simultaneously handle a different section, similar to an assembly line in a factory.

### Quantization: Making Models More Efficient

Quantization is like compressing a high-resolution image into a smaller file size while trying to maintain visual quality. Traditionally, model parameters are stored using 32-bit floating-point numbers (FP32). Through quantization, we can represent these numbers using 8-bit integers (INT8) or even less, significantly reducing memory usage and computational requirements. Here's a practical example: A model that originally required 20GB of GPU memory might only need 5GB after quantization. This could be the difference between needing expensive GPU instances and being able to run your application on more affordable hardware. While there might be a slight decrease in accuracy, the trade-off is often worth it for many real-world applications.

### Speculative Decoding: The Power of Prediction

Speculative decoding is like having an efficient assistant who makes educated guesses while a senior expert verifies them. The system uses a smaller, faster model to predict several tokens ahead while the main model validates these predictions.
For example, when generating the sentence "The capital of France is Paris," the smaller model might predict "Paris" immediately after "is," and if the main model agrees, we saved computation time. This technique can lead to 2-3x speed improvements in text generation.

### Putting it all together

When building a production generative AI application, these optimization techniques often work in concert. Consider a customer service AI assistant that needs to handle thousands of concurrent conversations:
The application might use a quantized model to reduce memory requirements, utilize KV-caching to speed up responses, and leverage model parallelism to handle the large model size. For particularly heavy traffic periods, speculative decoding could help maintain quick response times even under load. Using Amazon Bedrock, you can experiment with these optimizations without managing the underlying infrastructure. For instance, you could deploy different model configurations and compare their performance in terms of latency and resource usage.

## Further Reading

* Topic 3.4.2: Model inference optimization

## Contributors

**Authors:**
 - Guillermo Tantachuco - Principal AI Technologist 
 - Markus Bestehorn - Tech Lead Generative AI EMEA 

**Primary Reviewer:** Dmitry Soldatkin - Sr. ML Specialist SA 

**Additional Reviewers:**

- Tonny Ouma - Sr. Applied AI Architect 
