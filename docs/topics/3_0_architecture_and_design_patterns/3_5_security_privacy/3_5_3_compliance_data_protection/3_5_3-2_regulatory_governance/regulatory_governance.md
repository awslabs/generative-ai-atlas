<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Regulatory Compliance and Governance



**Content Level: 300**


## Suggested Pre-Reading

* [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/){:target="_blank" rel="noopener noreferrer"}
* [Protecting data is our ongoing commitment to European customers](https://aws.amazon.com/compliance/eu-data-protection/){:target="_blank" rel="noopener noreferrer"}

## TL;DR

**_Disclaimer_**: This page is provided for informational purposes only and does not constitute legal advice. Regulatory compliance is context-specific and subject to change. Organizations are responsible for consulting legal counsel to understand their obligations under applicable laws and regulations.

Organizations should first understand the complex regulatory landscape they operate in. Since AWS customers remain responsible for their own compliance, it is important to begin by thoroughly evaluating how specific use cases align with relevant regulations. This evaluation then forms the foundation for defining clear and compliant artificial intelligence (“AI”) requirements. The final step is to establish a balanced governance framework that enables compliance and maintains strong oversight through comprehensive audit capabilities.

## Regulations and standards landscape

As you decide to adopt AI technologies, the implementation of regulatory compliance and governance frameworks becomes increasingly important. The frameworks and guidance available today (such as the European Union AI Act, applicable ISO standards,  and industry best practices) can help you build a strong foundation for your AI implementation. As the regulatory landscape continues to evolve, you should be prepared to adapt. Success requires a thoughtful balance between innovation and risk management, while employing appropriate audit controls based on specific use cases and implementation scope.

### Regulations

As AI technologies continue to evolve and become embedded in products, services, and infrastructure, responsible development and deployment are more important than ever. 

The global regulatory environment is rapidly evolving. Builders must stay informed and compliant with applicable laws, including:

* [**European Union AI Act (EU AI Act)**](https://artificialintelligenceact.eu/){:target="_blank" rel="noopener noreferrer"}: Classifies AI systems by risk and imposes strict requirements for high-risk use cases (e.g., biometric ID, critical infrastructure).
* [**GDPR & Data Protection Laws**](https://aws.amazon.com/compliance/gdpr-center/){:target="_blank" rel="noopener noreferrer"}: These govern the handling of personal data in AI training and inference processes.
* **Sector-Specific Regulations**: Financial, healthcare, and education sectors often carry additional AI-related obligations.

Whether you're developing applications, models, or infrastructure, it's important to architect with compliance in mind. You should:

* **Conduct Risk Assessments**: Identify and mitigate risks related to algorithmic harm, misuse, and operational failures.
* **Implement Auditable Systems**: Maintain logs and documentation for traceability and future audits.
* **Establish Governance Controls**: Assign accountability within your team or organization for how AI systems are used.
* **Design for Adaptability**: Be prepared to adjust to evolving laws and emerging best practices.

We encourage you to track guidance from regulatory bodies, such as:

* European Commission (AI Office)
* U.S. National Institute of Standards and Technology (NIST AI RMF)
* OECD Principles on AI

### Developments
In 2024, more than 1,000 AI policy initiatives emerged from 69 countries, territories, and regions. This surge in regulatory interest reflects the growing impact of AI on society and business operations. In August 2024, the European Union AI Act (the “Act”), which establishes a comprehensive framework for AI governance, became effective. The Act introduces a risk-based approach, categorizing AI applications into distinct risk levels: 

* **Prohibited AI systems**: The Act prohibits certain AI use cases with “unacceptable risk”. 
* **High-risk AI systems**: The Act places numerous requirements on AI systems used in ways that the EU considers “high risk”. 
* **General-purpose AI systems**: The Act includes transparency, documentation, and copyright obligations for "general purpose AI systems". Additional documentation and safety requirements are required for general purpose AI systems that present “systemic risk.” 
* **Low-risk AI systems**: The Act imposes notice requirements on low-risk AI systems (e.g., informing a user that they are using AI where not obvious).

### Standards

AI standards offer valuable guidance for organizations to develop trustworthy AI management systems. In December
2023, ISO introduced the [42001 International Standard](https://www.iso.org/standard/42001){:target="_blank" rel="noopener noreferrer"}, which intends to help organizations to responsibly develop, monitor or provide products or services that leverage AI. Among the numerous controls included in the standard it is possible to identify some key elements that help us to better understand its focus:

* **Risk Management**: organizations are required to implement processes to identify, analyze, evaluate, and monitor the risks during the entire management system's lifecycle.
* **AI impact assessment**: organizations should define a process to assess potential consequences for users of the AI system. An impact assessment could be performed in different ways, but it should consider the technical and societal context where the AI is developed.
* **System Lifecycle management**: organizations should take care of all the aspects of the development of the AI System, including planning, testing and remediating the findings.
* **Performance optimization**: the standard also places a strong emphasis on performance, requiring organizations to continuously improve the effectiveness of their AI management system.
* **Supplier management**: the controls cover not only the organization's internal processes but also extend to suppliers, who must be aligned with the organization’s principles and approach.

## Building a governance framework

Risk management forms the cornerstone of any governance framework. [The NIST AI Risk Management framework (RMF)](https://www.nist.gov/itl/ai-risk-management-framework){:target="_blank" rel="noopener noreferrer"} can provide a framework for risk management for AI applications. To help your organization’s workforce understand the risks associated with AI and what is acceptable use, you should create a AI governance strategy, with specific usage guidelines, and make sure that your users are made aware of these policies at the right time. Effective governance of AI begins with establishing clear organizational structures and accountability. Leadership should define who holds responsibility for AI system oversight, how decisions are made, and how risks are managed. This framework should extend beyond traditional IT governance to encompass the unique challenges posed by AI. Organizations should develop systematic processes for assessing and monitoring risks associated with their AI systems. This includes not only technical risks but also responsible AI dimensions and potential impacts on stakeholders. Regular audits and updates help ensure the framework remains relevant as technology and regulations evolve. Data governance takes on particular importance in the context of AI. The quality and integrity of training data directly influence model performance and potential biases. Organizations should establish robust processes for data collection, validation, and protection. This includes maintaining clear data lineage and implementing appropriate access controls.

## Making it Practical

The [AWS Cloud Adoption Framework for AI (CAF-AI)](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html){:target="_blank" rel="noopener noreferrer"} relies on the [AWS Cloud Adoption Framework (CAF)](https://aws.amazon.com/cloud-adoption-framework/){:target="_blank" rel="noopener noreferrer"} foundational capabilities and enriches many of them so they include the changes that AI demands. In addition, it adds new foundational capabilities that organizations should consider as part of their AI journey. The [governance perspective](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/governance-perspective-managing-an-aiml-driven-organization.html){:target="_blank" rel="noopener noreferrer"} of CAF-AI helps you orchestrate your AI initiatives while maximizing organizational benefits and minimizing transformation related risks. It pays special attention to the changing nature of the risk and therefore the cost that is associated both with the development as well as the scaling of AI. For governance, CAF-AI recommends focusing on these capabilities:

* **Cloud Financial Management (CFM)** helps you plan, measure, and optimize the cost of AI in the cloud.
* **Data Curation** creates value from data catalogs and products.
* **Risk Management** leverages AWS to mitigate and manage the risks inherent to AI.
* **Responsible Use of AI** fosters continual AI innovation through responsible use.

### Monitoring Compliance with AWS

To learn whether an AWS service is within the scope of specific compliance programs, see [AWS services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/){:target="_blank" rel="noopener noreferrer"} and choose the compliance program that you are interested in. For general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/){:target="_blank" rel="noopener noreferrer"}. You can download third-party audit reports using AWS Artifact. For more information, see [Downloading Reports in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html){:target="_blank" rel="noopener noreferrer"}. Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. 

### AWS Services

The implementation of compliance controls should align with the scope of the AI system being deployed. These AWS services can help you with a compliant AI implementation:

* **Amazon SageMaker AI:** It provides purpose-built ML governance tools for managing control access, activity tracking, and reporting across the ML lifecycle. Manage least-privilege permissions for ML practitioners using [Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html){:target="_blank" rel="noopener noreferrer"}, create detailed model documentation using [Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html){:target="_blank" rel="noopener noreferrer"}, and with [Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html){:target="_blank" rel="noopener noreferrer"}, you can gain visibility into your models with centralized dashboards using. [SageMaker Data and AI Governance](https://aws.amazon.com/sagemaker/data-ai-governance){:target="_blank" rel="noopener noreferrer"} offers a comprehensive set of features by providing a unified experience for cataloging, discovering, and governing data and AI assets. It’s centered around SageMaker Catalog built on [Amazon DataZone](https://aws.amazon.com/datazone/){:target="_blank" rel="noopener noreferrer"}, providing a centralized repository that is accessible through Amazon SageMaker Unified Studio. The catalog is built directly into SageMaker, offering seamless integration with existing SageMaker workflows and tools, helping engineers, data scientists, and analysts to safely find and use authorized data and models through advanced search features. With SageMaker, users can safeguard and protect their AI models using guardrails and implementing responsible AI policies.
* **Amazon Bedrock:** It offers monitoring and logging capabilities that can support your governance and audit requirements. You can use Amazon CloudWatch to track usage metrics and build customized dashboards with metrics that can be used for your audit purposes. You can also use AWS CloudTrail to monitor API activity and troubleshoot issues as you integrate other systems into your generative AI applications. You can also choose to store the metadata, requests, and responses in your Amazon S3 bucket, as well as to Amazon CloudWatch Logs. Finally, to prevent potential misuse, Amazon Bedrock implements [automated abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html){:target="_blank" rel="noopener noreferrer"} mechanisms to identify potential violations of AWS’s [Acceptable Use Policy](https://aws.amazon.com/aup/){:target="_blank" rel="noopener noreferrer"} (AUP) and Service Terms, including the [Responsible AI Policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/){:target="_blank" rel="noopener noreferrer"} or a third-party model provider’s AUP. You can also use [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/){:target="_blank" rel="noopener noreferrer"} to provide an additional level of control on top of the protections built into foundation models (FMs) to help deliver relevant and safe user experiences that align with your organization’s policies and principles.
* **AWS Audit Manager:** It provides a [pre-built standard framework](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html){:target="_blank" rel="noopener noreferrer"} to help you gain visibility into how your Generative AI implementation on Amazon Bedrock and Amazon SageMaker AI is working against AWS recommended best practices. This framework includes a pre-built collection of controls with descriptions and testing procedures. These controls are grouped into control sets according to Generative AI best practices. You can also customize this framework and its controls to support internal audits with specific requirements. 

## Further Reading

* [Generative AI adoption and compliance: Simplifying the path forward with AWS Audit Manager](https://aws.amazon.com/blogs/security/generative-ai-adoption-and-compliance-simplifying-the-path-forward-with-aws-audit-manager/){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author**

* Guillermo Tantachuco - Principal Technologist, AI []

**Reviewers**

* Sundeep Bhasin - Principal FSI Compliance Specialist []

* Andrew Kane - GenAI Security/Compliance Lead 