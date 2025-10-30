<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Inference in Generative AI
Inference is the process by which trained generative AI models produce outputs based on input prompts, representing the critical bridge between model development and real-world application. This section explores the different approaches to deploying and serving models in production, from real-time interactions to large-scale batch processing, providing essential knowledge for building scalable and efficient AI systems.

## Key Topics Covered

This section explores several crucial aspects of inference in Generative AI, including:

 - **[Online Inference](2_3_5-1_online_inference/online_inference.md)**: Learn how to enable real-time interactions between users and AI models, including prompt processing, content generation, and response management for applications like chatbots and content generation tools.
 - **[Asynchronous Inference](2_3_5-2_async_inference/async_inference.md)**: Discover how to efficiently process large volumes of requests without blocking operations, ideal for batch processing tasks like document analysis, bulk content classification, and large-scale embedding generation.
 - **[Model Serving](2_3_5-3_model_serving/model_serving.md)**: Understand the infrastructure and processes needed to deploy LLMs to production, including deployment strategies using Amazon SageMaker AI, Amazon Bedrock, and Amazon EKS for different workload patterns and operational needs.

## Why It Matters

Understanding inference strategies is fundamental to building production-ready generative AI applications that balance performance, cost, and user experience. Whether you're developing interactive chatbots requiring sub-second response times or processing millions of documents for analysis, choosing the right inference approach directly impacts your application's success and scalability.

By the end of this section, you will:

- Understand the trade-offs between online and asynchronous inference patterns and when to apply each approach
- Master optimization techniques like KV-caching, quantization, and speculative decoding to improve model performance
- Know how to choose between Amazon SageMaker AI, Amazon Bedrock, and Amazon EKS for different deployment scenarios
- Be able to design scalable inference architectures that balance latency, throughput, and cost considerations
- Implement practical solutions for common inference challenges in production environments

These topics build progressively from understanding real-time inference fundamentals to implementing complex deployment strategies, providing you with a comprehensive toolkit for delivering AI capabilities at scale.

**Prerequisites**: Familiarity with [Key Primitives](../../2_1_key_primitives/index.md) and [Responses: Understanding Model Outputs](../../2_1_key_primitives/2_1_2_model_outputs/2_1_2_model_outputs.md) will help you get the most from this section.