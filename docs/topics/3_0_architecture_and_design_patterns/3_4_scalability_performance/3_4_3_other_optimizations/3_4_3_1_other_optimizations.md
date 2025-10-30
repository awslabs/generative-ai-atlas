<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Other Optimizations

**Content Level: 300**


## TL;DR

While model selection, quantization, parallelization, and distillation form the foundation of inference optimization, additional techniques can significantly enhance the performance, responsiveness, and scalability of generative AI systems. These complementary strategies address different aspects of the inference pipeline, from perceived latency to resource utilization and throughput maximization.

<div style="margin:auto;text-align:center;width:100%;"><img src="../assets/images/other_optimizations_overview.svg" alt="Other Optimization Techniques"/></div>

*Figure 1: Complementary optimization techniques for generative AI inference*{: style="text-align: center; display: block"}

## Streaming Response Optimization

Response streaming represents perhaps the most immediately impactful optimization available for LLM applications. By delivering tokens incrementally as the model generates them, streaming transforms the user experience from "wait and receive" to "watch and follow," dramatically improving perceived responsiveness and user satisfaction.


SageMaker AI Inference Endpoints also support streaming via both WebSockets and Server-Sent Events (SSE), with automatic integration for vLLM, TGI, and other popular inference backends.

### Streaming Performance Impact


## Amazon Bedrock Prompt Caching

One of the most significant developments for optimizing generative AI inference is Amazon Bedrock's Prompt Caching feature. This capability addresses an important performance bottleneck by eliminating redundant computation for commonly used prompt prefixes.

### How Prompt Caching Works

Prompt caching works by preserving the internal model state representing your prompt prefixes. When subsequent requests use the same prefix, the model can skip recomputation, delivering several key benefits:

1. **Latency Reduction**: By avoiding recalculation of already processed prefixes, response times can be significantly reduced.

2. **Cost Savings**: Since fewer tokens need to be processed, prompt caching can substantially reduce costs for supported models.

3. **Cache Persistence**: Cached prompts remain available for several minutes after each access, making this especially valuable for interactive applications.

**Ideal Use Cases:**

- **Document Q&A**: When users ask multiple questions about the same document
- **Code Assistants**: Where context about specific code files remains constant
- **Agentic Search**: Where system prompts and agent instructions are reused
- **Long-form Chat**: Where conversation context includes substantial unchanging elements

### Integration with Other Features

Prompt caching is designed to work seamlessly with other Amazon Bedrock features, including:

- **AgentCore Runtime**: Accelerating multi-step agent tasks by caching agent instructions and system prompts across long-running workloads
- **Intelligent Prompt Routing**: Combining routing between model sizes with caching for optimal performance and cost
- **Knowledge Bases**: Enhancing retrieval-augmented generation by caching common retrieval contexts

## Concurrency and Continuous Batching

!!! warning "Important for Throughput"
    Processing multiple requests simultaneously is important for cost-effective LLM deployments. Modern batching techniques significantly outperform sequential processing approaches.

### Continuous Batching

Continuous batching has become the standard approach for high-throughput LLM serving:

1. **Dynamic Micro-Batching**: Requests are grouped into micro-batches with similar characteristics (prompt length, expected output size) to optimize processing efficiency.

2. **Instruction-Level Interleaving**: Advanced schedulers interleave operations from different requests at the instruction level, maximizing hardware utilization.

3. **Prompt-Aware Scheduling**: Requests with similar prompts are intelligently grouped to leverage KV-cache reuse, dramatically improving throughput.

4. **Attention-Based Preemption**: Long-running generations can be temporarily paused to allow shorter, higher-priority requests to complete quickly.

### Inference Server Performance Comparison

Different inference server implementations offer varying performance characteristics, with vLLM establishing itself as a leader in throughput optimization, particularly for scenarios requiring high concurrency:

| Inference Server | Key Strength |
|------------------|--------------|
| vLLM             | PagedAttention and continuous batching |
| TGI              | Ease of deployment and configuration |
| TensorRT-LLM     | Hardware-specific optimizations |
| Triton Inference | Multi-framework support |

vLLM's performance comes from its advanced implementation of:

- PagedAttention for memory efficiency
- Block-based Key-Value cache management
- Prefix-aware request scheduling
- Attention operation optimizations

## Integrated Optimization Strategies

In production environments, these techniques are typically combined into cohesive optimization strategies tailored to specific workload characteristics.

### Real-Time Conversation Systems

For applications like customer service chatbots requiring quick responses:

1. **Streaming + Prompt Caching**: Immediately stream responses while leveraging cached prompts for consistent context.
2. **State Compression + Model Selection**: Use compressed context with smaller, faster models for most interactions.
3. **Fallback Architecture**: Employ automatic escalation to larger models only when necessary.

### High-Volume Document Processing

For applications processing large volumes of documents:

1. **Continuous Batching + Parallelization**: Maximize throughput with optimal batch sizes across multiple accelerators.
2. **Pipeline Parallelism**: Split tasks across specialized models optimized for different stages.
3. **Quantization + Specialized Hardware**: Deploy INT8 or mixed precision models on purpose-built inference accelerators.

## Conclusion

While model-focused optimizations form the foundation of efficient LLM inference, these complementary techniques—streaming, prompt caching, continuous batching, and state management—have become equally important in production environments. By thoughtfully combining these approaches and tailoring them to specific workload characteristics, organizations can dramatically improve performance while controlling costs.

!!! tip "Strategic Implementation"
    Start with streaming for immediate user experience improvements, then implement prompt caching for frequently used contexts, and finally optimize batch processing for maximum throughput.

The Amazon Bedrock Prompt Caching capability represents a particularly significant advancement, promising substantial improvements in both performance and cost-efficiency for a wide range of generative AI applications. As models continue to grow in size and capability, these optimizations will remain important for translating theoretical advances into practical, responsive, and cost-effective generative AI systems.

## Further Reading

- [Stream Amazon Bedrock responses for a more responsive UI](https://community.aws/content/2gYtxK2HNy3bg4z68HJ1FM0OOuK/stream-amazon-bedrock-responses-for-a-more-responsive-ui){:target="_blank" rel="noopener noreferrer"}
- [Amazon Bedrock Intelligent Prompt Routing and Prompt Caching](https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/){:target="_blank" rel="noopener noreferrer"}
- [Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html){:target="_blank" rel="noopener noreferrer"}
- [vLLM: High-Throughput and Memory-Efficient LLM Serving](https://vllm.ai/){:target="_blank" rel="noopener noreferrer"}
- [AWS Neuron: Deep Learning on AWS Inferentia and Trainium](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 