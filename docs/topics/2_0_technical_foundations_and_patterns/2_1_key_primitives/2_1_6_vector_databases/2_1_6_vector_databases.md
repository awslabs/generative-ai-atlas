<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Vector Databases: Storing and Retrieving Semantic Information

**Content Level: 100**



## Suggested Pre-Reading

* [Embeddings](../2_1_5_embeddings/2_1_5_embeddings.md)

## TL;DR

Vector databases are specialized storage systems designed to efficiently store, index, and retrieve embedding vectors based on similarity rather than exact matching.
They form an important infrastructure component for many generative AI applications that need to connect LLMs with your organization's data, particularly for Retrieval Augmented Generation (RAG).
These databases use specialized indexing algorithms like "Hierarchical Navigable Small World" (HNSW) and "Locality-Sensitive Hashing" (LSH) to perform high-dimensional similarity searches quickly, enabling applications to find semantically similar content even when words don't match exactly.
Whether implemented as dedicated solutions or as extensions to existing databases (like pgvector for PostgreSQL), vector databases bridge the gap between unstructured data and the structured representations needed by AI models to deliver context-aware, knowledge-grounded responses.

## Vector Databases: Storing and Retrieving Semantic Information

Vector databases are specialized storage systems designed to efficiently index and retrieve embedding vectors based on similarity rather than exact matching.

Core Features

Key capabilities of vector databases include:

* Approximate Nearest Neighbor (ANN) search: Efficiently finding similar vectors without exhaustive comparison
* Indexing algorithms: Methods like HNSW, IVF, or LSH that organize vectors for quick retrieval
* Filtering: Combining semantic search with metadata filters for precise retrieval
* Vector management: Supporting CRUD operations on vectors and associated metadata

Architectural Considerations

When integrating vector databases:

* Scaling: Consider partitioning strategies and replication for high availability
* Consistency: Determine appropriate consistency models for your application needs
* Performance: Balance recall (finding the most similar items) against query latency
* Storage: Plan for growing vector collections and associated metadata

## Making it practical
Vector databases serve as a critical foundation for many generative AI applications, particularly those requiring contextual information retrieval.
Understanding when and how to use vector databases helps you build more effective AI solutions.
Vector databases excel in these scenarios:

- **Retrieval Augmented Generation (RAG)**: When you need to provide LLMs with relevant context from your business data before generating responses. Vector databases enable semantic search over your documents, finding information based on meaning rather than keywords.
- **Semantic search applications**: When users need to find information based on concepts rather than exact keyword matches. This improves user experience by understanding intent rather than relying on perfect search queries.
- **Recommendation systems**: For suggesting similar products, content, or answers based on semantic similarity rather than rigid categorization or tagging.
- **Multimodal applications**: When working with combinations of text, images, audio, or video, vector databases can store embeddings from different modalities in a unified way.
- **Duplicate detection**: Identifying similar or duplicate content across large datasets by comparing vector similarities.

### Implementation Considerations
When implementing vector databases in production:

- Choose the right solution: For simpler use cases with moderate data volumes, you might use vector extensions in traditional databases (like pgvector in PostgreSQL). For large-scale deployments, dedicated vector databases with vector search may be more appropriate.
- Embedding quality matters: The quality of your vector database is directly tied to the quality of your embeddings. You should focus on using appropriate embedding models for your domain.
- Index maintenance: As your data grows, establish processes for managing your vector indices, including updates, deletions, and optimizations.
- Hybrid approaches: Consider combining traditional search (keywords, filters) with vector search for the best results, especially when filtering by metadata is important.
- Performance tuning: Balance recall accuracy (finding the most relevant results) against query latency based on your application's needs.

## AWS Implementation Options
When implementing vector databases in AWS environments:

- Amazon OpenSearch Service: Offers vector search capabilities alongside traditional search features, making it ideal for hybrid search applications.
- Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL: Support pgvector extension for simpler vector search use cases that can be integrated with existing relational databases.
- Amazon SageMaker Feature Store: Can be used to store and manage feature vectors with built-in versioning and lineage tracking.
- AWS Managed Services for partner solutions: Several vector databases partners offer AWS integrations that simplify deployment and management.

Vector databases are often the "missing link" that connects your unstructured data (documents, images, audio) to your LLMs, enabling them to access and use your organization's knowledge effectively. 
Mastering vector database concepts is important for building production-grade generative AI applications.

## Further Reading
[What is Retrieval Augmented Generation?](https://aws.amazon.com/what-is/retrieval-augmented-generation/){:target="_blank" rel="noopener noreferrer"}

## Contributors

Author/s:

 - Markus Bestehorn - Tech lead Generative AI EMEA 

Primary Reviewers:

 - Yibo Liang - Generative AI Specialist SA 
 - Emily Ransley - Generative AI Specialist SA 

Additional Reviewer/s: 

 - Ana-Maria Olaru - Sr. Program Manager 
 - Andrew Hood - Head of Program Development 
 - Dominic Murphy - Sr Mgr, Applied AI Architecture 
 - Gareth Faires - Sr Generative AI Specialist SA 
