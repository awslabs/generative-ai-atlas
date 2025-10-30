<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Application Performance Monitoring for Generative AI

**Content Level: 300**


## TL;DR

Monitoring generative AI applications requires deeper visibility than traditional application performance monitoring (APM) due to the complex nature of LLM workflows, prompt/response variability, and high compute costs. To operate LLM-based systems reliably in production, teams should track token-level latency metrics (like Time to First Token), invocation-level statistics (such as error types and throughput), and agent-level observability (especially for multi-step workflows powered by autonomous agents). AWS provides native observability tools through Amazon Bedrock, CloudWatch, and Lambda, while emerging services like Langfuse and OpenTelemetry integrations are becoming important for full-stack visibility.

## Introduction

LLM applications do not behave like traditional web services. Each request may involve token-heavy inputs, variable response lengths, external tool invocations, and non-deterministic reasoning steps. As a result, measuring overall latency is insufficient — engineers need to break down performance at the level of model invocations, agent workflows, and session interactions.

Bedrock, SageMaker AI, Amazon Bedrock AgentCore, and frameworks such as [Strands Agents](https://strandsagents.com/latest/){:target="_blank" rel="noopener noreferrer"} now support fine-grained observability through metrics, logs, and traces. This document outlines how to implement application performance monitoring for LLM systems using both AWS-native tooling and specialized observability services.

<div style="margin:auto;text-align:center;width:100%;"><img src="../../assets/images/application_runtime_optimization_architecture.svg" alt="Application Performance Monitoring Architecture"/></div>

*Figure 1: Generative AI Application Performance Monitoring Architecture*{: style="text-align: center; display: block"}

---

## Monitoring Key Metrics in LLM Workloads

Modern LLM systems introduce metrics that go beyond traditional latency or error rate:

- **Time to First Token (TTFT)**: Measures how quickly the model starts responding after receiving a prompt. In streaming applications, this is key for user-perceived responsiveness.

- **Throughput (tokens/sec)**: Indicates how fast tokens are generated once output starts. Useful for sizing infrastructure and assessing performance differences across models.

- **Token Counts (Input/Output)**: Directly tied to cost in API-based models (e.g., Bedrock). Monitoring large token volumes helps identify cost anomalies or inefficient prompts.

- **Invocation Errors**: Breaks down into client errors (e.g., invalid input), server errors (e.g., model unavailable), and throttling. These are important for uptime and reliability monitoring.

- **Content Filtering Events**: Indicates when responses were blocked by moderation policies (especially in Bedrock).

Amazon Bedrock emits all of the above as CloudWatch metrics. For example, `InputTokenCount` and `InvocationLatency` are available per-model, allowing dashboards and alarms to be configured with minimal setup.

---

## Observability Patterns Using AWS Services

### 1. **CloudWatch Gen AI Observability**

Amazon Bedrock integrates with CloudWatch to automatically emit model invocation metrics and supports logging request/response payloads to CloudWatch Logs. CloudWatch now provides [Generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html){:target="_blank" rel="noopener noreferrer"} with pre-configured dashboards and end-to-end prompt tracing:

**Pre-built Dashboards:**

- **Model Invocations**: Detailed metrics on model usage, token consumption, and costs
- **Amazon Bedrock AgentCore Agents**: Performance and decision metrics for agents

**Key Capabilities:**

- End-to-end prompt tracing across knowledge bases, tools, and models
- Integration with popular frameworks (e.g. Strands Agents) and AgentCore
- Support for third-party model traces via ADOT SDK
- Cost attribution by application, user role, or specific user

With minimal setup, you can:

- Visualize latency trends (p50, p90, p99) across models
- Compare token usage by model version or feature
- Alert on spikes in `InvocationServerErrors` or `ContentFilteredCount`
- Inspect full prompts and responses using Logs Insights queries

**Example Use Case**:

> Detecting prompt-induced latency regressions by tracking increases in average `InputTokenCount` and `InvocationLatency` for a specific model. Alerts configured via CloudWatch notify the Ops team when thresholds are exceeded.

### 2. **CloudWatch Dashboards for LLM Monitoring**

Combining metrics and logs into unified CloudWatch dashboards helps correlate usage spikes with specific prompt patterns or model configurations. For example:

- Invocation Count by Model ID
- p95 Latency vs. Output Token Volume
- Recent Prompts from Logs Table
- Alarm Status for Key Error Types

### 3. **Logging and Search with CloudWatch Logs Insights**

CloudWatch Logs Insights enables real-time and historical queries over Bedrock invocation logs. Teams can:

- e.g. Filter requests with large token counts (`InputTokenCount > 1000`)
- e.g. Identify slow responses (`InvocationLatency > 5000`)
- Analyze failure trends by error type or content filter triggers

Enable logging via Bedrock settings and structure logs with session metadata for easier tracing and troubleshooting during production incidents.

### 4. **Using CloudTrail for Audit Events**

While not performance-centric, CloudTrail records all Bedrock API calls — useful for compliance and auditing. Pair this with CloudWatch metrics for holistic monitoring.

---

## Agent-Level Observability with AgentCore, Strands, and LangGraph

Autonomous agents add complexity — LLMs plan actions, invoke tools, evaluate responses, and loop until goals are met. To debug and optimize these workflows:

### Amazon Bedrock AgentCore Observability

AgentCore provides comprehensive, built-in observability for agent workflows:

- **Real-time Dashboards**: Monitor agent behavior through intuitive CloudWatch-powered dashboards with comprehensive metrics
- **Session Tracking**: Complete visibility into agent workflows with session isolation and 8-hour long-running task support
- **OpenTelemetry Integration**: Seamless integration with existing monitoring systems via OpenTelemetry compatibility
- **Operational Metrics**: Track key performance indicators including token usage, latency, session duration, and error rates
- **Debugging Support**: Full audit trails of agent decisions and tool invocations for compliance and troubleshooting

**AgentCore + Strands Integration**:

Strands Agents can be deployed directly to AgentCore Runtime with enhanced observability. AgentCore automatically provides session isolation, CloudWatch metrics, and OpenTelemetry traces. For comprehensive monitoring, use ADOT (AWS Distro for OpenTelemetry) with strands-agents and bedrock-agentcore.

### Framework-Specific Observability

**Strands Agents Observability**:

The Strands Agents SDK provides comprehensive observability through native OpenTelemetry integration:

- **Automatic Instrumentation**: Built-in traces, metrics, and logs with zero configuration
- **Agent-Specific Metrics**: Token usage (input/output/total), cycle durations, tool performance
- **Rich Trace Data**: Complete agent execution flow including model invocations and tool calls
- **Multi-Service Support**: Export to CloudWatch Gen AI Observability, AWS X-Ray, and other OTLP-compatible systems (e.g. LangFuse)

**Custom Framework Observability**:

For frameworks beyond Strands and AgentCore:

- **Custom Graph Frameworks (e.g. LangGraph)**: Structure agent logic as directed graphs. Combined with trace visualization tools, developers can see branching logic, action results, and detect failure loops
- **Custom Implementations**: Enable `returnControlInvocationResults` to get detailed trace events per agent invocation (tool calls, decisions, etc.)
- Extract and log session state attributes (context variables, memory slots)
- Map reasoning steps as traceable spans or events (future X-Ray integration hinted by AWS engineers)

Langfuse offers a node-edge view of agent behavior — from input to action invocation to LLM decision — and aggregates metrics like average session cost, TTFT per node, etc.

---

## OpenTelemetry and Distributed Tracing

OpenTelemetry (OTEL) adoption is growing in GenAI workflows. Frameworks like Strands Agents provide native OTEL support, while various tracing services provide observability for agent workflows. You can:

- Wrap LLM invocations in spans with prompt metadata
- Export traces to any compatible APM backend (Datadog, Jaeger, etc.)
- Correlate LLM invocations with backend services (e.g., vector DB, API calls)

This enables unified visibility across microservice applications that include AI components.

---

## Combining Native and External Observability Services

| Service     | Capabilities                                                                 |
|--------------|------------------------------------------------------------------------------|
| **CloudWatch** | GenAI observability, pre-built dashboards, end-to-end prompt tracing, metrics (token, latency, errors), logs, alarms |
| **Langfuse**   | Full-context traces, agent graph views, prompt/version analytics            |
| **LangSmith**  | Tracing for LangChain chains/agents, prompt evaluation, performance monitoring |
| **Helicone**   | API-level proxy that logs LLM calls and costs, with minimal integration     |

---

## Recommendations for Production Systems

1. **Enable Bedrock Invocation Logs**: Capture prompt/input/output/token details for every request.
2. **Set Token-Level Alarms**: Use `InputTokenCount`, `OutputTokenCount`, and `InvocationLatency` with CloudWatch alarms.
3. **Leverage AgentCore Observability**: For agent-based applications, utilize built-in AgentCore dashboards and OpenTelemetry integration for comprehensive monitoring.
4. **Trace Agent Workflows**: Use available tracing services or custom OTEL spans to capture agent reasoning steps for non-AgentCore deployments.
5. **Monitor Cost & Latency**: Dashboards showing token usage per model/user/feature help optimize prompts and route traffic.
6. **Track Errors by Source**: Log and trace both LLM-side and tool-side failures for agent tasks.
7. **Log Session Context**: In agent systems, record session attributes and state transitions with AgentCore's session isolation features.

---

## Further Reading

- [CloudWatch Generative AI Observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html){:target="_blank" rel="noopener noreferrer"}
- [Monitoring metrics and logs for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html){:target="_blank" rel="noopener noreferrer"}
- [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html){:target="_blank" rel="noopener noreferrer"}
- [Strands Agents Observability](https://strandsagents.com/latest/documentation/docs/user-guide/observability-evaluation/observability/){:target="_blank" rel="noopener noreferrer"}
- [Langfuse: Observability for LLM Apps](https://www.langfuse.com/){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Sanghwa Na - Specialist SA, Gen AI 
