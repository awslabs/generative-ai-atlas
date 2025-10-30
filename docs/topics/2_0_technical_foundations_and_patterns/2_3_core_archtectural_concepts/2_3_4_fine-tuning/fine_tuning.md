<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Fine Tuning

**Content Level: 200**

## Suggested Pre-Reading

* [Introduction to Large Language Models](../../../1_0_generative_ai_fundamentals/1_1_core_concepts_and_terminology/core_concepts_and_terminology.md)
* [Tokens and Tokenization](../../2_1_key_primitives/2_1_4_tokens/2_1_4_tokens.md)
* [Prompt Engineering Fundamentals](../2_3_2_prompt_engineering/index.md)

## TL;DR

Fine-tuning adapts pre-trained language models to specific tasks using supervised learning with domain-/task-specific datasets. This process improves model performance on targeted tasks while requiring fewer computational resources than full model training. In practice, this means customers can customize existing models for their specific needs - whether that's improving response accuracy in specialized fields like healthcare or legal, ensuring consistent output formatting for business documents, or correcting model biases in specific domains. The process requires high-quality datasets and  evaluation of whether fine-tuning offers advantages over simpler solutions like prompt engineering.

## Introduction to fine-tuning

A base large language model (LLM) performs well on many tasks as-is, but specific use cases require LLM customization through domain-specific knowledge, task-specific instructions, or both to boost base LLM performance. LLM pre-training includes fine-tuning as an instruction tuning step. The following sections explore fine-tuning applications for domain-/task-specific use cases that transform an off-the-shelf LLM into an expert. Fine-tuning enhances an LLM's domain knowledge and task execution capabilities using a relatively small dataset compared to the initial training data.

<div style="margin:auto;text-align:center;width:100%;"><img src="./assets/finetune-diagram.png" alt="Fine Tuning Diagram" width="800"/></div>

<center>Supervised finetuning with Amazon Bedrock Model Customization API</center><br>

Explore prompt engineering methods thoroughly before considering fine-tuning, as fine-tuning requires additional dataset preparation and training costs.

A base LLM might perform poorly despite elaborate prompt engineering techniques due to limited domain knowledge, uncommon languages, or small model size. Elaborate prompt engineering also increases latency by requiring longer input and output tokens, as seen in few-shot and chain-of-thought approaches. Model fine-tuning enhances the base model's capabilities to overcome these limitations. Through supervised learning, this process uses labeled prompt-completion pairs to update the model's weights, improving its ability to generate task-specific responses.

### **Fine-tuning use cases**

* **Task-specific use cases**: Model customization demonstrates strong performance for well-defined tasks like sentiment analysis, tool-calling/routing, entity recognition. In these cases preparing appropriate datasets for model customization is straightforward for customers. 
* **Injecting Domain Knowledge:** Model customization is effective when the goal is to incorporate domain-specific knowledge or information that remains relatively stable over time. A comparison of Supervised Fine-Tuning (SFT) and Retrieval-Augmented Generation (RAG) demonstrates that domain-specific LLMs enhance question-answering (Q&A) performance when combined with RAG, compared to using RAG with base models alone.
* **Improving Instruction Following:** Fine-tuning improves model performance in following structured instructions and output formats. This process enables models to generate responses matching predetermined templates, such as business reports, code documentation, or standardized forms.
* **Aligning Response Tone and Style:** When the objective is to match the model's responses to a specific tone, style, or brand voice, fine-tuning achieves this goal. This process aligns the model's outputs with the communication style of an organization or application.
* **Addressing Consistent Biases or Errors:** Fine-tuning corrects base model errors and biases through targeted training examples. For instance, a model that misclassifies medical terminology improves its accuracy through domain-specific training data.

### **Fine-tuning process**

1. **Data Preparation:** The first step in instruction fine-tuning is preparing the training data. This dataset should meet several important training characteristics. The dataset requires an adequate number of data points for effective fine-tuning. While there is no definitive rule for the optimal number of examples, successful fine-tuning typically requires a minimum of at least 500 data points. The fine-tuning dataset should maintain high quality standards. The fundamental principle of Artificial Intelligence and Machine Learning (AI/ML), "Garbage in, garbage out," remains critical for fine-tuning Large Language Models (LLMs). The dataset should also encompass the full spectrum of expected input and output variations to enable real-world applicability. Fine-tuning datasets differ from traditional training data in one key aspect: each example should include the specific prompt intended for the task. Data format requirements vary by model. Each target model requires specific formatting guideline verification during preparation.
2. **Training Implementation:** Once the fine-tuning dataset is ready, standard supervised fine-tuning requires dividing the dataset into training, validation, and test splits. During fine-tuning, selected prompts from the training dataset are passed to the LLM to generate output. The generated text is then compared with the ground truth responses specified in the fine-tuning data by the cross-entropy loss. The calculated loss enables weight updates through standard backpropagation. This process repeats across multiple batches of prompt-completion pairs over a few epochs in general. During fine-tuning, close training and validation loss during fine-tuning is important to track progress and prevent overfitting or underfitting.
3. **Performance Evaluation:** Lastly, performance testing of a fine-tuned model requires a held-out test set. Performance evaluation methods vary by task. For conventional AI/ML tasks such as intent classification, sentiment analysis, tool calling, and entity extraction, evaluation uses standard metrics like accuracy, F1 score, or token matching. Tasks with less quantifiable quality, including Q&A, summarization, and reasoning, require LLM-as-a-Judge scores or human evaluation.

**Output:** The fine-tuning process produces a new version of the base model optimized for specific target tasks. Fine-tuning with instruction prompts represents the most common LLM adaptation method. This approach has become the standard that "fine-tuning" now typically refers to instruction fine-tuning. 

### Performance Evaluation

A key consideration when fine-tuning is how to evaluate the quality of the model's completions. There are several metrics and benchmarks that determine how well a model is performing and how much better the fine-tuned version is than the original base model. See the [Evaluations](../../2_6_model_evaluation_and_selection_criteria/introduction_to_generative_AI_evaluations.md) section for more information. 

## Making it Practical

Fine-tuning becomes relevant when a customer application requires consistent, specialized responses that basic prompt engineering cannot achieve. Common scenarios include applications requiring company-specific knowledge, specialized document analysis tools, or domain-specific chatbots.

Before implementing fine-tuning, consider these key questions:

* Does the project have a high-quality fine-tuning dataset with sufficient volume (>500 samples with ground truth)?
    * Projects without ground truth datasets should consider [model distillation](../2_3_4_fine-tuning/2_3_4-4_Distillation/distillation.md) as an alternative
* Have base model prompt engineering techniques been tested for the target task? What specific gaps require fine-tuning?
    * Fine-tuning addresses performance and latency gaps. 
    * Cost benefits vary based on implementation factors such as model hosting requirements
* Which specific models require fine-tuning?
* What are the budget constraints for fine-tuning and inference?

The most popular methods for fine-tuning are:

* **[Full Fine-Tuning (FFT)](../2_3_4_fine-tuning/2_3_4-1_full_fine-tuning/full_fine-tuning.md):** Full fine-tuning updates all weights of a base model. This typically requires more computational resources and a larger fine-tuning dataset.
* **[Parameter Efficient Fine-Tuning (PEFT)](../2_3_4_fine-tuning/2_3_4-2_PEFT(parameter%20efficient%20fine-tuning)/peft.md)**: PEFT is arguably the most popular method for fine-tuning. This requires less computational resources as it only updates a portion of the weights of a base model using a PEFT adapter. 
* **[Alignment methods](../2_3_4_fine-tuning/2_3_4-3_Preference%20Alignment/preference_alignment.md):** These include Reinforcement Learning with Human Feedback (RLHF) and Direct Preference Optimization (DPO): This enables multi-dimensional improvements in model performance. Dataset preparation requires more structure than FFT and PEFT. DPO needs preference-based datasets, while RLHF requires human feedback data and reward metrics.

These methods need to be chosen based on a use case and requirements, and sometimes need to be used together. In practice, starting with PEFT requires the least computational requirements and is relatively faster for quick experiments. When PEFT reaches its performance ceiling, implementing FFT or combining with alignment methods becomes appropriate, depending on the available computational resources for each use case. The following sections covered under this fine-tuning topic will provide more details on these approaches.

The Amazon Bedrock Model Customization API provides several practical operational considerations. The quality of training data impacts outcomes. Well defined input-output pairs from actual user interactions often perform better than synthetic data. For example, in healthcare applications, using real de-identified patient records for training typically yields better results than artificially generated medical scenarios.

Cost and resource management require intensive planning. Fine-tuning consumes compute resources during training and potentially increases inference costs. When working with Amazon Bedrock, consider starting with smaller datasets to validate the approach before scaling up. Monitor the model's performance metrics through Amazon CloudWatch to determine if the fine-tuned model is maintaining its effectiveness over time. Many customers find that combining fine-tuning with RAG provides optimal results - using fine-tuning for core domain understanding while leveraging RAG for up-to-date information.

Security and compliance considerations often influence fine-tuning strategies. When working with sensitive data, utilize AWS's security features like KMS encryption and VPC endpoints. Maintain separate development and production versions of the fine-tuned models to enable stable performance in production while allowing for continued experimentation. Regular evaluation of model outputs against established benchmarks helps maintain quality standards and identify potential drift.

The iterative nature of fine-tuning means the initial implementation will likely need refinement. Start with a focused use case, measure results against measurable success criteria, and expand based on validated improvements. While fine-tuning improves model performance, the process is most effective as part of a broader strategy that includes proper prompt engineering, evaluation methods, and business-aligned metrics.

## Further Reading
* [Mastering Amazon Bedrock Custom Models Fine-tuning (Part 1): Getting started with Fine-tuning:](https://community.aws/content/2jNtByVshH7vnT20HEdPuMArTJL/mastering-amazon-bedrock-custom-models-fine-tuning-part-1-getting-started-with-fine-tuning){:target="_blank" rel="noopener noreferrer"} 
* [Cost Optimization Strategy and Techniques](../../../3_0_architecture_and_design_patterns/3_6_cost_optimization/3_6_3_cost_optimization_strategy/readme.md#finetuning-and-model-distillation)

## Contributors
**Primary Author:** Wangechi Doble- Principal Technologist 
**Primary Reviewer:** Sungmin Hong - Sr Applied Scientist 