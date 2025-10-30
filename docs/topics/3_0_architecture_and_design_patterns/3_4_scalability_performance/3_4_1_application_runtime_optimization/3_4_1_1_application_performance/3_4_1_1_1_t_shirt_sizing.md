<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# T-Shirt Sizing for Generative AI Workloads on AWS

**Content Level: 300**


## TL;DR

Successful GenAI deployment requires accurate capacity planning based on expected request volume, concurrency, and latency requirements. Both Amazon Bedrock and SageMaker can handle workloads from small prototypes to global-scale applications. The key is accurately forecasting your requirements and choosing the right service configuration. Start with Bedrock On-Demand for most cases, then scale to Provisioned Throughput or SageMaker as requirements grow.

---

## Capacity Planning Framework

<div style="margin:auto;text-align:center;width:100%;"><img src="../../assets/images/genai_tshirt_sizing_architecture.svg" alt="T-Shirt Sizing for GenAI Workloads"/></div>

*Figure 1: Example of T-Shirt Sizing Framework for AWS GenAI Workloads*{: style="text-align: center; display: block"}

Effective GenAI scaling depends on understanding your workload characteristics: request volume, concurrency patterns, and latency requirements. Both Amazon Bedrock and SageMaker AI scale to meet diverse needs—from prototype to global production.

---

## Service Selection

**Amazon Bedrock** handles infrastructure automatically—consider starting here for most workloads:

- **On-Demand**: Pay-per-token, scales globally, handles variable traffic
- **Provisioned Throughput**: Reserved capacity for high-volume or latency-sensitive apps

**Amazon SageMaker AI** provides infrastructure control for custom models and specialized requirements:

- Custom model deployment (open-source, proprietary)
- Fine-grained resource control and cost optimization
- Advanced scaling with Training Plans (up to 8 weeks reservations)

**Key Considerations:**

- Bedrock has default TPM and RPM quota. (e.g. Claude Sonnet 4 cross-region limits: 200 requests/min, 200K tokens/min)
- Both services scale from prototype to global production

For Bedrock quota increases, see [Bedrock service quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock){:target="_blank" rel="noopener noreferrer"} and [Token quota management](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas-token-burndown.html){:target="_blank" rel="noopener noreferrer"}.


---

## Implementation Strategy

**Phase 1: Start Small**

- Begin with Bedrock On-Demand for initial deployment
- Monitor CloudWatch metrics: `InputTokenCount`, `OutputTokenCount`, `InvocationLatency`
- Use cross-region inference for burst traffic management
- Implement cost attribution through tagging

**Phase 2: Scale Up**

- Bedrock for large volume of traffic
- SageMaker AI for custom models or specialized requirements
- Consider Training Plans for advance GPU reservations
- Multi-region deployment for high-availability applications
- Bedrock Provisioned Throughput when consistently using millions of tokens/hour


**Phase 3: Optimize**

- Implement prompt caching and request batching
- Use model cascading (fast models → premium models)
- Monitor and adjust based on actual usage patterns
- Leverage auto-scaling and cost optimization features

---

## Further Reading

- [Amazon Bedrock Quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock){:target="_blank" rel="noopener noreferrer"}
- [Choosing Between On-Demand and Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html){:target="_blank" rel="noopener noreferrer"}
- [SageMaker Training Plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html){:target="_blank" rel="noopener noreferrer"}
- [SageMaker Hosting for Large Language Models](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 
