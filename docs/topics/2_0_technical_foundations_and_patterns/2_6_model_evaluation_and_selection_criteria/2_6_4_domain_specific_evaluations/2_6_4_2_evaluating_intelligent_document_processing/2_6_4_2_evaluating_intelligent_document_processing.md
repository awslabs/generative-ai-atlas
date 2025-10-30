<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Evaluating Intelligent Document Processing Solutions

**Content Level: 200**

## Suggested Pre-Reading

* [Evaluation Techniques](../../2_6_3_evaluation_technique/2_6_3_evaluation_techniques.md)

## TL;DR

Intelligent Document Processing (IDP) using large language models (LLMs) offers powerful solutions across industries for automating document handling. This guide examines evaluation frameworks for two common IDP systems: one that processes documents through dynamic schema generation and extraction, and another that maps input documents to existing database fields with appropriate transformations.

## Intelligent Document Processing & Large Language Models

Intelligent Document Processing (IDP) refers to the automated extraction, classification, and processing of data from documents using AI technologies. With the integration of Large Language Models (LLMs), IDP has evolved from template-based systems to more flexible solutions capable of understanding context, inferring structure, and extracting relevant information from diverse document types.

Traditional document processing is labor-intensive and costly, with human operators manually reviewing and entering data from invoices, contracts, forms, and other business documents. LLM-powered IDP solutions reduce this burden by offering:

* Greater flexibility with unstructured documents
* Improved accuracy through contextual understanding
* Reduced setup time through zero/few-shot learning capabilities
* Better handling of document variations without explicit programming

### Case Study 1: Extracting Structured Data Without Predefined Schemas

Advanced IDP systems are required to dynamically determine relevant information and structure without prior domain-specific training. Consider a legal department extracting key provisions from thousands of unique contracts, each with different clauses and structures.

An IDP solution for this task typically includes these components:

|Component	|Function	|Challenges	|
|---	|---	|---	|
|PDF Ingestion	|Convert PDF to processable format	|PDF parsing errors, text flow issues, handling of tables/figures	|
|Document Chunking	|Divide document into logical segments	|Maintaining context, handling cross-references, optimal chunk sizing	|
|Schema Generation	|Dynamically identify relevant fields and structure	|Determining appropriate level of detail, balancing comprehensiveness with usability	|
|Data Extraction	|Extract values according to schema	|Handling ambiguity, maintaining structural relationships	|

#### Evaluation Framework

Each component requires specific evaluation metrics. For document chunking, you might use:

|Metric	|Description	|Calculation Method	|
|---	|---	|---	|
|Context Preservation Score	|How well chunks maintain logical context	|% of cross-references correctly maintained across chunks	|
|Content Coverage	|Percentage of relevant content preserved in chunks	|Semantic overlap between original and chunked content	|
|Chunking Efficiency	|Balance between number of chunks and information retention	|Ratio of information density to chunk count	|
|Logical Segmentation Accuracy	|Alignment of chunk boundaries with logical document sections	|% of chunks with boundaries matching semantic transitions	|

The most critical evaluation focuses on end results - the coverage and accuracy of extracted information. Consider:


1. **Ground truth comparison**: Compare extraction results against human-annotated data using exact match, partial match, and semantic similarity metrics.
2. **LLM-assisted evaluation**: When using dynamic schemas, use LLMs to intelligently compare extraction results with original documents via Amazon Bedrock Converse API, which supports various formats including PDFs and CSVs.
3. **Comprehensive assessment**: Evaluate both accuracy (what was correctly extracted) and coverage (what was missed).
4. **Human-in-the-loop review**: Incorporate human feedback for ambiguous cases and to validate LLM evaluations, as LLMs may occasionally misinterpret information.

### Case Study 2: Field Mapping and Data Translation

For financial institutions needing to ingest client data from diverse formats into a standardized database, IDP tasks involve mapping source attributes to target fields and translating/validating data points.


#### Field Mapping Evaluation

Using ground truth datasets created by subject matter experts (SMEs), evaluate:

1. **File-level accuracy**: Ability to identify correct source files for each field
2. **Column-level accuracy**: Complete matches where both source file and specific column are correctly identified

#### Data Translation Evaluation

While SMEs can provide ground truth data, PII considerations may limit complete evaluation. Address this by:

* Implementing Bedrock Guardrails to filter PII during LLM processing
* Adding data security maintenance with services like [Amazon Macie](https://aws.amazon.com/macie/){:target="_blank" rel="noopener noreferrer"}, [Amazon Comprehend PII detection,](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html){:target="_blank" rel="noopener noreferrer"} or [Amazon GuardDuty](https://aws.amazon.com/guardduty/){:target="_blank" rel="noopener noreferrer"}

## Making It Practical

When implementing IDP evaluations in real-world scenarios:

1. **Customize evaluation metrics** to your specific use case and business requirements
2. **Consider model selection tradeoffs** including performance, cost, and context window limitations
3. **Evaluate document handling capacity** - for large documents, implement intelligent chunking to fit content within LLM context limits
4. **Balance automation with human oversight** - particularly for high-value or sensitive documents
5. **Design iterative improvement processes** by incorporating evaluation feedback into prompt engineering and system design

Systematically evaluating your IDP solution's components and overall performance should result in optimal accuracy, efficiency, and value for your document processing needs.

## Further Reading

* [Architecture Patterns by Application Type: Intelligent Document Processing (IDP)](../../../../3_0_architecture_and_design_patterns/3_1_system_and_application_design_patterns_for_genai/3_1_2_architecture_patterns_by_application_type/3_1_2_2_intelligent_document_processing/index.md)

## Contributors

**Authors**

* Hayley Park - Applied Scientist II 

* Jae Oh Woo - Sr. Applied Scientist 

* Sungmin Hong - Sr. Applied Scientist 

**Primary Reviewer:**

* Tony Ouma - Sr. Applied AI Architect 
