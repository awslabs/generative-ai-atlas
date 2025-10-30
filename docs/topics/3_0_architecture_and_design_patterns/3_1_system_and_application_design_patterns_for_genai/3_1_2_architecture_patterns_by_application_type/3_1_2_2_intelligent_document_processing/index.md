<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Intelligent Document Processing

**Content Level: 100**


## Suggested Pre-Reading

None.

## TL;DR

IDP refers to ingesting input data in the form of documents, extracting useful information from them, and doing useful things to and/or with them. The documents themselves can be any standard office documents (scanned or electronic), call or meeting transcripts, tabular data files, images, or any other large chunks of file-based data that need to be processed through a pipeline to ingest, extract, and save the data as required. 

IDP is a popular category of generative AI use case because the return on investment is clear, easy to measure, and multiple orders of magnitude greater than the costs of running the IDP solution, when compared to costs of manual document processing in paper or electronic form.

## Intelligent Document Processing Concepts

IDP is conceptually similar to traditional database ETL (extract, transform, load) jobs, but now generative AI gives us very flexible ways to support a wide variety of unstructured data in addition to traditional structured data. Now we can use multi-modal LLMs to ingest many file types directly, and use common preprocessing techniques (discussed on the next page) to support nearly any other file type. 

LLMs now enable powerful and flexible optical character recognition (OCR) services that can be instructed by natural language to do almost anything you can describe clearly and concisely. Compared to previous generation document processing and extraction services, modern LLMs tend to be better (in terms of output quality and task flexibility), faster, and cheaper. Previous generation document processing services are great if you're already using them, happy with them, and more interested in "buy" vs "build," but if you're starting a new project and willing to do some prompt engineering, evaluate multi-modal LLM-based solutions first.


## Making it practical

Use cases can include not only processing of office documents, but also: 

* Form auto-population from documents, to eliminate the customer experience of "Why didn't they pull all this form info out of the document I just uploaded?"

* Image processing to extract text information for purposes of description or categorization, like detection of personal protective equipment being worn, or equipment identifiers and conditions.

* Entity extraction from unstructured data in documents to a graph database or filterable metadata. 

* Tabular data extraction for analytics based on data from unstructured documents.

* Summarization of documents to save time for human knowledge workers.

...and many more.

AWS services useful for IDP include Bedrock Knowledge Bases and Bedrock Data Automation. For customers interested in custom IDP solutions, AWS services like S3, SQS, Lambda, and Bedrock model invocations can be combined to automate the ingestion and processing of documents with complete customization.

In subsequent pages we'll discuss document ingestion and information extraction in conceptual and practical terms.

## Further Reading

* [Gen AI Intelligent Document Processing](https://github.com/aws-solutions-library-samples/accelerated-intelligent-document-processing-on-aws){:target="_blank" rel="noopener noreferrer"}

* [Intelligent Document Processing with AWS AI Services](https://github.com/aws-samples/aws-ai-intelligent-document-processing){:target="_blank" rel="noopener noreferrer"} : Github repository with a sample stack and many demonstration notebooks. From one of the AWS Solutions listed on the website in the previous bullet point.

* [Intelligent document processing on AWS](https://aws.amazon.com/ai/generative-ai/use-cases/document-processing/){:target="_blank" rel="noopener noreferrer"} :  benefits, use cases, and case studies

* [AWS Solutions for Intelligent Document Processing](https://aws.amazon.com/solutions/ai/?awsf.solution-area-4=solutions-use-case%23uc-mla-000-00009&solutions-all.sort-by=item.additionalFields.date&solutions-all.sort-order=desc&awsf.solution-type=*all&awsf.solution-area-1=*all&awsf.solution-area-2=*all&awsf.solution-area-3=*all&awsf.solution-area-5=*all&awsf.solution-area-6=*all&awsf.solution-area-7=*all#solutions){:target="_blank" rel="noopener noreferrer"}: Prescriptive guidance in the form of supported "AWS Solutions" stacks.


## Contributors

### Authors

* Dave Thibault - Sr. Applied AI Architect 

* Felix Huthmacher - Sr. Applied AI Architect 

### Reviewers

* Don Simpson - Principal Technologist 

* Felix Huthmacher - Sr. Applied AI Architect 

