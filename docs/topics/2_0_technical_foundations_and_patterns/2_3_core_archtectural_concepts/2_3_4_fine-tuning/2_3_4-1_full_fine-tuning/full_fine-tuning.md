<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Full fine-tuning

**Content Level: 200**


## Suggested Pre-Reading

* [Fine-Tuning Fundamentals](../fine_tuning.md)
* [Fine-Tuning and Model Adaptation](../../../../2_0_technical_foundations_and_patterns/2_1_key_primitives/2_1_8_fine_tuning/2_1_8_fine_tuning.md)

## TL;DR

Full fine-tuning updates all parameters of a pre-trained language model through supervised learning on task-specific data, enabling measurable performance improvements for targeted use cases. This adaptation is resource intensive with high computational costs and complex training procedures to avoid catastrophic forgetting. These requirements create a trade-off between performance gains and infrastructure costs. Implement full fine-tuning only when quantifiable performance improvements outweigh specific computational and maintenance costs.

## Understanding Full Fine-Tuning

Full fine-tuning LLMs is the process of updating all model parameters during training to adapt the model to a specific task or domain. Unlike other adaptation techniques, full fine-tuning modifies all model weights to deliver complete model adaptation. This approach differs from alternatives such as prompt engineering, which relies on crafting effective prompts without model modification, and few-shot learning, which uses examples within the prompt to guide model behavior.

Parameter-efficient fine-tuning (PEFT) methods like [LoRA (Low-Rank Adaptation)](../2_3_4-2_PEFT(parameter%20efficient%20fine-tuning)/2_3_4_2_1LoRA/lora.md) and adapters offer a middle ground, updating only a small subset of parameters while keeping most of the model frozen. While PEFT methods require fewer computational resources, full fine-tuning becomes necessary when domain-specific behavior demands deeper model modifications. This includes cases requiring extensive syntactic shifts, new reasoning paths, or novel token-level patterns. For example, legal document analysis often requires understanding complex legal terminology and reasoning patterns that cannot be effectively captured through prompt engineering or PEFT methods alone.

Full fine-tuning improves model performance in specialized domains like healthcare, where models need to understand medical terminology, interpret clinical guidelines, and maintain high accuracy in patient-related tasks. Financial services applications benefit from full fine-tuning when models must comprehend complex financial instruments and regulatory requirements. Scientific research applications often require full fine-tuning to process technical publications and experimental data accurately.


<div style="margin:auto;text-align:center;"><img src="./assets/full-finetuning.png" alt="Full Fine Tuning Diagram"/></div>
<center>Full fine-tuning creates a full copy of the original LLM</center>

### Full fine-tuning process

The process involves initializing the pre-trained model with its existing weights and then training it on a new dataset. During this training phase, all layers of the model are updated based on the task-specific data. This approach enables the model to learn new patterns, terminologies, and structures specific to the fine-tuning dataset, improving its ability to generate relevant and context-aware outputs. However, full fine-tuning requires a large amount of labeled data to prevent overfitting and ensure that the model generalizes well to unseen inputs.

### Challenges

Full fine-tuning comes with large computational costs. Since the entire model is updated, the process requires substantial GPU memory, processing power, and storage capacity. Training large-scale models from scratch is already resource-intensive, and full fine-tuning compounds these demands. Additionally, fine-tuning large models can take days or weeks, depending on the model size and dataset complexity.

Another challenge is catastrophic forgetting, where the model loses knowledge from its pre-trained phase as it adapts to the new dataset. This issue can be mitigated using techniques such as regularization methods, continual learning strategies, or selective fine-tuning of only certain layers while freezing others. A common approach is to freeze lower transformer layers (which encode more general linguistic knowledge) and fine-tune only the top layers or task-specific heads. Additionally, replay strategies or knowledge distillation from the original model can preserve general capabilities.

Based on these trade-offs, full fine-tuning is typically used when a high degree of task specialization is needed and when the benefits justify the computational costs. In cases where efficiency is a priority, alternative approaches like instruction tuning, adapter-based fine-tuning, or retrieval-augmented generation may be preferable. Full fine-tuning LLMs delivers optimal performance when optimizing models for specialized tasks.

## Making it Practical

Full fine-tuning becomes relevant when working with customers who need specialized language models for their domain. Common scenarios include processing medical records, analyzing legal documents, or handling industry-specific technical documentation. Amazon SageMaker is ideal for implementing full fine-tuning workflows, with additional support available through Amazon EC2 instances equipped with specialized GPU configurations.

### Data Considerations

The first consideration is data availability. Customers need large amounts of high-quality training data - typically tens of thousands of examples minimum - to achieve meaningful results. This data should be properly labeled and representative of the target use case. For example, a healthcare provider looking to fine-tune a model for radiology reports would need a large collection of validated reports with consistent formatting and terminology. Using Amazon SageMaker Ground Truth can help establish efficient data labeling workflows. Additionally, tokenization mismatches can cause noise in domain-specific vocabularies. It's critical to pre-tokenize and validate how domain terms (e.g., medical acronyms) are split by the tokenizer. For long-form documents, apply chunking or sliding window techniques to preserve context. Amazon SageMaker Processing Jobs can help automate these data preparation steps.

### Resource Requirements and Technical Feasibility

When evaluating whether full fine-tuning is appropriate, engineers should assess core feasibility criteria such as model scale, number of trainable parameters, available GPU memory, and sequence length.

Resource requirements form the second major consideration. Full fine-tuning demands intensive computational resources and time. A typical fine-tuning job for a large language model can take several days to weeks and require multiple GPUs. Using Amazon SageMaker's distributed training capabilities on ml.p4d or ml.g5 instances can help optimize this process. The infrastructure costs need business justification. Consider starting with smaller models or alternative approaches like few-shot learning if the use case allows. Make use of training efficiency techniques such as gradient accumulation to simulate large batch sizes, mixed-precision (FP16/BF16) training to reduce memory usage, and gradient checkpointing to trade compute for memory. Amazon SageMaker's built-in algorithms and training optimizations can help implement these techniques effectively.

The third consideration is ongoing maintenance. Fine-tuned models require regular evaluation and potential retraining as domain knowledge evolves. Amazon SageMaker Model Monitor helps establish specific metrics for model performance and implements monitoring systems to detect degradation. Amazon CloudWatch can track key performance indicators and trigger alerts when models need attention. Plan for periodic retraining cycles, especially in rapidly changing fields like medicine or technology.

When implementing full fine-tuning, start with a smaller subset of data to validate the approach before committing to a full-scale implementation. Use Amazon SageMaker Experiments to track different training configurations and their outcomes. Monitor the training process closely for signs of catastrophic forgetting or overfitting. Amazon SageMaker Debugger can help identify training issues early. Consider implementing techniques like gradient checkpointing to manage memory usage and mixed-precision training to improve efficiency.

For many use cases, alternatives to full fine-tuning may be more appropriate. Amazon Bedrock provides access to foundation models that support prompt engineering and few-shot learning. Parameter-efficient techniques like LoRA often provide sufficient performance improvements with significantly lower resource requirements. These can be implemented using Amazon SageMaker's training capabilities with substantially reduced computational overhead. Reserve full fine-tuning for scenarios where these lighter-weight approaches have been proven inadequate through testing and validation. As a rule of thumb, full fine-tuning is justified only when parameter-efficient methods hit a ceiling in performance or cannot adapt to domain-specific language distributions.

### Security Requirements

Security requirements form a core component of fine-tuning implementations. Use AWS IAM roles to control access to training resources and data. Implement encryption at rest using AWS KMS for sensitive training data and model artifacts. Network isolation is achieved using Amazon VPC configurations. Conduct regular security audits to enable compliance with organizational requirements and industry regulations.


## Get Hands-On

* AWS Blog: [Fast and cost-effective LLaMA 2 fine-tuning with AWS Trainium](https://aws.amazon.com/blogs/machine-learning/fast-and-cost-effective-llama-2-fine-tuning-with-aws-trainium/){:target="_blank" rel="noopener noreferrer"}
* AWS Samples: [Amazon Bedrock fine-tuning text summary deep dive blog source code](https://github.com/aws-samples/amazon-bedrock-samples/pull/114/files){:target="_blank" rel="noopener noreferrer"}

## Further Reading

* [Parameter-efficient fine-tuning (PEFT)](../2_3_4-2_PEFT(parameter%20efficient%20fine-tuning)/peft.md)
* [Preference Alignment](../2_3_4-3_Preference%20Alignment/preference_alignment.md)
* Academic research paper: [Full Parameter Fine-tuning for Large Language Models with Limited Resources](https://arxiv.org/abs/2306.09782){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Primary Author:** Wangechi Doble- Principal Technologist 

**Primary Reviewer:** Baishali Chaudhury - Applied Scientist II 