<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Deploying generative AI applications 

**Content Level: 200**

## Suggested Pre-Reading

* [Responsible AI Principles and Considerations](../../1_0_generative_ai_fundamentals/1_4_responsible_ai_principles_and_considerations/1_4_responsible_ai_principles_and_considerations_placeholder.md)
* [Managing Hallucinations and Guardrails](../../2_0_technical_foundations_and_patterns/2_5_managing_hallucinations_and_guardrails/hallucinations_and_guardrails.md)


## TL;DR

With AI Ops, deployment follows a structured validation path through development, pre-production, and production environments, with comprehensive testing at each stage. CI/CD pipelines automate testing and deployment processes for both infrastructure and models, while Infrastructure as Code (IaC) enables consistent, version-controlled deployments across environments.
Guardrails provide key safety mechanisms to help ensure AI systems operate within defined boundaries for security, ethics, and performance. Monitoring and observability are important for tracking system behavior, detecting issues, and enabling continuous improvement through feedback loops. Success requires maintaining safety without sacrificing system performance or user experience while optimizing costs and resource usage.

---


## CI/CD
***Applied AI Ops Principles: Versioning, Testing, Automation, Reproducibility, Reliability & Resiliency***

GenAI applications go through different validation phases and environment tiers (e.g. DEV/UAT/PROD). The number of environment tiers and validation phases is typically dependent on the complexity and criticality of the workload. Overall, these validation phases are similar to the best practices described in ML Ops and require automation for consistent, version-controlled, and automated deployment across environments.

### Pre Release
Similar to the benchmarking during the development cycle, use a validation dataset to evaluate changes to the LLM portion of your system as part of your CI/CD pipeline that's deploying changes to the environment. 
A drop in these metrics should block the pipeline from deploying.
As you uncover more issues and understand the way users expect to interact with your system, these datasets will change and be added to over time.

### Candidate Release in PreProd
For new candidate releases, shadow a subset of user traffic and capture relevant metrics. If the metrics improve, it provides confidence that the candidate release should move into production.
 
###Prod Release
Once shadowing is completed, you can begin A/B testing the solution which enables you to track user driven business metrics. And finally, if the A/B test was successful, you can be more confident that the candidate release should roll out to all traffic.
Versioning helps ensure you can roll back to a previous version if a new deployment has issues.

### Infrastructure as Code
Infrastructure as code (IaC) is important for consistent, version-controlled, and automated infrastructure and application deployments across environments. This practice streamlines deployment, reduces errors, and enhances team collaboration. When selecting your tool stack for AI Ops, consider your team's skills and project requirements. Tools such as AWS Cloud Development Kit (AWS CDK), AWS CloudFormation, or Terraform can help define and manage infrastructure resources required for your GenAI applications.
Ensure IaC templates can handle multiple environments such as development, testing and staging, and production to maintain consistency across environments by using the same templates with different parameters. Establish governance practices and controls to maintain compliance of your resources. Services such as AWS Config can help with tracking resource configurations.

### Automation
Implement CI/CD pipelines using services like AWS CodePipeline or similar tools to automate testing and deployment of application and infrastructure changes. Automation across training, tuning, validating, and deploying models, enables not only operational efficiency and reduces time-to-market, but it also establishes a reproducible and version-controlled generative AI application stack.

## Guardrails
***Applied AI Ops Principles: Security, Monitoring & Observability, Reliability & Resiliency, Reusability***

Guardrails are important for designing safe and reliable generative AI applications. Like any component in your ML pipeline, guardrails require monitoring, measurement, and maintenance to confirm they are functioning effectively without introducing performance issues. Think of guardrails as another key micro-service in your architecture - one that requires the same level of operational rigor as your core ML systems.


### Implementing Guardrails in AI Ops

Effective guardrail implementation requires integration throughout the Generative AI application lifecycle, beginning with the design phase and continuing through development, deployment, and ongoing monitoring.

**During the design phase**, organizations should conduct a thorough risk assessment to identify potential failure modes and their impacts. This involves analyzing use cases, user personas, data characteristics, and operational contexts to understand where and how AI systems might fail or be misused. Based on this assessment, organizations should design layered protection mechanisms appropriate to their use cases, typically involving multiple guardrail types working together to provide defense in depth.
Organizations should clearly articulate what the system should and should not do, including defining prohibited topics, acceptable response characteristics, and performance expectations, and ethical boundaries. These definitions should be specific, measurable, and aligned with organizational values and compliance requirements. Ensuring all stakeholders agree on guardrail requirements is key for successful implementation, including alignment across technical teams, business units, legal/compliance departments, and executive leadership.

**In the development phase**, guardrails are implemented and tested as part of the overall system. AWS provides SDKs for services like Amazon Bedrock Guardrails that can be integrated into application code to implement content filtering, topic detection, and other safety features. Building comprehensive tests for guardrail effectiveness helps ensure they function as expected, including positive testing (ensuring legitimate content passes) and negative testing (ensuring prohibited content is blocked).
Organizations should create clear documentation of all implemented guardrails supports maintenance and compliance efforts. Documentation should include guardrail purposes, configurations, expected behaviors, and testing results. Including guardrail implementation in code review processes helps to ensure quality and completeness, with reviews specifically evaluating whether guardrails are implemented correctly, cover all identified risks, and integrate properly with other system components.

***During deployment***, guardrails are activated and configured in production environments. Implementing progressive deployment with increasing guardrail relaxation allows for careful validation. Start with strict guardrails in limited environments and gradually relaxing constraints as confidence grows. Leverage a CI/CD system to support staged rollout strategies.
Establishing secure processes for managing guardrail settings prevents unauthorized changes. AWS Systems Manager Parameter Store or AWS Secrets Manager can be used to securely store and manage guardrail configurations. Verifying guardrail functionality in production-like environments helps to ensure they work as expected in the actual deployment context, including testing interactions with other production systems, performance under expected load, and behavior with real user patterns.

***Post deployment***, ongoing monitoring helps ensure guardrails remain effective. Collecting metrics on guardrail activations and effectiveness provides visibility into system behavior. Amazon CloudWatch can be configured to track metrics like guardrail trigger rates, false positive/negative rates, and performance impacts. Setting up notifications for guardrail breaches or failures enables rapid response to issues. Amazon EventBridge can be configured to trigger alerts and automated responses when guardrails detect problematic patterns or fail to function properly.

### Multi-Layer Guardrail Architecture

Effective guardrail systems implement protection at multiple layers, creating a defense-in-depth strategy.
 
At the ***application layer***, designing interfaces that naturally guide users toward appropriate interactions helps prevent problematic requests from being submitted. Implementing preliminary checks before requests reach the model can filter out obviously inappropriate content early in the process. Filtering and formatting model outputs before display provides an additional layer of protection against harmful content.

At the ***API layer***, enforcing schema and content requirements for all requests helps ensure that inputs meet basic safety and quality standards. Ensuring only authorized users access specific capabilities prevents misuse by unauthorized parties. Preventing abuse through excessive API usage protects system resources and availability. Routing requests to appropriate handling based on content and intent enables specialized processing for different request types.

At the ***model layer***, using system prompts to establish behavioral boundaries guides the model toward safe and appropriate responses. Setting appropriate temperature and other generation parameters controls the randomness and creativity of model outputs, which can affect safety. Implementing custom filters for known model weaknesses addresses specific vulnerabilities in particular models. Training models to inherently avoid problematic outputs provides a foundation of safety that other guardrails can build upon.

At the ***infrastructure layer***, containing models within appropriate security perimeters prevents unauthorized access or data leakage. Preventing resource exhaustion or denial of service helps ensure system availability and performance. Limiting model access to external resources or data prevents unauthorized data access or exfiltration. Securing data in transit and at rest protects sensitive information throughout the system.

### Monitoring Guardrail Performance

As guardrails are introduced for trust and safety, you should collect metrics such as the number of invocations and denied responses to help ensure that they working as intended. And given that these guardrails can introduce extra latency or new error modes, you should also capture metrics for those. 
Common metrics of interest are in the table below.

| Metric                        | Interpretation                                                                                   |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| Invocations                   | How often a specific guardrail or other capability is called                                     |
| Latency                       | The amount of time it takes to get a response from the guardrail or other capability             |
| Errors                        | Any errors reported by the guardrail or other capability                                         |
| Number of invocations per use | If a single user query requires multiple calls to different guardrails or capabilities, record how many such calls are made |
| Denied responses              | How many times an interaction fails because a guardrail denied the request or response           |


### Integration with Monitoring Systems

As the metrics to be collected are determined, they should be integrated with monitoring systems.
Managed services like Amazon Bedrock provide automatic metric reporting to CloudWatch, complete with built-in dashboards for guardrail performance, integration with CloudWatch Alarms, and custom metric creation capabilities. This native integration simplifies monitoring and management of guardrail systems.
Third-party solutions often include Prometheus metric export support, Grafana dashboard templates, custom monitoring integrations, and cross-platform metric aggregation capabilities, providing flexibility in monitoring approaches.
Distributed tracing implementation through AWS X-Ray enables request flow visualization, tracks guardrail impact on request paths, helps identify bottlenecks and optimization opportunities, and monitors inter-service dependencies for comprehensive system understanding.

### Best Practices and Operational Considerations

Alerting strategy should encompass automated alerts for unusual spikes in denied responses, latency exceeding thresholds, error rate increases, and resource utilization warnings. This proactive monitoring helps maintain the overall health of the AI application.
Performance optimization involves regular review of guardrail configurations, optimization of rule ordering, implementation of caching for frequently used checks, and comprehensive load testing with guardrails enabled.
Compliance and audit practices should maintain detailed logs of guardrail decisions, implement audit trails for policy changes, include regular reviews of guardrail effectiveness, and document false positive/negative rates for continuous improvement.
Continuous improvement requires regular review of denied responses, implementation of feedback loops for guardrail tuning, A/B testing of guardrail configurations, and ongoing performance impact analysis to optimize system effectiveness.
Resource planning encompasses capacity planning for guardrail processing, developing scaling strategies for high-load scenarios, implementing redundancy planning for important guardrails, and maintaining cost optimization strategies.
Keep in mind that while guardrails are important for safety, they shouldn't significantly impact your application's performance. Regular monitoring helps balance protection with user adoption and trust.

### Making it practical

When implementing guardrails as part of AI Ops, organizations have several practical paths depending on their specific needs and use cases.
They can either:

* self-host open-source frameworks, 
* implement guardrails as a separate, independent API service through services like Amazon Bedrock's Guardrails API, or
* leverage the build-in guardrail capabilities in services like Amazon Bedrock and Amazon SageMaker to further reduce implementation complexity.

Amazon Bedrock's native guardrails handle important functions like content filtering, topic restrictions, and PII detection without requiring custom development. Access control is managed through AWS Identity and Access Management (IAM) roles and resource policies, while Amazon CloudWatch and AWS CloudTrail handle the important task of logging guardrail activations and maintaining audit trails for compliance and troubleshooting.

Peak load and volume of requests are important factors to consider when deciding on a Guardrails implementation approach with the best price-performance.

Guardrails should be implemented as a defense-in-depth strategy, with multiple layers of protection working together. No single guardrail mechanism is foolproof, so combining approaches provides more robust protection against AI system failures or misuse.


## Monitoring and Observability
***Applied AI Ops Principles: Security, Monitoring & Observability, Reliability & Resiliency, Continuous Improvement, Cost & Resource Optimization***

Observability for generative AI involves monitoring and analyzing generative AI applications in production to understand, evaluate, and optimize their performance. It goes beyond traditional API or ML monitoring, requiring collection and analysis of logs, traces, and metrics at both infrastructure and application levels.

It helps developers track prompts, user feedback, latency, API usage, and retrieval performance. 
Monitoring tracks "what" is happening (API latency, request rates, GPU usage) via metrics and dashboards to ensure performance meets SLAs, while observability digs deeper into "why" issues occur by analyzing interconnected data (logs, traces) to trace individual requests, uncover root causes, and understand system behavior.

Put more simply, monitoring focuses on high-level metrics while observability enables granular investigation.


### Why Observability Is Important for Generative AI 

GenAI systems introduce new operational risks and complexities:

* **Hallucinations / opaque model behavior**: LLMs are non-deterministic with unpredictable outputs
* **Cost and resource sensitivity**: Token usage and computational costs can spike unexpectedly
* **Complex workflows**: Modern GenAI applications often use sophisticated patterns like RAG or agents
* **Semantic quality**: Traditional testing methods fail due to open-ended inputs
* **Performance demands**: Users expect low-latency responses despite computational complexity

Observability is important to monitor model performance, detect drift, and ensure accuracy and latency stay optimal. It enables debugging of unpredictable outputs by logging inputs and outputs for root-cause analysis while optimizing costs and API efficiency. It safeguards compliance by tracking harmful content and improves UX by refining prompts based on user feedback. Observability helps ensure your application's scalability by detecting failures and maintaining reliability in high-traffic deployments.

### Core Observability Signals

#### Logs

* Application logs (inputs, outputs, errors, warnings)
* Model-specific logs (prompt, response, token counts, cost)
* Infrastructure logs (system events, resource allocation, failures)

#### Traces

* End-to-end request flows
* Span metadata
* Context propagation across services

####  Metrics

* Request volume, latency, and error rates
* Token usage and cost per request/model
* Resource utilization (CPU, GPU, memory)
* Application-specific metrics


Effective observability requires collecting the above across key components, such as:

* LLMs – Core models (API-based or self-hosted).
* Vector Databases – Store & retrieve embeddings for retrieval-augmented generation (RAG).
* Chains / Agents – Workflows for processing inputs.
* User Interface – Endpoint for interactions.

Since LLMs are prompt-sensitive, robust monitoring of inputs/outputs is important and end to end tracking of these components is needed to help ensure reliability and a consistent user experience. 


### Observability Goals

* **Root Cause Analysis**: Rapidly diagnose unexpected or poor-quality outputs.
* **Bottleneck Identification**: Pinpoint latency or resource issues in API calls or retrieval steps.
* **Performance Drift Detection**: Identify changes in input distributions, concept drift, or degradation in model accuracy.
* **User Experience Optimization**: Track user satisfaction, session duration, return rates, and feedback to refine prompts and outputs.
* **Guardrails**: Detect and prevent harmful or inappropriate outputs.
* **Cost and Resource Management**: Monitor and optimize token usage, API costs, and infrastructure consumption.

These goals allow teams to proactively manage generative AI applications, without which you cannot assess or measure your application's real world impact.

### Methods and Best Practices

#### Prompts & User Feedback

Log prompts and collect feedback:

* Prompt Performance Tracking: Measures the success rate of different prompt templates
* Input Validation: Confirms prompts meet security and quality standards. Detect and flag toxic/inappropriate inputs (for example by using embedding distance checks from flagged content libraries).
* Response Quality: Monitors the relevance and accuracy of model outputs
* Drift detection identifies prompt drift, meaning deviations from baseline input distributions that signal changing user needs or adversarial queries. We further distinguish between different drift types:
    * Data Drift: Changes in input distributions
    * Concept Drift: Changes in the relationship between inputs and outputs (Prompt and responses stored in vector DB)
    * Performance Drift: Degradation in model performance (APM)
    * Usage Drift: Changes in how users interact with the system (monitoring token usage)
* User driven metrics indicate how successful users are in performing tasks within the system. If these metrics go down, that's generally an indicator that something is not working correctly. Some examples of user driven metrics include:
    * Session duration: How long users interact with the system.
    * Return rate: Frequency of users coming back to use the system.
    * Query volume: Number of queries processed over time.
* User satisfaction provides you with user experience trends, implicit vs explicit feedback, and Net Promoter Score (NPS) to better capture user sentiment.


#### Tracing

Track requests:

* Tracing tracks end-to-end user interactions in LLM applications by breaking them into granular "spans" representing each workflow step, like API calls or prompt assembly. These hierarchical spans reveal component connections and performance bottlenecks across the entire system. Tracing is especially valuable for complex, non-deterministic workflows like chains and agents where execution paths vary per request.
* Complete traces provide immediate visibility into system interactions and time allocation during request processing. This proves particularly important for chains and agents, where the request-dependent execution flow makes traces key for behavioral analysis.


#### Latency & Usage Monitoring

Measure API costs, token usage, and response times:

* Due to their size and complexity, LLMs can take a long time to generate a response. Managing and reducing latency is a key concern for LLM application developers.
* To optimize costs and reliability when using paid APIs, teams should track three key metrics: response times (latency), token consumption (for billing), and error patterns (to distinguish app errors from throttling or provider outages).
    * Latency metrics can be further broken down into:
        * Time to First Token (TTFT): The time it takes for the model to generate the first token after receiving a request. A shorter TTFT enhances the perceived responsiveness of the application.
        * Time Per Output Token (TPOT): The time taken to generate each subsequent token after the first one. Reducing TPOT can improve the overall generation speed.
        * Total Generation Time: The cumulative time required to generate the entire response.
    * Throughput: Requests processed per time unit. Metrics here are RPM and TPM.
    * Resource Usage: CPU, memory, and GPU utilization.
    * Cost: At application and request / token level. Monitoring token usage helps budget and control expenses by identifying heavy usage and potential optimization areas, such as by reducing response lengths or limiting unnecessary requests.
* For applications using managed services like Amazon Bedrock, utilize CloudWatch to monitor key metrics such as invocation counts, latency, token usage, error rates, and throttling events.

#### LLM Evaluations

* LLM applications lack clear success metrics since responses can vary while still being correct, making evaluation complex. Effective evaluation requires collecting representative prompt-output pairs that reflect real-world usage to accurately gauge performance.
* You can assess outputs via the following methods:
    * Structure validation (JSON parsing).
    * Reference comparisons (BLEU, ROUGE scores).
    * LLM-based evaluations (using another model).
    * Human evaluations (expensive but valuable).
* Since user intent can be ambiguous, supplementing evaluations with feedback and interaction patterns (like repeated rephrased queries) is necessary to see a complete picture of the interaction.

#### Retrieval Analysis

Check relevance of RAG-retrieved documents:

* LLMs can only replicate information they encountered in their training data or the prompt. With RAG systems, the user's input is used to retrieve additional information based on the prompt fed into the LLM.
* A RAG sub-system should be included in traces for tracking latency and cost to monitor the retrieval component of the application.



### Tools and Implementation

Modern observability for GenAI leverages both cloud-native (e.g., AWS CloudWatch, X-Ray) and specialized third-party tools (e.g., Arize Phoenix, LangSmith, Langfuse, Helicone, Confident AI, Galileo, Aporia, WhyLabs). OpenTelemetry (OTEL) is emerging as the standard for unified instrumentation across diverse environments.

| Tools                       | Observability Features                                                                                  |
|-----------------------------|---------------------------------------------------------------------------------------------------------|
| Arize Phoenix               | Open-source, tracing, LLM evaluations, RAG analysis                                                     |
| LangSmith                   | Prompt management, tracing, evaluations (LangChain integration)                                         |
| Langfuse                    | Open-source, prompt versioning, cost monitoring, human feedback                                         |
| Helicone                    | Cost tracking, prompt experiments, basic evaluations                                                    |
| Confident AI (DeepEval)     | Unit-test-like evaluations, feedback collection                                                         |
| Galileo                     | Enterprise-focused, LLM metrics, RAG analysis                                                          |
| Aporia                      | Guardrails for hallucinations, prompt injections                                                        |
| WhyLabs (LangKit)           | Open-source metrics for hallucinations, security                                                        |


Beyond LLMs, components such as vector databases and orchestration frameworks require developers to apply architectural patterns to this new tech stack. New tools, architectures, and vendors are introduced monthly. Current LLM observability solutions provide important capabilities for monitoring and improvement, but should continuously adapt to address emerging challenges in next-generation AI deployments like multi-modal processing and edge computing. LLM observability will continue to be necessary for ensuring LLM application flow and performance.  


## Feedback Loops
***Applied AI Ops Principles: Continuous Improvement, Cost & Resource Optimization***

Feedback loops allow for continuous improvement in GenAI deployments. They enable teams to systematically collect, analyze, and act on user interactions, model outputs, and operational signals, enabling GenAI systems to evolve to deliver higher quality, safer, and more relevant results over time. Unlike traditional ML systems, GenAI applications generate open-ended outputs that are highly sensitive to prompt phrasing, context, and user intent. This variability makes it important to implement robust feedback mechanisms that capture both explicit and implicit signals from real-world usage. Effective feedback loops help organizations:

* Detect and mitigate hallucinations, bias, and toxic outputs
* Adapt to changing user needs and business requirements
* Optimize prompt templates, retrieval strategies, and model selection
* Support compliance and responsible AI practices through traceability and auditability

### Core Patterns for Feedback Loops

To operationalize feedback loops in GenAI applications, consider the following actionable patterns:

#### User Feedback Collection

* Integrate explicit feedback channels directly into GenAI-powered applications (e.g. thumbs up/down, star ratings, comment boxes).
* Capture implicit signals such as user engagement, click-through rates, or abandonment, which can indicate satisfaction or frustration.
* Store feedback with rich context: prompt, response, user/session metadata, and model version for downstream analysis.

#### Automated Output Evaluation

* Use LLM-as-a-Judge or other automated evaluators to assess response quality, relevance, and safety at scale.
* Implement guardrails and classifiers to flag outputs for human review (e.g., toxicity, PII exposure, factuality checks).
* Leverage semantic similarity scoring to compare generated outputs against ground truth or reference answers.

#### Human-in-the-Loop (HITL) Review

* Establish workflows for human reviewers to audit flagged outputs, annotate errors, and provide corrective feedback.
* Use review outcomes to refine prompt templates, retrieval logic, or model parameters.
* Track reviewer agreement and escalate ambiguous cases for expert adjudication.

#### Closing the Loop: Incorporating Feedback

* Feed collected signals into prompt management systems, retrieval pipelines, or model fine-tuning workflows.
* Schedule regular retraining or prompt updates based on aggregated feedback trends.
* Prioritize feedback-driven improvements using business impact and risk assessments.

The most effective AI Ops implementations establish complete "observe-evaluate-improve" loops with clear ownership and automated workflows, typically reducing intervention time from weeks to hours when issues are detected.

## Getting Hands-On
* [Guardrails for Amazon Bedrock Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/0720c7c4-fb23-4e43-aa9f-036fc07f46b2/en-US){:target="_blank" rel="noopener noreferrer"} is a workshop where you'll explore how to leverage the power of Guardrails to implement customizable safeguards and responsible AI policies within your Amazon Bedrock applications.
* [Creating Responsible AI With Amazon Bedrock Guardrails](https://catalog.workshops.aws/bedrockguard/en-US){:target="_blank" rel="noopener noreferrer"} is a workshop provides hands-on experience implementing guardrails with Amazon Bedrock.
* [LLM Guardrails Implementation Patterns for AWS](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai){:target="_blank" rel="noopener noreferrer"} is a repository of code samples and patterns for implementing guardrails with AWS services.

## Further Reading
* [Compliance and assurance of AI systems](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/security-perspective-compliance-and-assurance-of-aiml-systems.html){:target="_blank" rel="noopener noreferrer"} 
* [Generative AI adoption and compliance](https://aws.amazon.com/blogs/security/generative-ai-adoption-and-compliance-simplifying-the-path-forward-with-aws-audit-manager/){:target="_blank" rel="noopener noreferrer"} 
* [Innovating with AI in Regulated Industries](https://aws.amazon.com/blogs/enterprise-strategy/innovating-with-ai-in-regulated-industries/){:target="_blank" rel="noopener noreferrer"}
* [AWS Generative AI Observability Best Practices](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/governance-perspective-managing-an-aiml-driven-organization.html){:target="_blank" rel="noopener noreferrer"}

## Contributors
**Authors:** <br>
- Felix Huthmacher, Senior Applied AI Architect <br>
- Rob Sable, Sr.Solutions Architect <br> 
- Nishant Arora, Solutions Architect <br>
- Sandeep Raveesh-Babu, Sr GenAI Specialist SA <br>
 
**Reviewers:** <br>
- Sireesha Muppala, Sr Mgr Solutions Architecture <br>
