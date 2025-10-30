<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Runtime Environment Scalability

**Content Level: 300**


## Suggested Pre-Reading

- [Application Performance Monitoring](../3_4_1_1_application_performance/3_4_1_1_2_application_performance_monitoring.md)

## TL;DR

Generative AI workloads have unique infrastructure needs due to large model sizes, limited concurrency, and cold-start latency. This section outlines how to build scalable runtime environments using AWS-native services such as Amazon Bedrock (On-Demand and Provisioned Throughput) and SageMaker AI Hosting. Key design principles include horizontal scaling for concurrency, vertical scaling for large model support, warm pool provisioning to address cold-starts, and quota management for optimal performance. AWS services like CloudWatch and Application Auto Scaling help manage these patterns effectively.

## Runtime Environment Scalability for GenAI Applications

Unlike traditional microservices, GenAI systems place intensive demands on compute, memory, and infrastructure-level readiness. A runtime environment should:

- Support low-latency, high-throughput LLM inference,
- Scale horizontally to handle concurrent requests,
- Scale vertically to host memory-heavy models,
- Minimize cold-start delays for responsiveness,
- Manage long-lived state or sessions for agent-like workloads.

AWS offers managed services and autoscaling features to support these requirements out of the box.

## Key Runtime Services on AWS

### Amazon Bedrock (On-Demand and Provisioned Throughput)

- **On-Demand Bedrock** endpoints scale automatically within defined RPM/TPM quotas. For most development or variable-traffic production workloads, on-demand is sufficient.
- **Provisioned Throughput** allows you to reserve fixed model capacity (Model Units) for predictable, low-latency performance. Recommended for consistent, high-throughput use cases and custom model variants.
- **Inference Profiles** provide advanced throughput and cost management capabilities, including cross-region routing for increased throughput and fault tolerance.

Monitor Bedrock metrics like `InvocationLatency`, `InvocationThrottles`, and `Input/OutputTokenCount` to identify scaling needs or quota limits. For comprehensive monitoring setup, see [Monitoring Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html){:target="_blank" rel="noopener noreferrer"}.

### Amazon SageMaker AI Hosting

- Ideal for fine-tuned or proprietary models.
- Real-time inference endpoints support GPU-backed instances, vertical scaling, and Application Auto Scaling.
- **ConcurrentRequestsPerModel** enables fast, concurrency-driven scaling for latency-sensitive workloads.
- Always keep at least one instance warm to prevent cold-start delays.

## Best Practices for Scaling GenAI Infrastructure

### 1. Horizontal vs Vertical Scaling

- **Vertical Scaling:** Use larger instances or multi-GPU nodes (e.g. ml.p5e.48xlarge with 8 H200 GPUs, ml.p6e with Blackwell GPUs) for large models.
- **Horizontal Scaling:** Add model replicas (instances) to support higher concurrency. Works well with stateless inference APIs (Bedrock, SageMaker AI RT endpoints).

### 2. Mitigating Cold Starts

- Use Bedrock Provisioned Throughput or SageMaker AI min-capacity to maintain warm instances.
- Preload models and send warm-up inference calls on deployment.
- Monitor model loading time via logs or metrics (e.g. `ModelLoadingWaitTime`).

### 3. Session Management

- Configure appropriate session timeouts for conversation-based applications.
- Implement efficient memory management for multi-turn interactions.
- Monitor session state lifecycle and cleanup patterns.

### 4. Scaling Triggers

- Bedrock auto-scales internally; manage via quota and monitor `InvocationThrottles`.
- SageMaker AI: Use `ConcurrentRequestsPerModel` with Application Auto Scaling.
- Watch p95 latency and queue time to refine scaling thresholds.

### 5. Monitoring and Alerts

- Create CloudWatch dashboards for `InvocationCount`, `Latency`, `TokenUsage`, and `Throttles`.
- Use CloudWatch Alarms to trigger actions (alerts, StepFunctions, Lambda invocations).
- Log invocations to S3/CloudWatch Logs for diagnostics.

**Implementation Guidelines:**

- Don't assume every LLM model is auto-scalable: provisioning matters
- Quota limits (e.g. RPM/TPM in Bedrock) can silently throttle traffic under high load
- Use load testing (e.g. ML Inference Load Testing Toolkit) to simulate peak RPS

## Next Steps

- If using Bedrock on-demand and seeing high latency or throttles → explore Provisioned Throughput.
- If using SageMaker AI and experiencing latency under load → configure autoscaling with concurrency metrics.
- For conversation-based applications → ensure session management aligns with user interaction patterns.

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 
