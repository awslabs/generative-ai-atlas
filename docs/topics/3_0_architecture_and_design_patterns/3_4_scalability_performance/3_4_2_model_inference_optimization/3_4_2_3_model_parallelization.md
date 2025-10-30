<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Model Parallelization

**Content Level: 300**


## TL;DR

As large language models continue to grow in size and complexity, the computational resources required for inference often exceed the capabilities of single accelerators. Model parallelism distributes model execution across multiple devices, allowing organizations to serve large models with acceptable latency and throughput.

This section explores practical approaches to model parallelization with a focus on AWS deployment options, focusing primarily on the most widely-used tensor and pipeline parallelism strategies.

<div style="margin:auto;text-align:center;width:100%;"><img src="../assets/images/model_parallelization_approaches.svg" alt="Model Parallelization Approaches"/></div>

*Figure 1: Comparative overview of model parallelization techniques for LLM inference*{: style="text-align: center; display: block"}

## Primary Parallelization Strategies

Tensor parallelism and pipeline parallelism are the two most widely used strategies for LLM inference. Which one you choose depends on your model architecture, hardware configuration, and latency requirements.

### Tensor Parallelism

Tensor parallelism distributes the weights of individual layers across multiple GPUs, with each device responsible for a portion of the computation within that layer.

**Key characteristics:**

- Model weights are split horizontally across devices
- Each GPU handles a slice of the matrix computations
- Results are synchronized across devices after computation
- Communication happens during each forward pass

**Advantages:**

- Minimizes memory requirements per GPU
- Works well for models with large hidden dimensions
- Generally offers lower latency than pipeline parallelism
- Ideal for real-time, latency-sensitive applications

**Challenges:**

- Requires high-bandwidth connections between GPUs (NVLink preferred)
- Communication overhead increases with the number of GPUs
- Implementation complexity increases with scale

Tensor parallelism performance depends on both intra-instance and inter-instance connectivity:

**Intra-instance connectivity (within a single instance):**

- NVLink provides high-bandwidth GPU-to-GPU communication within the same instance
- AWS instances like p4d.24xlarge, p5.48xlarge, and p5e.48xlarge offer NVLink for optimal tensor parallelism
- NVLink bandwidth enables efficient parameter sharing and gradient synchronization

**Inter-instance connectivity (across multiple instances):**

- EFA (Elastic Fabric Adapter) provides low-latency, high-throughput networking between instances
- Important for pipeline parallelism and distributed training across multiple nodes
- Supports RDMA for reduced CPU overhead and improved scaling efficiency

### Pipeline Parallelism

Pipeline parallelism segments the model vertically, assigning different layers to different accelerators and passing activations sequentially through the pipeline.

**Key characteristics:**

- Model is divided into sequential stages across GPUs
- Each GPU processes a complete portion of the model layers
- Activations flow from one stage to the next
- Multiple batches can be processed simultaneously at different stages

**Advantages:**

- Requires less communication bandwidth between GPUs
- Works well for very deep models
- Can utilize heterogeneous hardware effectively
- Less sensitive to inter-GPU bandwidth limitations

**Challenges:**

- Introduces pipeline bubbles (idle time) at the beginning and end
- May increase overall latency for single requests
- Requires careful balancing of computation across stages
- Benefits from EFA networking when stages span multiple instances

!!! warning "Pipeline Parallelism Consideration"
    Pipeline parallelism generally introduces higher latency for single requests compared to tensor parallelism. Consider this impact when designing latency-sensitive applications.

## Other Parallelization Strategies

### Sequence Parallelism

Sequence parallelism splits input sequences across devices, with each handling a portion of the tokens.
- Useful for models with extremely long context windows
- Complements tensor parallelism for long-sequence workloads
- Particularly valuable for document processing applications

### Mixture of Experts (MoE) Parallelism

In MoE architectures, specialized "expert" networks are distributed across devices:
- Only a subset of experts is activated for each token
- Reduces computation while maintaining model capacity
- Enables efficient scaling to very large model sizes

## AWS Deployment Options

AWS provides several options for deploying parallelized models:

The right AWS infrastructure depends on model size, parallelization strategy, and performance requirements. Start with SageMaker AI for the most straightforward deployment path.

### SageMaker AI

SageMaker AI offers fully-managed inference with built-in parallelism support:
- Simplified configuration through SageMaker AI SDK
- Pre-configured containers optimized for different model types
- Support for tensor and pipeline parallelism
- Automatic resource provisioning and scaling

### SageMaker HyperPod for Inference

Amazon SageMaker AI HyperPod now extends beyond training to provide comprehensive inference capabilities:

- **Unified Infrastructure**: Seamlessly transition compute resources between training and inference workloads to maximize GPU utilization
- **Flexible Deployment**: Deploy models using kubectl, Python SDK, SageMaker Studio UI, or HyperPod CLI
- **Enterprise-Ready**: Support for open-weights models, gated models from SageMaker JumpStart, and custom models from S3/FSx
- **Advanced Autoscaling**: Dynamic resource allocation with automatic demand-based adjustments
- **Comprehensive Observability**: Track time-to-first-token, latency, and GPU utilization metrics
- **Multi-Node Support**: Deploy single-node and multi-node inference architectures with EFA networking

### EC2 Instance Selection

The choice of EC2 instance type significantly impacts parallelization capability:

| Instance Type | GPUs | GPU Memory | Best Parallel Strategy |
|---------------|------|------------|------------------------|
| p5.48xlarge   | 8x H100 | 640GB | Tensor parallelism |
| p4d.24xlarge  | 8x A100 | 320GB | Tensor or pipeline parallelism |
| g5.48xlarge   | 8x A10G | 192GB | Pipeline parallelism |

**AWS Instance Selection Guidelines:**

- **Tensor parallelism**: Prioritize instances with NVLink between GPUs (p4d.24xlarge, p5.48xlarge, p5e.48xlarge)
- **Pipeline parallelism**: Standard network connectivity is sufficient for intra-instance stages
- **Multi-instance deployments**: Use EFA-enabled instances (p4d, p5, p5e series) for optimized inter-instance communication with RDMA support
- **Hybrid strategies**: Combine NVLink for local tensor parallelism with EFA for distributed pipeline stages

### Other Multi-Instance Options

For extremely large models exceeding single-instance capabilities:

- **AWS ParallelCluster**: Customizable multi-node clusters with EFA (Elastic Fabric Adapter) for high-performance networking
- **EFA Benefits**: Up to 100 Gbps network performance, RDMA support, and microsecond-level latency for distributed workloads

## Frameworks for Implementation

Several frameworks simplify the implementation of model parallelism:

### vLLM

vLLM offers excellent support for tensor parallelism with these features:
- Efficient tensor parallelism implementation
- PagedAttention for memory management
- High-throughput continuous batching
- Simple API for configuration

### DeepSpeed Inference

DeepSpeed provides comprehensive support for both tensor and pipeline parallelism:
- Flexible configuration options
- Optimized performance on various hardware
- Support for hybrid parallelization strategies

### TensorRT-LLM

NVIDIA's TensorRT-LLM offers hardware-optimized implementation:
- Highly optimized for NVIDIA GPUs
- Support for both tensor and pipeline parallelism
- Integration with AWS SageMaker AI

## Implementation Guidelines

!!! example "Implementation Steps"
    1. **Benchmark different strategies** with your specific model
    2. **Start simple** with tensor parallelism for most use cases
    3. **Monitor communication overhead** between devices
    4. **Optimize batch sizes** for your parallelization strategy
    5. **Test with realistic workloads** before production deployment

Key considerations for successful implementation:

1. **Communication efficiency**: Minimize data transfer between devices
2. **Load balancing**: Ensure even distribution of computation
3. **Hardware topology**: Align parallelization with physical hardware connections
4. **Batch size optimization**: Find optimal batch sizes for your strategy
5. **Memory management**: Balance memory usage across devices

## Conclusion

Model parallelization, particularly tensor and pipeline strategies, enables deployment of large models that exceed single-device memory capacity. AWS provides robust infrastructure and services for implementing these techniques, from GPU-optimized EC2 instances to managed SageMaker AI deployments.

For most LLM deployments, tensor parallelism offers the best balance of performance and implementation simplicity, especially on AWS instances with NVLink connectivity. Pipeline parallelism provides an alternative approach that's less dependent on high-bandwidth connections but may introduce additional latency.

By applying these parallelization strategies appropriately, you can deploy even very large models efficiently while maintaining acceptable performance characteristics.

## Further Reading

- [AWS Documentation: SageMaker AI Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html){:target="_blank" rel="noopener noreferrer"}
- [Deploying models on Amazon SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment.html){:target="_blank" rel="noopener noreferrer"}
- [DeepSpeed-Inference: Parallelization Strategies](https://www.deepspeed.ai/inference/){:target="_blank" rel="noopener noreferrer"}
- [vLLM: Distributed Inference and Serving](https://docs.vllm.ai/en/latest/serving/distributed_serving.html){:target="_blank" rel="noopener noreferrer"}
- [NVIDIA TensorRT-LLM: Multi-GPU Inference](https://developer.nvidia.com/tensorrt){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 
