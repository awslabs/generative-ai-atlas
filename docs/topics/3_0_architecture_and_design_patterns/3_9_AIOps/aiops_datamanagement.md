<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Data Management

**Content Level: 200**

## Suggested Pre-Reading

* [Data Engineering Concepts](../../2_0_technical_foundations_and_patterns/2_3_core_archtectural_concepts/2_3_1_data_engineering/2_3_1-1_data_engineering_foundation/data_engineering_concepts.md)


## TL;DR

Data management in AI Ops encompasses the end-to-end lifecycle of data used for generative AI applications, including data labeling, synthetic data generation, pipeline automation, and cataloging. These practices help ensure high-quality, reproducible, and scalable data workflows that underpin reliable model development and deployment.

---


## Data Pipelines
***Applied AI Ops Principles: Automation, Reproducibility, Security***

Even if you start with a pre-trained model, AI Ops still starts with data:

* **Prompt/Completion Logs**: In prompt engineering workflows, you need a repository of prompts and expected outputs. 
* **Embedding Data for RAG**: In retrieval-augmented generation, a workflow step is dedicated to indexing knowledge into a vector database. This means taking unstructured text (documents, knowledge base articles, etc.), splitting it into chunks, and converting each chunk into a vector embedding (using an embedding model). The embeddings are stored in a vector database which can be queried later. This pipeline often needs to be automated and kept up-to-date as new data comes in. For example, regularly ingesting the latest forum posts or articles relevant to your domain.
* **Training/Fine-Tuning Data**: If you fine-tune a foundation model on domain-specific knowledge, you must gather and prepare that data. This could be a collection of domain texts, question-answer pairs, conversation logs, etc. For instance, assembling a dataset of customer support emails and their resolutions could be used to fine-tune a customer service chatbot.
 
Whether it is for prompt engineering, RAG, or fine-tuning, data quality is key. Noisy or biased data leads to poor results. Therefore data quality checks, PII redaction, deduplication, and bias checks should be part of the data pipelines to reduce data quality issues like broken formats, duplicates, or biases in the data. Data quality directly influences model outputs, safety, and explainability.


### AI Ops Best Practices

* **Scalability**: data pipelines should be scalable, and able to handle diverse, often-times massive datasets. For example pre-training may require petabytes of data and thus requires scalable pipelines.
* **Robust protection mechanisms**:  incorporate robust protection mechanisms for sensitive data, especially when working with broad datasets that might contain personal information (e.g. names, emails, phone numbers). 
* **Data Quality Management**: to sanitize and deduplicate data, reduce biases, and maintain the overall quality of your datasets.

ETL tools like AWS Glue provide built-in mechanisms for data quality checks and detecting and handling sensitive data.
Orchestration is commonly handled via a workflow manager such as Managed Apache Airflow (MWAA) or AWS Step Functions.

## Data Labeling
***Applied AI Ops Principles: Automation***

Data labeling is foundational for training, evaluating, and fine-tuning generative AI models. High-quality labeled data enables models to learn relevant patterns and produce accurate outputs. 
In AI Ops, data labeling is approached systematically, with clear guidelines to help ensure consistency and minimize bias. Organizations typically combine manual annotation by subject matter experts, semi-automated labeling with model assistance, and programmatic labeling using rules or metadata. 
Quality assurance is embedded throughout the process, with regular audits, consensus checks, and feedback loops to maintain high standards. 
Version control of labeling guidelines and continuous documentation of labeling decisions are important for reproducibility and ongoing improvement. As datasets grow, automation and active learning become increasingly important to scale labeling efforts while maintaining quality.

### AI Ops Best Practices

* Define clear labeling guidelines and quality standards
* Implement regular quality audits of labeled data
* Track labeling costs and efficiency metrics
* Maintain version control of labeling guidelines
* Document bias mitigation strategies in labeling processes


Labeling services like Amazon SageMaker Ground Truth provide built-in workflows for these approaches, with features for label verification and quality metrics, and workforce management.

* Integration with ML pipelines
* Cost and efficiency tracking

## Synthetic Data Generation
***Applied AI Ops Principles: Automation, Security***

Synthetic data generation addresses challenges of data scarcity, privacy, and coverage of edge cases. By creating artificial data that mirrors the statistical properties of real-world datasets, teams can augment training corpora, test model robustness, and protect sensitive information. 

Common approaches include using foundation models to generate text, simulating data based on statistical distributions, and leveraging generative adversarial networks (GANs) for more complex scenarios. 

Quality assurance involves validating that synthetic data matches production schemas, adheres to business rules, and maintains distributional similarity to real data. 

Privacy is preserved through techniques such as anonymization and differential privacy, to help ensure that synthetic datasets do not expose personal or sensitive information. All synthetic data generation processes are integrated with existing data pipelines, tracked with versioning, and regularly validated against real-world benchmarks to help ensure ongoing relevance and utility.

### AI Ops Best Practices

* Data format consistency: Help ensure synthetic data matches production schema.
* Scale requirements: Plan for generation and storage capacity.
* Validation pipeline: Automate quality checks of generated data.
* Version control: Track synthetic data versions and generation parameters.
* Integration: Connect with existing data pipelines and catalogs.
* Documentation: Document generation parameters and methods.
* Quality metrics: Implement quality metrics for synthetic data.
* Data distribution review: Perform regular validation against real data distributions.
* Usage monitoring: Continuously track synthetic data performance in production.
* Lineage tracking: Maintain a clear lineage between real and synthetic data.


Services like Amazon Bedrock and Amazon SageMaker are commonly used for model-based synthetic data generation, whereas Amazon S3 is used for synthetic data storage, and services like AWS Glue for data validation and transformation.


## Data Catalog
***Applied AI Ops Principles: Versioning, Security, Ownership & Accountability, Reusability, Continuous Improvement***

Dataset versioning enables teams to track changes to datasets over time by creating snapshots that allows them to reference or revert to earlier states. This helps ensure data lineage and reproducibility in RAG, fine-tuning, and evaluation while maintaining data integrity throughout the development & experimentation.

Each dataset version typically includes important metadata such as timestamps, authorship information, and detailed change logs documenting specific modifications (e.g. added columns, corrected errors, filtered records). This comprehensive tracking enables teams to precisely identify which data version was used for specific model experiments or deployments.

For RAG systems specifically, versioning can become more complex as it involves tracking both the source documents as well as the derived vector embeddings. Solutions range from straightforward approaches using version-tagged identifiers (e.g., "doc1#v1#chunk1" for smaller projects) to sophisticated systems integrating with vector databases to maintain multiple embedding versions simultaneously.

Tools like LakeFS or DVC (Data Version Control) enable Git-like data ops, allowing teams to pull exact versions of data alongside their code. This helps ensure reproducibility, which is key for training, and fine-tuning models, as those results heavily depend on input data, and make it impossible to reliably recreate a model's training environment without tracking dataset changes. If model training or fine-tuning is not required, and the focus is exclusively on prompt engineering or RAG, then prompt management tools can be sufficient. These tools streamline prompt iteration, enable collaboration, and provide robust version control, without the complexity of a full dataset management system.

Ultimately these dataset versions should be added to a Data Catalog to help ensure data governance and discoverability, and to simplify collaboration across teams. Here common tools are a Amazon S3 data lake along with SageMaker Unified Studio or Amazon SageMaker Catalog as the foundation for organizing data and AI assets. 

## Further Reading
* [Amazon SageMaker Unified Studio data catalog Documentation](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/working-with-business-catalog.html){:target="_blank" rel="noopener noreferrer"}

## Contributors
**Authors:** <br>
- Felix Huthmacher, Senior Applied AI Architect 

**Reviewers:** <br>
- Dave Thibault, Senior Applied AI Architect <br>