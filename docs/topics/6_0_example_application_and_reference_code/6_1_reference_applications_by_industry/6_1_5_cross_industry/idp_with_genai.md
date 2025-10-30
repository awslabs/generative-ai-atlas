<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Intelligent Document Processing with Generative AI

**Content Level: 300**

## Suggested Pre-Reading
* [What is intelligent document processing](https://aws.amazon.com/what-is/intelligent-document-processing/){:target="_blank" rel="noopener noreferrer"}

* [Amazon Bedrock Data Automation](https://aws.amazon.com/what-is/intelligent-document-processing/){:target="_blank" rel="noopener noreferrer"}

* [Amazon Textract](https://aws.amazon.com/textract/){:target="_blank" rel="noopener noreferrer"}

* [Amazon Sagemaker](https://aws.amazon.com/sagemaker/){:target="_blank" rel="noopener noreferrer"}

## TL;DR
The Generative AI Intelligent Document Processing reference architecture solves the important business challenge of manually processing  vast volumes of unstructured documents that create operational bottlenecks, introduce human errors, and fail to scale during peak periods across industries. This serverless AWS solution combines advanced OCR capabilities with generative AI models like Amazon Bedrock and Textract to automatically extract structured data from complex documents—whether they're loan applications in financial services, patient records in healthcare, contracts in legal firms, or regulatory filings in manufacturing. Enterprise architects, data engineers, operations teams, and compliance officers can leverage this modular, pay-per-use architecture that processes documents 10x faster than manual review with 92-95% accuracy while maintaining comprehensive audit trails and automatic scaling capabilities. Organizations should  implement this solution when they're experiencing document processing backlogs, need to improve data extraction accuracy, want to reduce operational costs, or require scalable processing capabilities that can handle variable workloads without infrastructure management overhead—making it ideal for any industry dealing with high-volume document workflows where speed, accuracy, and compliance are important business requirements.

## Industry
Cross-industry application with primary adoption in:
- Financial Services (loan processing, compliance documentation, regulatory filings)
- Healthcare (patient records, insurance claims, medical forms)
- Legal Services (contract analysis, case documentation, regulatory compliance)
- Insurance (claims processing, policy documentation, underwriting)
- Government (permit applications, citizen services, regulatory processing)
- Manufacturing (quality documentation, compliance records, supplier contracts)

## Business Situation
Organizations process millions of documents annually through manual review processes that create significant operational bottlenecks. Traditional approaches require teams of analysts to extract key information from forms, contracts, invoices, and regulatory documents. This manual processing introduces human error, creates inconsistent data quality, and fails to scale during peak business periods. Legacy OCR solutions struggle with complex layouts, handwritten text, and documents requiring contextual understanding. The result is delayed decision-making, increased operational costs, and poor customer experience due to processing delays.

## When to Use
Deploy this solution when your organization experiences document processing backlogs that impact business operations. Use it for high-volume scenarios where manual review creates bottlenecks, such as loan origination, insurance claims processing, or regulatory compliance workflows. The solution works best for organizations processing structured and semi-structured documents that contain extractable data fields. Consider implementation when you need to improve processing accuracy, reduce operational costs, or scale document processing capabilities without adding headcount. The architecture suits organizations requiring audit trails and compliance documentation for regulated industries.

## Benefits

**Business Benefits:**
- Reduce document processing time from hours to minutes, improving customer response times
- Lower operational costs by eliminating manual data entry and review processes
- Increase processing accuracy to 92-95%, reducing downstream errors and rework
- Scale processing capacity automatically during peak periods without staffing changes
- Improve compliance through automated audit trails, real time monitoring/tracking and consistent processing standards
- Enable 24/7 processing capabilities without human intervention
- Possible human feedback and evaluation. 

**Technology Benefits:**
- Pay-per-use serverless architecture eliminates infrastructure management overhead
- Automatic scaling handles variable workloads without capacity planning
- Built-in error handling and retry mechanisms result in reliable processing
- Real-time monitoring and alerting enable proactive issue resolution
- Modular flexible solution design allows customization for specific document types and business rules
- Integration APIs enable seamless connection with existing business systems

## Architecture Description, Diagram, and AWS Services

<div style="margin:auto;text-align:center;width:100%;"><img src="./assets/IDP.png" alt="IDP" width="800"/></div>

The architecture centers around a flexible processing pipeline that can handle multiple document types and processing patterns within a unified framework. At its core, the solution uses AWS Step Functions to orchestrate complex workflows, providing reliable processing even when individual components experience temporary failures. Amazon SQS provides intelligent queuing capabilities that manage processing loads and enable automatic scaling based on demand.

Document ingestion occurs through multiple channels, including direct S3 uploads and a modern web interface built with React and hosted on AWS Amplify. The web interface provides real-time visibility into processing status and enables business users to review results without requiring technical expertise. All documents are securely stored in Amazon S3 with appropriate lifecycle policies to manage costs while maintaining compliance requirements.

The processing engine supports three distinct patterns to accommodate different document types and business requirements. 


* Pattern 1 utilizes Amazon Bedrock Data Automation for end-to-end processing of document packets and media files.
* Pattern 2 combines Amazon Textract for OCR with Amazon Bedrock for classification and extraction, providing flexibility for documents requiring custom processing logic. 
* Pattern 3 incorporates UDOP classification through Amazon SageMaker for specialized document types that benefit from advanced machine learning models.

Each processing pattern includes error handling and retry mechanisms. The system automatically manages throttling when interacting with AI services and provides detailed logging through Amazon CloudWatch. Processing results are stored in structured formats that enable downstream integration with existing business systems.

The architecture includes built-in evaluation capabilities that assess extraction accuracy against baseline datasets. This feature enables continuous improvement of processing accuracy and provides metrics for compliance reporting. A knowledge base component allows users to query processed documents using natural language, extending the value of extracted information beyond traditional structured data use cases.

Monitoring and observability are integrated throughout the solution. CloudWatch dashboards provide real-time visibility into processing metrics, error rates, and system performance. Detailed logging enables rapid troubleshooting and provides audit trails for compliance requirements. The system includes automated alerting for important issues and provides comprehensive reporting capabilities for operational teams.

**AWS Services Used:**
- Amazon Bedrock (generative AI models and data automation)
- Amazon Textract (optical character recognition)
- Amazon SageMaker (machine learning model hosting)
- AWS Step Functions (workflow orchestration)
- Amazon S3 (document storage)
- Amazon SQS (message queuing)
- Amazon DynamoDB (metadata storage)
- AWS Lambda (serverless compute)
- Amazon CloudWatch (monitoring and logging)
- AWS Amplify (web interface hosting)
- Amazon Cognito (user authentication)

## Gen AI Patterns

**Intelligent document processing(IDP):** The solution implements IDP pattern for 

**Retrieval Augmented Generation (RAG):** Processed documents populate a searchable knowledge base that enables natural language queries against extracted information.

**Workflow Orchestration:** Step Functions coordinate multi-step AI processing workflows, managing dependencies between OCR, classification, and extraction tasks.

**Prompt Engineering:** The system uses structured prompts with examples to guide large language models in extracting specific data fields from document text.

**Human in the loop:** LLMs evaluate extraction confidence scores and identify potentially problematic results for human review.  



## AWS Well-Architected Best Practices

### Operational Excellence

#### GENOPS01-BP01: Establish model performance baselines and evaluation metrics
**Implementation**: The architecture includes a built-in evaluation framework that systematically assesses extraction accuracy against baseline datasets. The solution implements field-level accuracy measurement, document classification accuracy tracking, and confidence scoring for all extractions. CloudWatch metrics capture processing performance, error rates, and throughput statistics to establish operational baselines.

**Evidence**: The evaluation framework code demonstrates automated accuracy assessment with configurable thresholds. Performance benchmarks show 92-95% accuracy across different document types, with detailed metrics collection for continuous improvement.

#### GENOPS02-BP01: Monitor all application layers
**Implementation**: The solution implements monitoring across all layers including document ingestion, processing workflows, AI model invocations, and result storage. Amazon CloudWatch provides real-time visibility into Step Functions execution, Lambda performance, SQS queue depths, and Bedrock/Textract API calls. The web interface displays processing status and enables operational teams to track document workflows.

**Evidence**: CloudWatch dashboards provide metrics for each processing pattern, error tracking, and performance monitoring. The Step Functions orchestration enables detailed workflow visibility and troubleshooting capabilities.

#### GENOPS03-BP01: Implement prompt template management
**Implementation**: The architecture uses versioned prompt templates stored in configuration files for document classification and extraction tasks. Each processing pattern maintains structured prompts with examples that guide large language models in extracting specific data fields. The system supports few-shot learning through example-based prompting stored in vector databases.

**Evidence**: Configuration files demonstrate structured extraction schemas with validation rules. The prompt engineering approach uses consistent templates across document types while enabling customization for specific business requirements.

#### GENOPS04-BP01: Automate lifecycle management
**Implementation**: The solution uses Infrastructure as Code through CloudFormation templates for consistent deployment across environments. Automated deployment pipelines enable version control and rollback capabilities. The serverless architecture eliminates manual infrastructure management while providing automatic scaling and resource provisioning.

**Evidence**: CloudFormation templates demonstrate complete infrastructure automation. The modular stack design enables selective updates and customization without affecting important processing capabilities.

#### GENOPS04-BP02: Follow GenAIOps practices to optimize the application lifecycle
**Implementation**: The architecture implements CI/CD practices through automated deployment templates and version-controlled configuration management. The evaluation framework enables systematic testing of model performance changes. Processing patterns can be updated independently, enabling rapid iteration and improvement.

**Evidence**: The solution includes comprehensive documentation for deployment, testing, and customization. Sample datasets and evaluation metrics support continuous improvement practices.

### Security

#### GENSEC01-BP01: Grant least privilege access to foundation model endpoints
**Implementation**: The architecture uses IAM roles with least privilege principles for accessing Amazon Bedrock, Textract, and SageMaker endpoints. Each Lambda function has specific permissions limited to required AWS services. Amazon Cognito manages user authentication with multi-factor authentication support for the web interface.

**Evidence**: IAM role definitions in CloudFormation templates demonstrate granular permissions. Service-to-service communication uses role-based access without embedded credentials.

#### GENSEC02-BP01: Implement data encryption and secure data handling
**Implementation**: All data is encrypted at rest using AWS KMS and in transit using TLS. Document storage in S3 includes server-side encryption. Processing results maintain encryption throughout the workflow. The solution includes data residency controls and retention policies for compliance requirements.

**Evidence**: S3 bucket configurations demonstrate encryption settings. Lambda functions and Step Functions maintain secure data handling practices throughout processing workflows.

#### GENSEC03-BP01: Monitor and audit generative AI interactions
**Implementation**: The architecture provides audit trails for all document processing activities through CloudWatch logging. Processing decisions are tracked with confidence scores and model invocation details. The evaluation framework maintains historical accuracy metrics for compliance reporting.

**Evidence**: CloudWatch logs capture detailed processing information including model responses, confidence scores, and processing decisions. The web interface provides audit trail visibility for operational teams.

### Reliability

#### GENREL01-BP01: Scale and balance foundation model throughput as a function of utilization
**Implementation**: The solution uses Amazon SQS for intelligent queuing that manages processing loads and enables automatic scaling based on demand. Multiple processing patterns distribute workload across different AI services. The serverless architecture automatically scales Lambda functions and Step Functions based on processing volume.

**Evidence**: SQS configuration demonstrates queue-based load management. Processing patterns show distribution across Bedrock, Textract, and SageMaker services to balance throughput requirements.

#### GENREL02-BP01: Implement retry logic and error handling for model interactions
**Implementation**: Step Functions orchestration includes retry mechanisms for transient failures in AI service calls. The architecture handles throttling from Bedrock and Textract APIs through exponential backoff strategies. Error handling includes circuit breaker patterns to prevent cascading failures.

**Evidence**: Step Functions definitions demonstrate retry logic and error handling. Lambda functions include timeout and error management for AI service interactions.

#### GENREL03-BP01: Design for graceful degradation when models are unavailable
**Implementation**: The modular architecture enables fallback between processing patterns when specific AI services experience issues. Document processing can continue with alternative models or processing approaches. The system maintains processing queues during service interruptions.

**Evidence**: Multiple processing patterns provide redundancy options. SQS queuing can resume document processing after service restoration.

### Performance Efficiency

#### GENPERF01-BP01: Select appropriate foundation models for your use case
**Implementation**: The architecture supports three distinct processing patterns optimized for different document types and performance requirements. Pattern selection considers document complexity, processing speed requirements, and accuracy needs. The evaluation framework enables systematic comparison of model performance across different document types.

**Evidence**: Processing patterns demonstrate model selection based on use case requirements. Performance benchmarks show processing times and accuracy metrics for different approaches.

#### GENPERF01-BP02: Collect performance metrics from generative AI workloads
**Implementation**: The solution implements monitoring across all AI service interactions including Bedrock, Textract, and SageMaker endpoints. CloudWatch metrics capture processing latency, throughput, and error rates. The evaluation framework provides accuracy metrics and confidence assessment capabilities.

**Evidence**: CloudWatch integration demonstrates performance metric collection. Evaluation framework code shows systematic accuracy measurement and reporting capabilities.

#### GENPERF02-BP01: Optimize prompt engineering for performance
**Implementation**: The architecture uses structured prompts with examples to improve model accuracy and reduce processing time. Few-shot learning capabilities enable rapid adaptation to new document types without extensive retraining. Prompt templates are optimized for specific extraction tasks.

**Evidence**: Configuration files demonstrate optimized prompt structures. Few-shot example implementation shows performance improvement techniques.

### Cost Optimization

#### GENCOST01-BP01: Right-size model selection to optimize inference costs
**Implementation**: The solution provides multiple processing patterns with different cost profiles. Pattern 1 uses Bedrock Data Automation for end-to-end processing, Pattern 2 combines Textract with Bedrock for flexibility, and Pattern 3 incorporates SageMaker for specialized requirements. Organizations can select patterns based on cost and performance requirements.

**Evidence**: Processing patterns demonstrate different cost optimization approaches. Documentation includes cost considerations for pattern selection.

#### GENCOST02-BP01: Implement cost controls and monitoring
**Implementation**: The serverless architecture provides pay-per-use pricing that eliminates idle resource costs. Built-in cost controls prevent unexpected expenses through service limits and monitoring. The solution includes cost estimation frameworks for different processing volumes.

**Evidence**: CloudFormation templates include cost control configurations. Documentation provides cost calculation frameworks for capacity planning.

#### GENCOST03-BP01: Optimize prompt design for cost efficiency
**Implementation**: Prompt templates are designed to minimize token usage while maintaining extraction accuracy. The system uses structured prompts that guide models efficiently to required information. Few-shot examples are optimized for cost-effective learning.

**Evidence**: Prompt engineering examples demonstrate cost-optimized design. Processing patterns show token usage optimization strategies.

### Sustainability

#### GENSUS01-BP01: Implement auto scaling and serverless architectures to optimize resource utilization
**Implementation**: The entire architecture uses serverless AWS services including Lambda, Step Functions, and managed AI services. Automatic scaling prevents over-provisioning while providing processing capacity during peak periods. The solution minimizes resource consumption through efficient processing algorithms.

**Evidence**: Serverless architecture eliminates idle resource consumption. Auto-scaling configurations demonstrate efficient resource utilization.

#### GENSUS02-BP01: Optimize model selection and inference for sustainability
**Implementation**: Processing patterns are optimized for computational efficiency based on document complexity. The solution uses the most efficient models for specific tasks rather than applying heavyweight models universally. Caching mechanisms reduce redundant processing.

**Evidence**: Processing pattern selection demonstrates efficiency optimization. Model selection criteria include computational resource considerations.

#### GENSUS03-BP01: Implement efficient data processing and storage practices
**Implementation**: The architecture includes S3 lifecycle policies for cost-effective storage management. Document preprocessing optimizes OCR accuracy to reduce reprocessing requirements. Efficient data formats minimize storage and transfer costs.

**Evidence**: S3 configuration demonstrates lifecycle management. Processing optimization reduces computational requirements and environmental impact.

## Limitations

1. The solution requires documents to be in supported formats (PDF, JPEG, PNG, TIFF). Processing accuracy depends on document quality and legibility. Handwritten text recognition has lower accuracy rates compared to printed text. Complex table structures may require custom extraction logic.

2. Large documents (over 100 pages) may experience longer processing times. The system works best with structured and semi-structured documents rather than completely unstructured text. Custom document types require configuration and testing to achieve optimal accuracy.

3. Processing costs increase with document complexity and the number of AI model invocations required. Organizations with extremely high security requirements may need additional customization for air-gapped environments.

## Common Customizations

**Industry-Specific Schemas:** Configure extraction schemas for industry-specific document types such as medical forms, legal contracts, or financial statements. Add custom validation rules and data formatting requirements.

**Multi-Language Support:** Extend the solution to process documents in multiple languages by configuring appropriate OCR and language models. Add language detection capabilities for automatic routing.

**Integration Customizations:** Extend this artichecture into agentic workflow with tools to integrate with other existing business systems such as CRM platforms, ERP systems, or document management solutions. Add webhook notifications for real-time processing updates.

**Compliance Customizations:** Implement additional security controls for regulated industries. Add data residency controls, extended audit logging, and custom retention policies.

**Processing Logic Customizations:** Create custom classification models for specialized document types. Implement business rule engines for complex extraction logic. Add additional human-in-the-loop workflows for exception handling.

**User Interface Customizations:** Modify the web interface to match organizational branding and workflows. Add role-based access controls and custom reporting dashboards.

**Performance Customizations:** Implement document preprocessing for improved OCR accuracy. Add parallel processing capabilities for high-volume scenarios. Configure custom retry and timeout policies.


## Further Reading
* [Github Repository for the sample code](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws){:target="_blank" rel="noopener noreferrer"}
* [ AWS Solutions Library](https://aws.amazon.com/solutions/guidance/accelerated-intelligent-document-processing-on-aws/){:target="_blank" rel="noopener noreferrer"}

## Contributors
**Author**: Neelam Koshiya - Principal Applied AI Architect 

**Reviewer** Randy Defauw - Sr. Principal Solutions Architect 
