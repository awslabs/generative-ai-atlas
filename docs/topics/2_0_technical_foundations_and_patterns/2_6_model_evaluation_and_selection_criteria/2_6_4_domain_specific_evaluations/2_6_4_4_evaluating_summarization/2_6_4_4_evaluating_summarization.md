<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Evaluating Summarization Use Cases

**Content Level: 200**

## Suggested Pre-Reading

* [Introduction to Generative AI Evaluations](../../introduction_to_generative_AI_evaluations.md)

## TL;DR

This chapter provides a comprehensive guide for software developers to effectively evaluate use cases involving summarization. It covers important evaluation metrics, practical frameworks, implementation strategies, and best practices to produce generated summaries that are accurate, relevant, and reliable. 

## 1. Introduction

Summarizing content is important as they exploit the benefits of Large Language Models (LLMs) to: 

* understand topic from a user query
* retrieve latest relevant information from multiple sources including documents and websites
* summarize the results and generate an answer

Customers may look to summarization use cases to improve efficiency, enhance decision making, reduce storage and time, and enhance user engagement, depending on the task. However, having metrics to evaluate summaries are vital in order to measure the output quality, make sure important information is not lost, extract key information, and reduce hallucination in the model. In addition, there are some domain specific knowledge requirements that need to be taken into account. 

This chapter outlines a structured approach to evaluating summarization use cases, providing developers with practical tools and methodologies to build more reliable AI applications. 


## Key Evaluation Metrics



* **Coverage Score:** This metric measures the amount of detail included in a summary from the original text.

**Algorithm:** 

```
Given the original text, an LLM generates 'n' questions
successful_qns = 0
For each of the 'n' questions: 
    LLM evaluates whether question {i} can be answered from the summarized content
    if it can be answered: 
        successful_qns += 1
return successful_qns/'n'

Coverage = 8/10 = 0.8 or 80%
```

* **Alignment Score:** This metric measures the factual alignment between the original text and the summary.

**Algorithm:** 

```
Given the summary, an LLM generates 'n' questions
successful_qns = 0
For each of the 'n' questions: 
    LLM generates answers for question {i} from the original content and summary
    if original content answer == summary answer: 
        successful_qns += 1
return successful_qns/'n'

Alignment = 8/10 = 0.8 or 80%
```



## Evaluation Frameworks and Tools

Below are specialized frameworks to facilitate the evaluation of text summarization use cases


### 3.1 DeepEval

DeepEval is an open source LLM evaluation framework for evaluating and testing large language models. The metrics are calculated from recent research in G_Eval, Ragas, and many other open-source frameworks. Specifically in the summarization space, DeepEval includes a summarization metric that combines Alignment and Coverage. LLM prompts are designed for an evaluation LLM to

*  generate ‘n’ questions from a text
* generate answers from those ‘n’ questions
* generate alignment verdicts
* generate  reasons for why a summarization score has been achieved. 

Overall DeepEval is similar to Pytest, but specialized for unit testing of LLM outputs, and can be incorporated into your summarization use cases. 


### 3.2 Ragas Summarization Metric

RAGAS offers a particularly developer-friendly suite of metrics designed for comprehensive RAG evaluation without heavy reliance on human-annotated references. The framework provides a metric for summarization: **summarization score**, which measures how well a summary (response) captures the most important information from a retrieved context. The step-by-step process to calculate this metric includes the following: 

* Extract important key phrases from the context and use the key phrases to generate a set of questions
* Compute the question-answer score (QA score) by dividing the number of questions that have the same answer among the original text and summary by the total number of questions
* There is an option to penalize larger summaries by providing a conciseness score, with the final summarization score being a weighted average of the above summarization score and the conciseness score

[Image: Image.jpg]

**Example**

```
from ragas.dataset_schema import SingleTurnSample
from ragas.metrics import SummarizationScore
sample = SingleTurnSample(
    response="A company is launching a fitness tracking app that helps users set exercise goals, log meals, and track water intake, with personalized workout suggestions and motivational reminders.",
    reference_contexts=[
        "A company is launching a new product, a smartphone app designed to help users track their fitness goals. The app allows users to set daily exercise targets, log their meals, and track their water intake. It also provides personalized workout recommendations and sends motivational reminders throughout the day."
    ]
)
scorer = SummarizationScore(llm=evaluator_llm)await scorer.single_turn_ascore(sample)
```

## Conclusion

Evaluating text summarization tasks is important for confirming that the summaries are complete and accurate. By understanding these evaluation metrics and utilizing appropriate frameworks and tools, software developers can assess and enhance their text summarization use cases. 


## References

* [DeepEval OpenSource](https://github.com/confident-ai/deepeval/tree/main){:target="_blank" rel="noopener noreferrer"}
* [Confident AI Blogpost: Evaluating an LLM Text Summarization Task](https://www.confident-ai.com/blog/a-step-by-step-guide-to-evaluating-an-llm-text-summarization-task){:target="_blank" rel="noopener noreferrer"}
* [Evaluating Summarization code example: Call Summarization](https://github.com/aws-samples/prompt-migration-for-large-language-model-agility/blob/main/use-case-examples/call-summarization/notebooks/Evaluate_Call_Summarization_Outputs.ipynb){:target="_blank" rel="noopener noreferrer"}

## Contributors

### Authors

* Suren Gunturu - Data Scientist II 

**Primary Reviewer:**

* Ruskin Dantra - Sr. Solution Architect 
