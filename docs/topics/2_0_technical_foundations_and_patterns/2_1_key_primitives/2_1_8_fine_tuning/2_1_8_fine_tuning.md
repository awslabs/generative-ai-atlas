<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Fine-Tuning and Model Adaptation

**Content Level: 100**

## Suggested Pre-Reading

- [Key Primitives](../index.md)
- [Retrieval Augmented Generation (RAG)](../2_1_7_rag/2_1_7_rag.md)

## TL;DR

Fine-tuning adapts pre-trained language models for specific use cases by further training them on domain-specific datasets, requiring changes to the model itself unlike [RAG](../2_1_7_rag/2_1_7_rag.md) which leaves the model unchanged.
While approaches like Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), and Parameter-Efficient Fine-Tuning (PEFT) offer powerful customization options, they introduce increased operational complexity and costs.
Fine-tuning is best considered after first exploring prompt engineering and RAG, and is most appropriate when you need consistent response formatting, specialized domain knowledge that affects reasoning (beyond factual recall), reduced prompt complexity, or alignment with specific values.
Successful implementation requires high-quality training data (quality over quantity), robust infrastructure planning including versioning and evaluation frameworks, and careful cost-benefit analysis against alternatives.

## Fine-Tuning and Model Adaptation

Fine-tuning involves further training an existing model on a specific dataset to adapt it for particular use cases or to improve its performance on domain-specific tasks.
Contrary to RAG, fine-tuning will require changes to the LLM for customization and therefore maintaining as well as operating a customized version of an LLM.

### Types of Fine-tuning

Different approaches to fine-tuning include:

* Supervised fine-tuning (SFT): Training on example prompt-response pairs
* Reinforcement Learning from Human Feedback (RLHF): Optimizing models based on human feedback/preference.
* Parameter-Efficient Fine-Tuning (PEFT): Methods like LoRA (Low-Rank Adaptation) that fine-tune only a subset of model parameters

### When to Consider Fine-tuning

Fine-tuning may be appropriate when:

* Your application requires consistent formatting or response patterns
* You need specialized domain knowledge not covered in the base model
* You want to reduce prompt length and complexity for repeated tasks
* You need to align the model with specific values or guidelines

However, fine-tuning comes with increased operational complexity and costs compared to prompt engineering, requiring careful evaluation of the trade-offs.

## Making it practical
When evaluating whether to fine-tune a model or use an alternative approach such as [RAG](../2_1_7_rag/2_1_7_rag.md), consider this practical decision framework:

1. **Start with prompt engineering**: For most use cases, well-crafted prompts with a capable foundation model can deliver good results with minimal investment. Only pursue fine-tuning when prompt engineering cannot meet your requirements.

2. **Consider RAG next**: If your use case primarily requires adding specific knowledge or data to responses, Retrieval Augmented Generation (RAG) typically provides a more maintainable and cost-effective solution than fine-tuning.

3. **Choose fine-tuning when**:
   - Your application requires consistent response formats or patterns across many similar interactions
   - You need specialized domain knowledge that affects the model's reasoning (not just factual recall)
   - You want to reduce latency and token usage by eliminating complex prompting patterns
   - Your use case requires alignment with specific values or guidelines that prompt engineering cannot reliably enforce

### Implementation Considerations

When implementing fine-tuning for production environments:

#### Data Requirements
- **Quality matters more than quantity**: 100-1,000 high-quality examples often outperform larger datasets of lower quality
- For Supervised Fine-Tuning (SFT), aim for carefully crafted instruction-response pairs that demonstrate the exact behavior you want
- For RLHF, you'll need both example outputs and comparative preference data about which outputs are better
- Examples should cover the full spectrum of expected inputs and edge cases

#### Infrastructure Planning
- **Version control**: Implement rigorous versioning for both training data and fine-tuned models
- **Evaluation framework**: Develop metrics and test sets to objectively measure improvements
- **Production deployment**: Plan for model serving, monitoring, and updating processes

#### Cost-Benefit Analysis
Fine-tuning typically involves:
  - Upfront costs: Computing resources for training
  - Operational costs: Hosting, maintaining, and updating custom models
  - Potential savings: Reduced token usage from shorter prompts, improved accuracy
  
  Compare these costs against alternatives like complex prompting or RAG implementations.

### Practical Approaches by Use Case

1. **For response formatting standardization**:
   - Start with SFT using 100-200 examples showing the exact output format
   - Focus training data on covering different edge cases rather than repetitive examples

2. **For domain-specific knowledge**:
   - Consider PEFT methods like LoRA to efficiently adapt models to your domain
   - Start with domain adaptation on relevant texts before instruction tuning

3. **For reducing complex prompts**:
   - Identify your most common prompt patterns
   - Create training data that demonstrates how to respond to simplified versions of these prompts

4. **For value alignment**:
   - RLHF approaches are typically more effective than SFT alone
   - Build training data that explicitly demonstrates the values and behaviors you want

Remember that fine-tuned models require ongoing maintenance and evaluation. As your use cases evolve or the model's performance drifts, you'll need to update your training data and potentially retrain your models.

## Further Reading
- [Customize models in Amazon Bedrock with your own data using fine-tuning and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/){:target="_blank" rel="noopener noreferrer"}
- [Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment](https://arxiv.org/abs/2312.12148){:target="_blank" rel="noopener noreferrer"}
- [Incorporate offline and online human – machine workflows into your generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/incorporate-offline-and-online-human-machine-workflows-into-your-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}

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
