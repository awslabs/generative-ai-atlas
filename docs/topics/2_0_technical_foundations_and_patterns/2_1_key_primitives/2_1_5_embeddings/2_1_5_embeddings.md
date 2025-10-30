<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Embeddings: Semantic Representation

**Content Level: 100**



## Suggested Pre-Reading

- [Key Primitives](../index.md)

## TL;DR

Embeddings are numerical vector representations that translate text into multidimensional space where semantic relationships are preserved as geometric relationships.
These vectors (typically 384-1536 dimensions) enable machines to understand meaning rather than just match words, placing similar concepts closer together in vector space.
This mathematical representation allows computers to perform operations like measuring similarity between concepts and discovering relationships among them. Embeddings form the foundation for critical GenAI capabilities like semantic search, Retrieval Augmented Generation (RAG), content recommendation, and document clustering.
When implementing embeddings in production, developers should balance factors including model selection, storage requirements, chunking strategies, and vector database performance.
Understanding embeddings is important  for anyone building GenAI applications that require capturing and leveraging the semantic meaning of text.

## Embeddings: Semantic Representation

Embeddings are numerical vector representations of text that capture semantic meaning in a form that machines can process.
One can think of them as a way to translate human language into "coordinates" that a computer can understand and work with.
For instance, when humans read words like "cat" and "kitten", they naturally understand that both words refer to concepts.
However, computers don't inherently understand this relationship.
Embeddings solve this problem by converting words, sentences, or documents into lists of numbers (vectors) where similar concepts end up with similar number patterns.
Embeddings are similar to a map where every word or concept has specific coordinates.
On this map, related concepts like "cat" and "kitten" would be positioned close together, while unrelated concepts like "cat" and "refrigerator" would be far apart.
This is essentially what embeddings do - they create a mathematical space where the distance and direction between words represent their semantic relationships.
For example, in this mathematical space:

* "King" minus "Man" plus "Woman" might land close to "Queen"
* "Paris" minus "France" plus "Italy" might land close to "Rome"

These vector representations make it possible for AI systems to understand relationships between concepts, find similar content, and organize information based on meaning rather than just matching exact words.
Embeddings are fundamental concept that Retrieval Augmented Generation (RAG) uses to determine which content is relevant for a user’s request.

### Embedding Characteristics

Key properties of embeddings include:

* Dimensionality: Typically ranges from 384 to 1536 dimensions, with higher dimensions potentially capturing more nuanced semantic information
* Semantic similarity: Similar concepts appear closer together in the embedding space
* Mathematical operations: Support operations like similarity calculations (e.g., cosine similarity) and vector arithmetic

### Applications of Embeddings

Common use cases for embeddings include:

* Semantic search and retrieval
* Document clustering and organization
* Content recommendation
* Duplicate detection
* Cross-language information retrieval
* Input for downstream machine learning tasks

## Making it practical
In your journey building GenAI applications, embeddings play an important role in bridging the gap between human language and machine understanding. Here's how you'll encounter them in real-world applications:

### When to Use Embeddings

Embeddings are valuable when you need machines to understand the meaning of text, not just match keywords:

- Semantic search systems that understand synonyms and related concepts
- RAG applications that need to retrieve contextually relevant information
- Content recommendation engines where similarity matters more than exact matching
- Document clustering to organize large collections of text by topic
- Duplicate detection systems that identify conceptually similar content

### Real-world Implementation Considerations

When implementing embeddings in production environments:

- **Model selection**: Different embedding models have different strengths. Some are optimized for shorter text like queries, while others handle longer documents better. The default embedding dimensions (typically 384 to 1536) represent a tradeoff between semantic richness and computational efficiency.
- **Storage requirements**: Each document chunk in your knowledge base requires its own embedding vector, which means storage needs grow linearly with your content volume.
- **Chunking strategy**: How you divide documents significantly impacts retrieval quality. Too small chunks lose context, while too large chunks dilute relevance.
- **Vector databases**: As your collection grows, you'll need specialized storage solutions optimized for vector similarity search, such as vector databases or vector search capabilities in existing databases.

### Cost and Performance Balance
Consider these practical aspects as you scale:

- **Generation costs**: Creating embeddings for large document collections requires significant computation resources, which can be costly.
- **Latency considerations**: Real-time embedding generation adds latency to user interactions.
- **Query optimization**: As your vector database grows, query performance may degrade without proper indexing strategies.
- **Approximate vs. exact search**: Many systems use approximate nearest neighbor algorithms to trade minor accuracy for major speed improvements.

By understanding these practical considerations, you can make informed decisions about how to implement embeddings effectively in your GenAI applications, unlocking accurate and relevant results while maintaining reasonable performance characteristics.

### AWS Service Integration

You can implement embeddings in your AWS architecture through:

- **Amazon Bedrock**: Access embedding models like Titan Embeddings through API calls
- **Amazon OpenSearch Service**: Store and search embedding vectors efficiently at scale
- **Amazon RDS with pgvector**: Add vector search capabilities to PostgreSQL databases
- **SageMaker**: Train or deploy custom embedding models for specialized domains

Understanding how embeddings translate complex semantic relationships into machine-processable formats is important for building effective RAG systems and other modern AI applications where relevance and contextual understanding are key requirements.

## Further Reading
- [What are Embeddings in Machine Learning?](https://aws.amazon.com/what-is/embeddings-in-machine-learning/){:target="_blank" rel="noopener noreferrer"}

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
