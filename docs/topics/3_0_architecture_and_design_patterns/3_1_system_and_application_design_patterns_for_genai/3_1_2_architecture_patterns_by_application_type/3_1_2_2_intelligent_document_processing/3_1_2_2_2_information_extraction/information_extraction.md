<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Intelligent Document Processing: Information Extraction and Enrichment

**Content Level: 200**

### Suggested Pre-Reading:

[Document Ingestion](../3_1_2_2_1_document_ingestion/document_ingestion.md){:target="_blank" rel="noopener noreferrer"}

## TL;DR:

Modern intelligent document processing (IDP) with LLMs allows developers to extract any information they can describe to the LLM, but not necessarily all at once across a large context. This page addresses use cases and best practices for LLM-based information extraction and enrichment.

## Information Extraction and Enrichment

### Overview
IDP workloads usually end up in one or both of two broad categories:

1. **Structured data extraction**: extracting structure from unstructured data and make it available via structured queries via databases or index metadata, like OpenSearch match queries or SQL or graph database queries. This could also include form filling or processing, image categorization, sentiment analysis, entity extraction, or summarization.

2. **Semantic search**: Ingesting data for unstructured semantic Q&A use cases over full content of documents. This is a classic RAG chatbot situation.

### When do you need structured queries vs semantic search?
Many builders start with a RAG chatbot (number 2 above) but then eventually they want to ask questions about _all the documents_. Efficient RAG chatbots work the same we use a search engine: we have a question to answer and we pull as many documents as it takes to find the answer, usually the first five or ten. 

For example, we intuitively know we wouldn't go to our public search engine and ask for all the lease documents that don't have an auto-renewal clause. In that case, we would need to get all the lease documents and extract structured data (whether or not an auto-renewal clause is in the doc), then save that somewhere that would enable us to filter for records where that value is false.

Similarly, when implementing IDP workloads, a critical factor is watching out for the words "all the" (or similar concepts) in the expected user prompts. As soon as users want to know any question that can't be answered by the top five or 10 docs, it's a bad fit for semantic KNN search with large chunks being retrieved.

For example, setting this to an arbitrarily high number to enable those "all the" questions is a bad idea because then it creates a huge context in your prompt template and requires a larger model to understand it all, and ends up taking way too long (30-60 seconds sometimes) and users get frustrated. Also it still may not be enough if "all the" records you needed were more than the top 200.

The right way to answer the "all the" questions is to:

* Extract the structure you're interested in querying from the unstructured data, preferably at ingestion time to avoid runtime delay.

* Save it in a structured data format for structured data queries. 

* Take the schema of that structure as context, ask the model to take the user's prompt and the schema and output the structured query that's required to get the data out. 

* Take the query output from the model (a SQL select statement, for example) and run that query against your structured data source programmatically and retrieve the desired data. 

* Take the data outputs from the query and send them back to the user, or use the data to answer questions.

* Never ask the model to do rule-based operations  that could be done programmatically over large sets of data.

* Always use tools for complex rule-based processing, and let the model pick the tool and provide the tool inputs from the conversation context.

Since RAG concepts are covered elsewhere in this document (see _Further Reading_ section below), this page will focus on the use cases in number one above, to extract structured information from unstructured and use it downstream in your IDP pipeline.

### Data Extraction and Enrichment Use Cases

#### Entity Extraction

LLMs can follow natural language instructions to process text as desired. The entity extraction capabilities are flexible and powerful. If you can describe what you want extracted in a way that a well-meaning but overly-literal intern could understand it, and keep the input context minimal, then a small but high quality LLM can achieve it. For example, detecting subject->predicate->object triplets for nodes and edges in a graph database works well and will allow you to do graph traversal queries. Also writing queries to read the data back out of graph and other databases works well, if given a schema.

However, if you just need to filter on those concepts (who were the people in this document?) then storing them as metadata in a SQL or no-SQL database works as well. Don't over-engineer if you don't need the graph traversal queries (like "Find all the people who wrote these lease documents without auto-renewal policies, then find all the other documents those people wrote, then find their managers' email addresses.")

The more instructions, complexity, and examples you add (the more tokens total), the more likely it is that you'll end up needing a bigger model and your queries will slow down. A very common anti-pattern in prompt engineering is including too many explanations and examples and then needing a bigger model to understand it all. 

Note that multi-modal LLMs can be used to extract information from images as well, like part numbers, serial numbers, entities in the image, or other text or entity identification.

#### Form filling and processing

Many people have experienced the disappointment of being asked to upload a document into a web form and then being asked to enter data that was in the document into another form. The good news is that it's now easy for application builders to avoid this situation. That's why many job application systems, for example, have implemented the feature that when you upload your resume it will use it to pre-fill as many fields as possible on upcoming forms.

This is a well-solved use case of entity extraction with programmatic entry of the extracted data into the subsequent forms.

Similarly, documents that contain forms can be scanned by LLMs and have the data output to a programmatically useful format for downstream automated processing, like JSON, or JSON lines. 

#### Summarization, Categorization, and Sentiment Analysis

Automated summarization of documents can be a significant time saver for human knowledge workers. Storing a summary of the document along with the document (or wherever is programmatically accessible) for future use would be a form of enrichment.

Summaries can also be helpful as distilled versions of a document from which to more reliably categorize the document text into use-case-determined sets. Images can also be can also be categorized and summarized by multi-modal LLMs.

Sentiment analysis is another enrichment strategy that's useful to categorize documents, commonly used in call center use cases to determine customer satisfaction.

#### Vectorization

One of the most common enrichments is vectorizing text and images for semantic search use cases. Since that's well-covered elsewhere in Atlas, this section will not cover it further, other than to note that this would also qualify as an enrichment to data to enable the feature of semantic search.

## Making it Practical

As with prior advice, focus on use cases that will deliver quantifiable value. Replacement of manual document processing is easy to quantify in terms of the current cost, frees people up to deliver higher-value work, and accelerates production of business value.

There are many sample stacks and prescriptive guidance to accelerate your IDP journey. In addition to the resource shared on previous pages, see also [Enhanced Document Understanding on AWS](https://aws.amazon.com/solutions/implementations/enhanced-document-understanding-on-aws/?did=sl_card&trk=sl_card){:target="_blank" rel="noopener noreferrer"} and [LLM-Based Advanced Summarization](https://github.com/aws-samples/llm-based-advanced-summarization){:target="_blank" rel="noopener noreferrer"}

## Further Reading

* RAG coverage in ATLAS:

    * [Technical Foundations and Patterns/Key Primitives/RAG](../../../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_7_rag/2_1_7_rag.md)

    * [Technical Foundations and Patterns/Core Architectural Concepts/Retrieval Augmented Generation](../../../../../2_0_technical_foundations_and_patterns/2_3_core_archtectural_concepts/2_3_3_RAG(retrieval%20Augmented%20Generation)/index.md)

    * [Technical Foundations and Patterns/Model Evaluation and Selection Criteria/Domain Specific Evaluations/Evaluating RAG Systems](../../../../../2_0_technical_foundations_and_patterns/2_6_model_evaluation_and_selection_criteria/2_6_4_domain_specific_evaluations/2_6_4_1_evaluating_rag_systems/2_6_4_1_evaluating_rag_systems.md)

## Contributors

### Authors

* Dave Thibault - Sr. Applied AI Architect 

* Felix Huthmacher - Sr. Applied AI Architect 

### Reviewers

* Don Simpson - Principal Technologist 

* Felix Huthmacher - Sr. Applied AI Architect 
