<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Evaluating Retrieval-Augmented Generation (RAG) Systems

**Content Level: 200**

## Suggested Pre-Reading

* [Introduction to Generative AI Evaluations](../../introduction_to_generative_AI_evaluations.md)

## TL;DR

This chapter provides a comprehensive guide for software developers to effectively evaluate Retrieval-Augmented Generation (RAG) systems. It covers important evaluation metrics, practical frameworks, implementation strategies, and best practices to enable your RAG systems deliver accurate, relevant, and reliable results.

## 1. Introduction to RAG System Evaluation

Retrieval-Augmented Generation (RAG) systems represent a significant advancement in natural language processing by combining the generative capabilities of large language models with external knowledge retrieval. By fetching relevant information from knowledge bases before generating responses, RAG systems can produce more accurate, factual, and contextually appropriate outputs. However, the effectiveness of a RAG system depends on both the quality of its retrieval mechanism and the generation process. Systematic evaluation is therefore important to:

* Identify performance bottlenecks in the retrieval or generation components
* Confirm factual accuracy and minimize hallucinations
* Optimize relevance of retrieved contexts
* Measure overall system effectiveness against business requirements

This chapter outlines a structured approach to evaluating RAG systems, providing developers with practical tools and methodologies to build more reliable AI applications.


## 2. Key Evaluation Metrics

### 2.1 Retrieval Metrics

* **Hit Rate**: Measures the proportion of queries for which the system retrieves at least one relevant document. A higher hit rate indicates better retrieval coverage.
    

**Example**:

```
For 100 test queries, the system retrieves at least one relevant document for 
85 queries.
Hit Rate = 85/100 = 0.85 or 85%
```

* **Mean Reciprocal Rank (MRR)**: Evaluates how quickly the system retrieves relevant information by focusing on the position of the first relevant document. `MRR = 1/rank` of first relevant document, averaged across queries. Higher MRR values indicate better ranking performance.

**Example**:

```
Query 1: First relevant document is at position 1 → Reciprocal Rank = 1/1 = 1.0
Query 2: First relevant document is at position 3 → Reciprocal Rank = 1/3 = 0.33
Query 3: First relevant document is at position 2 → Reciprocal Rank = 1/2 = 0.5
MRR = (1.0 + 0.33 + 0.5)/3 = 0.61
```

* **Recall**: Quantifies the completeness of retrieval by calculating the proportion of relevant documents retrieved compared to all relevant documents. 
    `Recall = (relevant documents retrieved) / (total relevant documents).`

**Example**:

```
For a query about "climate change impacts," there are 10 relevant documents in 
the knowledge base
The system retrieves 7 of these relevant documents
Recall = 7/10 = 0.7 or 70%
```

* **Normalized Discounted Cumulative Gain (NDCG)**: Assesses the quality of ranking by considering both the relevance and position of retrieved documents. NDCG penalizes relevant documents appearing lower in search results, providing a nuanced view of retrieval quality.

**Example:**

```
For a query, documents are retrieved with relevance scores (on a scale of 0-3):
Position 1: Relevance 3 (highly relevant)
Position 2: Relevance 1 (somewhat relevant)
Position 3: Relevance 2 (relevant)
Position 4: Relevance 0 (not relevant)
DCG = 3 + 1/log₂(3) + 2/log₂(4) + 0/log₂(5) = 3 + 0.63 + 1 + 0 = 4.63
Ideal ranking would be: [3, 2, 1, 0]
IDCG = 3 + 2/log₂(3) + 1/log₂(4) + 0/log₂(5) = 3 + 1.26 + 0.5 + 0 = 4.76
NDCG = DCG/IDCG = 4.63/4.76 = 0.97
```

### 2.2 Generation Metrics

* **Faithfulness (Groundedness)**: Measures whether the generated response contains only information supported by the retrieved documents. This metric is critical for preventing hallucinations.
* **Answer Relevance**: Evaluates how directly the generated response addresses the user's query without including extraneous information.
* **Exact Match (EM)**: Calculates the percentage of generated answers that exactly match reference answers. While useful for factoid questions, this metric may be too strict for complex queries requiring nuanced responses.



## 3. Evaluation Frameworks and Tools

Several specialized frameworks have emerged to facilitate comprehensive RAG evaluation:

### 3.1 ARES (Automated RAG Evaluation System)

ARES provides an end-to-end automated framework for evaluating RAG systems with a focus on:

* Context relevance assessment
* Answer faithfulness verification
* Answer relevance measurement

The framework leverages synthetic training data and fine-tuned lightweight language models to efficiently evaluate RAG components without requiring extensive human annotation.

### 3.2 RAGBench

RAGBench offers a domain-diverse benchmark dataset specifically designed for RAG evaluation. Its TRACe evaluation framework introduces:

* Transparent metrics that provide clear insights into system performance
* Explainable evaluations that identify specific failure points
* Actionable feedback applicable across different RAG implementations and domains

### 3.3 VERA (Validation and Evaluation of Retrieval-Augmented Systems)

VERA enhances evaluation reliability through:

* Cross-encoder mechanisms that aggregate multiple evaluation metrics into a comprehensive score
* Bootstrap statistical methods that establish confidence bounds for evaluation results
* Transparent assessment of retrieval quality and its impact on generation

### 3.4 RAGAS Evaluation Metrics

RAGAS offers a particularly developer-friendly suite of metrics designed for comprehensive RAG evaluation without heavy reliance on human-annotated references. The framework provides metrics for retrieval, generation as well the end-to-end pipelines:

#### 3.4.1 Retrieval Metrics

1. **Context Precision**
    1. **Definition**: Context Precision is a metric that evaluates whether all of the ground-truth relevant items present in the contexts are ranked higher or not. Ideally all the relevant chunks should appear at the top ranks. This metric is computed using the question and the contexts, with values ranging between 0 and 1, where higher scores indicate better precision. 

**Example**:

```
Question: "What is the capital of France?"
Retrieved Contexts:
"Paris is the capital of France."
"Berlin is the capital of Germany."
"Madrid is the capital of Spain."

Analysis: Only the first context is relevant. ￼
Context Precision Score: 0.33 (1 relevant context out of 3) ￼
```

1. **Context Recall**
    1. **Definition**: Context recall measures the extent to which the retrieved context aligns with the annotated answer, treated as the ground truth. It is computed based on the `ground truth` and the `retrieved context`, and the values range between 0 and 1, with higher values indicating better performance.

**Example**:

```
Ground Truth Contexts: 
"Paris is the capital of France."  
"Paris is located in northern central France."

Retrieved Contexts: 
"Paris is the capital of France."
"Berlin is the capital of Germany."

Analysis: Only one of the two relevant contexts was retrieved. ￼
Context Recall Score: 0.5 (1 retrieved relevant context out of 2)
```

#### 3.4.2 Generation Metrics

1. **Faithfulness**
    1. **Definition**: This measures the factual consistency of the generated answer against the given context. It is calculated from answer and retrieved context. The answer is scaled to (0,1) range. Higher the better.

**Example**:

```
Question: "What is the capital of France?"
Generated Answer: "Paris is the capital of France and the largest city in Europe."
Retrieved Context: "Paris is the capital of France."
Analysis: The statement about Paris being the capital is supported, but the claim 
about it being the largest city in Europe is not present in the context.
Faithfulness Score: 0.5 (1 supported fact out of 2 statements)
```

1. **Answer Relevancy**
    1. **Definition**: This metric focuses on assessing how pertinent the generated answer is to the given prompt. A lower score is assigned to answers that are incomplete or contain redundant information. This metric is computed using the question and the answer, with values ranging between 0 and 1, where higher scores indicate better relevancy.

**Example**:

```
Question: "What is the capital of France?" ￼
Generated Answer: "Paris is the capital of France, known for its art, 
culture, and fashion." ￼
Analysis: The answer addresses the question but includes additional information.
Answer Relevancy Score: 0.75 (3 relevant concepts out of 4 total) ￼
```

#### 3.4.3 End-to-End Metrics

1. **Answer Similarity**
    1. **Definition**: The concept of Answer Semantic Similarity pertains to the assessment of the semantic resemblance between the generated answer and the ground truth. This evaluation is based on the `ground truth` and the `answer`, with values falling within the range of 0 to 1. A higher score signifies a better alignment between the generated answer and the ground truth.

**Example**:

```
Generated Answer: "Paris is the capital city of France." ￼
Reference Answer: "France’s capital is Paris."
Analysis: The answers are semantically similar despite different wording.
Answer Similarity Score: Approximately 0.9 (on a scale from 0 to 1)
```

1. **Answer Correctness**
    1. **Definition**: The assessment of Answer Correctness involves gauging the accuracy of the generated answer when compared to the ground truth. This evaluation relies on the `ground truth` and the `answer`, with scores ranging from 0 to 1. A higher score indicates a closer alignment between the generated answer and the ground truth, signifying better correctness. Answer correctness encompasses two critical aspects: semantic similarity between the generated answer and the ground truth, as well as factual similarity. These aspects are combined using a weighted scheme to formulate the answer correctness score. Users also have the option to employ a ‘threshold’ value to round the resulting score to binary, if desired.

**Example**:

```
Question: "When was the Eiffel Tower built?"
Context: "The Eiffel Tower was completed in 1889 for the Exposition Universelle 
(World's Fair)."
Answer: "The Eiffel Tower was completed in 1889."
Answer Correctness Score: High (≈ 0.95) as the answer is both faithful 
to the context and relevant to the question
```


By leveraging these metrics,  developers can systematically assess and enhance the performance of their RAG systems.

### **3.5. RAGChecker**

RAGChecker extends RAG evaluation by introducing a claim-based, structured verification framework, designed to systematically validate generated responses at a granular level. Its core metrics include:

* **Overall Metrics**
    * **Overall Precision**: Measures the proportion of generated claims that are factually correct.
    * **Overall Recall**: Assesses whether all necessary claims from the retrieved context are included in the generated response.
    * **Overall F1**: Combines precision and recall to provide a balanced evaluation of factuality.
* **Retrieval Metrics**
    * **Claim Recall**: Evaluates whether key claims from the retrieved context that are necessary to answer the question are present in the response.
    * **Context Precision**: Measures whether the retrieved context is strictly relevant and free from extraneous or misleading information.
* **Generation Metrics**
    * **Context Utilization**: Examines how effectively the retrieved context is used in forming the response.
    * **Hallucination**: Detects whether any unsupported or fabricated claims are introduced in the response.
    * **Self-Knowledge**: Evaluates whether the response incorporates general world knowledge beyond the retrieved context when appropriate.
    * **Faithfulness**: Similar to RAGAS, this metric checks the factual consistency of the response against the retrieved context, but with additional claim-level granularity.

By systematically verifying factual claims, RAGChecker enhances explainability and improves trustworthiness in RAG-generated responses. Its structured approach encourages responses that are not only factually accurate but also effectively leverage the retrieved evidence.

### 3.6 DeepEval Evaluation Metrics

DeepEval is an open source LLM evaluation framework for evaluating and testing large language models. The metrics are calculated from recent research in G_Eval, Ragas, and many other open-source frameworks.Overall DeepEval is similar to Pytest, but specialized for unit testing of LLM outputs, and can be incorporated into your summarization use cases. An example of a specific use case is shown below: 


```
import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

def test_case():
    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5
    )
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output from your LLM application
        actual_output="You have 30 days to get a full refund at no extra cost.",
        expected_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )
    assert_test(test_case, [correctness_metric])
```

## 4. Best Practices for Implementing RAG Evaluations

* Define Clear Evaluation Objectives: Establish specific goals for what aspects of the RAG system you intend to evaluate, such as accuracy, relevance, or latency.
* Utilize Appropriate Metrics: Select evaluation metrics that align with your objectives and provide meaningful insights into system performance. ￼
* Leverage Evaluation Frameworks: Incorporate established evaluation frameworks like ARES, RAGBench, VERA, and InspectorRAGet to streamline the evaluation process.
* Conduct Regular Evaluations: Implement continuous evaluation practices to monitor system performance over time and identify areas for improvement.



## 5. Conclusion

Evaluating RAG systems is important for confirming their effectiveness and reliability. By understanding key evaluation metrics and utilizing appropriate frameworks and tools, software developers can systematically assess and enhance the performance of RAG systems.


## References

* [RAGAS: Automated Evaluation of Retrieval Augmented Generation ￼](https://arxiv.org/abs/2309.15217){:target="_blank" rel="noopener noreferrer"}
* [RAGAS Documentation](https://docs.ragas.io/en/stable/){:target="_blank" rel="noopener noreferrer"}
* [ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2311.09476){:target="_blank" rel="noopener noreferrer"}
* [RAGBench: Explainable Benchmark for Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2407.11005){:target="_blank" rel="noopener noreferrer"}
* [VERA: Validation and evaluation of retrieval-augmented systems](https://www.amazon.science/publications/vera-validation-and-evaluation-of-retrieval-augmented-systems){:target="_blank" rel="noopener noreferrer"}
* [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://arxiv.org/abs/2408.08067){:target="_blank" rel="noopener noreferrer"}

## Contributors

### Authors

* Meghana Ashok - Machine Learning Engineer 

* Suren Gunturu - Data Scientist II 

* Rahul Ghosh - Applied Scientist 
