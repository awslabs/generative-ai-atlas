<!--
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Tokens and Embeddings

**Content Level: 200**

## TL;DR

Tokens are the basic units of text that language models process, while embeddings are numerical vector representations that capture semantic meaning. Amazon Bedrock provides powerful embedding models (like Titan Text Embeddings V2) for converting text into numerical vectors that enable semantic search, document clustering, and RAG applications. Understanding tokenization helps optimize costs and context window usage, while embeddings enable sophisticated text analysis and retrieval systems.

## Understanding Tokens

**Token** is the basic unit of text that language models process. Text is broken down into tokens before being processed by the model.

- **Characteristics:**
    - Can represent words, parts of words, or punctuation
    - Different models use different tokenization methods
    - Token count affects processing cost and context window usage
- **Examples:**
    - "Hello world" might be tokenized as ["Hello", " world"] (2 tokens)
    - "Bedrock" might be tokenized as ["Bed", "Rock"] (2 tokens)

### Tokenization Process

Tokenization is the process of converting raw text into tokens that language models can understand and process. This fundamental step affects everything from cost to context window management.

**Common Tokenization Patterns:**

    - **Word-level**: Each word becomes a token
    - **Subword-level**: Words are broken into smaller meaningful units
    - **Character-level**: Each character is a separate token

**Practical Examples:**
```
Text: "The quick brown fox jumps"
Tokens: ["The", " quick", " brown", " fox", " jumps"]
Token count: 5

Text: "AI-powered applications"
Tokens: ["AI", "-", "powered", " applications"]
Token count: 4

Text: "Hello, world!"
Tokens: ["Hello", ",", " world", "!"]
Token count: 4
```

### Token Economics

Understanding tokenization is important for cost optimization:

- **Input tokens**: Text you send to the model
- **Output tokens**: Text the model generates
- **Context tokens**: Previous conversation history
- **Cached tokens**: Reused computations (in supported models)

**Cost Optimization Strategies:**

1. **Efficient prompting**: Use concise, clear instructions
2. **Context management**: Trim unnecessary conversation history
3. **Batch processing**: Group similar requests together
4. **Token counting**: Monitor usage to predict costs

## Understanding Embeddings

**Embedding** is a numerical vector representation of text that captures semantic meaning, enabling mathematical operations on language.

- **Characteristics:**
    - High-dimensional vectors (typically 256-1024 dimensions)
    - Similar concepts have similar embeddings
    - Enable semantic search and similarity comparisons
- **Use Cases:**
    - Semantic search and information retrieval
    - Document clustering and classification
    - Recommendation systems
    - Retrieval Augmented Generation (RAG)

### How Embeddings Work

Embeddings transform text into numerical vectors where semantically similar content is positioned closer together in vector space:

```
"dog" → [0.2, -0.1, 0.8, ..., 0.3]
"puppy" → [0.3, -0.2, 0.7, ..., 0.4]
"car" → [-0.5, 0.9, -0.1, ..., -0.2]
```

The vectors for "dog" and "puppy" would be closer to each other than to "car" because they share semantic meaning.

## Embedding Models in Amazon Bedrock

Amazon Bedrock offers a variety of embedding models that serve as critical components for numerous AI applications, particularly those requiring semantic understanding of text and efficient information retrieval.

### Available Embedding Models

**Amazon's Embedding Models:**

- **Titan Embeddings G1 - Text**: Amazon's first-generation text embedding model
- **Titan Text Embeddings V2**: An improved version that adds batch inference capabilities while maintaining Knowledge bases compatibility
- **Titan Multimodal Embeddings G1**: Supports both batch inference and fine-tuning, along with model copy and share functionality


### Key Features and Integration Points

The embedding models in Amazon Bedrock offer several important capabilities:

1. **Knowledge Bases Integration**: Most embedding models support Amazon's Knowledge bases feature, enabling efficient document retrieval and question-answering systems
2. **Provisioned Throughput**: Select embedding models support consistent, dedicated capacity for applications requiring predictable performance
3. **Batch Inference**: Some models like Titan Text Embeddings V2 support batch processing for large volumes of text
4. **Fine-tuning Options**: Titan Multimodal Embeddings G1 supports fine-tuning for domain-specific adaptations


### Tips for Effective Embedding Usage

1. **Choose the Right Dimensions**: Lower dimensions (256) are faster and use less memory, while higher dimensions (1024) may capture more semantic information.

2. **Normalization**: Keep normalization enabled for cosine similarity comparisons.

3. **Binary vs. Float Embeddings**: Use binary embeddings when storage is a concern, and float embeddings when precision is more important.

4. **Provisioned Throughput**: For production applications with consistent embedding generation needs, consider using Provisioned Throughput for more predictable performance.

5. **Embedding Caching**: Store frequently used embeddings to avoid regenerating them, especially for static content.


## Complementary Capabilities

The embedding models work in conjunction with other specialized models in Amazon Bedrock:

- **Reranking Models**: Amazon Rerank 1.0 provides specialized reranking capabilities that can improve retrieval quality after initial embedding-based retrieval

- **Foundation Models**: These embedding models are designed to work seamlessly with large language models like Titan Text models, enabling end-to-end AI applications

When implementing embedding-based applications in Amazon Bedrock, organizations should consider their specific requirements around language support, throughput needs, and integration points with knowledge bases or retrieval-augmented generation (RAG) applications to select the appropriate embedding model.

## Further Reading

- [Amazon Titan Models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan.html){:target="_blank" rel="noopener noreferrer"}
- [Amazon Bedrock Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/embeddings.html){:target="_blank" rel="noopener noreferrer"}
- [Semantic Search with Embeddings](https://aws.amazon.com/blogs/machine-learning/build-a-semantic-search-engine-with-amazon-bedrock-titan-embeddings/){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author/s:**

* Alicja Kwasniewska - Sr Solution Architect 

**Primary Reviewer:**

* Deepika Kumar - Solution Architect 

**Additional Reviewer:**

* Afia Khan - Associate SA - GenAI 

* Kihyeon Myung - Sr Applied AI Architect 