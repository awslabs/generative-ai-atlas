<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Model Quantization

**Content Level: 300**


## TL;DR

Model quantization has emerged as one of the most effective techniques for optimizing inference performance of large language models. By reducing the numerical precision used to represent model weights and activations, quantization significantly decreases memory requirements, increases throughput, and reduces costs—often with minimal impact on output quality.

This guide explores practical quantization approaches for AWS deployments, focusing on implementation methods and best practices for efficient model serving.

<div style="margin:auto;text-align:center;width:100%;"><img src="../assets/images/model_quantization_overview.svg" alt="Model Quantization Overview"/></div>

*Figure 1: Model Quantization Precision Levels and Their Impact on Performance and Quality*{: style="text-align: center; display: block"}

## Quantization Fundamentals

Quantization lowers memory requirements by storing model weights in lower precision formats while preserving accuracy. Traditional full-precision (FP32) formats can be reduced to half-precision (FP16, BF16) or even integer formats (INT8, INT4), each offering different tradeoffs between performance and quality.

**Key Benefits:**

- **Reduced Memory Usage**: 50-87.5% memory reduction depending on precision level
- **Higher Throughput**: Process more requests with the same hardware
- **Lower Latency**: Faster response times for better user experience
- **Cost Efficiency**: Serve models on less expensive hardware
- **Wider Deployment Options**: Enable running on resource-constrained environments

## When to Apply Quantization

Quantization delivers the most value in these scenarios:

- **High-volume inference services** where GPU memory directly impacts costs
- **Latency-sensitive applications** requiring fast response times
- **Resource-constrained environments** with limited compute power
- **Multi-model deployments** where multiple models share hardware
- **Edge or local deployment** without access to cloud resources

## Common Quantization Formats

AWS supports multiple quantization precision levels, each with different tradeoffs:

- **FP16/BF16 (16-bit)**: 50% memory reduction with negligible quality impact
- **INT8 (8-bit)**: 75% memory reduction with minor quality impact
- **INT4 (4-bit)**: 87.5% memory reduction with moderate quality impact

Modern quantization techniques like GPTQ, AWQ, and SmoothQuant significantly reduce quality degradation compared to naive approaches, making even 4-bit precision viable for many production applications.

## Quantization Approaches on AWS

AWS offers several implementation paths for quantized models:

### 1. Amazon SageMaker AI

SageMaker AI provides the most integrated experience for quantized model deployment:

- **Built-in quantization support** for INT4 (AWQ), INT8 (SmoothQuant), and FP8
- **Optimized containers** with TensorRT-LLM and other acceleration libraries
- **Pre-quantized models** available through SageMaker AI JumpStart
- **Fast model loading** with optimized S3 streaming

For most enterprise deployments, SageMaker AI offers the simplest path to production with quantized models.

### 2. AWS Inferentia with Neuron SDK

For cost-optimized inference at scale:

- **INT8 quantization** optimized specifically for Inferentia hardware
- **Automatic optimizations** applied during model compilation
- **Significantly lower cost** compared to GPU-based inference
- **Simple integration** with existing Hugging Face and PyTorch models

Inferentia particularly shines for stable production workloads where cost efficiency is a priority.

### 3. Custom Deployment Options

For specialized needs or maximum flexibility:

- **vLLM**: High-performance serving with AWQ and GPTQ support
- **GGUF format**: Broad hardware compatibility with 2-8 bit quantization
- **TensorRT-LLM**: Maximum GPU performance with SmoothQuant and FP8

## Practical Implementation Guide

Follow these steps to implement quantization for your AWS deployments:

### 1. Select the Right Quantization Technique

Different model architectures respond differently to quantization:

- **Decoder-only models**: GPTQ and AWQ work exceptionally well
- **Encoder-decoder models** (T5): SmoothQuant and INT8 typically perform better
- **Multi-modal models**: Often require more careful quantization approach

Begin with higher precision (INT8) and evaluate before moving to more aggressive quantization (INT4). The quality impact varies significantly across models and tasks.

### 2. Choose Your Implementation Path

| If you want... | Choose |
|----------------|--------|
| Simplest deployment with minimal custom code | SageMaker AI with pre-quantized models |
| Maximum cost efficiency for stable workloads | AWS Inferentia with Neuron SDK |
| Highest flexibility and customization | Custom containers with vLLM or TensorRT-LLM |
| Local testing or edge deployment | GGUF format with compatible runtime |

### 3. Validate Performance and Quality

Always evaluate both performance improvements and quality impacts:

- **Throughput**: Measure requests/second and tokens/second
- **Latency**: Track Time to First Token (TTFT) and total generation time
- **Memory Usage**: Confirm actual memory reduction matches expectations
- **Output Quality**: Compare against full-precision model on representative tasks

!!! warning "Quality Monitoring"
    Implement ongoing quality monitoring for quantized models in production. Some edge cases may show more significant quality degradation than average performance suggests.

## Real-World Implementation Patterns

### Multi-Tiered Model Architecture

Many production systems implement a tiered approach:

- **Fast tier**: Smaller models (7B) with INT4 quantization handle common queries
- **Quality tier**: Larger models (70B+) with INT8 quantization process complex requests
- **Routing logic**: Simple classifier determines which model handles each request

This approach balances performance and quality while optimizing infrastructure costs.

### Edge and Low-Resource Deployment

For environments with limited resources:

- Use GGUF quantization with compatible runtime
- Select precision based on available hardware (q4_K for most cases, q8_0 where quality is important)
- Implement efficient context management to maximize performance

## Conclusion

Model quantization has become an important technique for deploying large language models efficiently. By selecting the right quantization approach and implementation path on AWS, organizations can dramatically reduce infrastructure costs while maintaining response quality and meeting latency requirements.

For most AWS deployments, we recommend:

1. Start with SageMaker AI and pre-quantized models for the fastest path to production
2. Evaluate INT8 quantization before moving to more aggressive INT4 techniques
3. Consider AWS Inferentia for stable, cost-sensitive production workloads
4. Implement continuous quality monitoring alongside performance metrics

As models continue to grow in size and capability, effective quantization strategies will remain important for building responsive, cost-effective AI applications.

## Further Reading

- [Amazon SageMaker AI Inference Optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-optimization-genai.html){:target="_blank" rel="noopener noreferrer"}
- [AWS Neuron SDK Quantization Guide](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/appnotes/quantization.html){:target="_blank" rel="noopener noreferrer"}
- [Optimizing Generative AI LLM Inference Deployment on AWS GPUs By Leveraging Quantization with llama.cpp](https://github.com/aws-samples/optimizing-llm-inference-with-quantization){:target="_blank" rel="noopener noreferrer"}
- [Introduction to llama.cpp and GGUF Format](https://github.com/ggerganov/llama.cpp){:target="_blank" rel="noopener noreferrer"}
- [HuggingFace Transformers Qunatization](https://huggingface.co/docs/transformers/v4.51.1/quantization/overview){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 
