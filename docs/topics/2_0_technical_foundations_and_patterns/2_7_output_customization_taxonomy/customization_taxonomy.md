<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Generative AI Customization Decision Taxonomy

**Content Level: 300**

## Suggested Pre-Reading

- [Introduction to Large Language Models](../../1_0_generative_ai_fundamentals/1_1_core_concepts_and_terminology/core_concepts_and_terminology.md)
- [Prompt Engineering Foundations](../2_3_core_archtectural_concepts/2_3_2_prompt_engineering/index.md)
- [Retrieval-Augmented Generation (RAG)](../2_1_key_primitives/2_1_7_rag/2_1_7_rag.md)
- [Fine-tuning Fundamentals](../2_3_core_archtectural_concepts/2_3_4_fine-tuning/fine_tuning.md)

## TL;DR

Customizing generative AI requires selecting the right approach based on your specific goals, available resources, and performance requirements.
The taxonomy in this section provides a structured framework for choosing among prompt engineering (lowest complexity, minimal data needs), retrieval-augmented generation (medium complexity, requires document corpus), fine-tuning (higher complexity, requires examples), custom model development (highest complexity, requires extensive data), and orchestration (combines models and tools).
The decision framework guides you through key questions about technical resources, factual accuracy needs, data availability, computational constraints, and specialized capabilities to determine the most appropriate customization approach.
Most successful implementations start with simpler techniques and progressively incorporate more sophisticated approaches as requirements and capabilities evolve.

## Generative AI Customization Decision Taxonomy

Generative AI customization exists on a spectrum from simple to complex, with each approach offering specific advantages, limitations, and resource requirements.
Understanding this spectrum helps organizations make informed decisions about which methods to employ based on their unique circumstances.
The five primary customization approaches (from simplest to most complex) include:

1. **Prompt Engineering**: Modifying instructions to the model without changing its parameters
2. **Retrieval-Augmented Generation (RAG)**: Enhancing model responses with external knowledge sources
3. **Fine-tuning**: Adapting pre-trained model parameters for specific domains or tasks
4. **Custom Model Development**: Building specialized models from scratch or through extensive transfer learning
5. **Orchestration**: Coordinating multiple models and tools in complex workflows

Each approach represents a significant step-up in implementation complexity, resource requirements, and potential performance gains for specific use cases.
While previous sections have discussed technical details about these approaches, this section focuses on a decision-making framework to outline how to choose between these approaches under different circumstances.

### Customization Methods Overview

#### A. Prompt Engineering
**Light-touch customization without model modification**

| Method | Description | Complexity | Data Needs |
|--------|-------------|------------|------------|
| Zero-shot Prompting | Direct instructions without examples | Low | None |
| Few-shot Prompting | Including examples in the prompt | Low | Few examples |
| Chain-of-Thought | Guiding reasoning process through prompting | Medium | None-Few |
| System Instructions | Setting context and role definitions | Low | None |
| Format Specification | Explicitly defining output structure | Low | None |

Prompt engineering is ideal for quick iteration and deployment, especially when technical resources are limited or when using API-only models without access to weights.
However, it has limitations in consistency, efficiency with token usage, and handling complex domain-specific knowledge.
A deeper and broader introduction to prompt engineering is in the Section [Prompt Engineering](../2_3_core_archtectural_concepts/2_3_2_prompt_engineering/index.md).

#### B. Retrieval-Augmented Generation (RAG)
**Enhancing generation with external knowledge**

| Method | Description | Complexity | Data Needs |
|--------|-------------|------------|------------|
| Basic RAG | Simple retrieval + generation pipeline | Medium | Document corpus |
| Hybrid Search | Combining keyword and semantic search | Medium | Document corpus |
| Multi-step RAG | Iterative retrieval and generation | High | Document corpus |
| Adaptive RAG | Dynamic retrieval strategy selection | High | Document corpus |

RAG is particularly valuable when information changes frequently, accuracy is critical, or when your knowledge base is too large to encode in the model context.
It also provides transparency and traceability in how information is sourced and allows incorporation of proprietary data without exposing it in training.

#### C. Fine-tuning
**Adapting pre-trained models to specific domains/tasks**

| Method | Description | Complexity | Data Needs |
|--------|-------------|------------|------------|
| Full Fine-tuning | Updating all model parameters | Very High | 1000s+ examples |
| PEFT (Parameter-Efficient) | Updating select parameters | High | 100s-1000s examples |
| LoRA (Low-Rank Adaptation) | Low-rank adaptation of weights | Medium-High | 100s-1000s examples |
| QLoRA | Quantized version for efficiency | Medium | 100s-1000s examples |s

Fine-tuning becomes appropriate when prompt engineering yields insufficient results, you need consistent behavior across similar inputs, or when you have domain-specific terminology to integrate.
It requires sufficient high-quality training data and accepts longer development time for better results.
Compared to RAG, it reduces the operational cost of running a vector database.

#### D. Custom Model Development
**Building specialized generative solutions**

| Method | Description | Complexity | Data Needs |
|--------|-------------|------------|------------|
| Training from Scratch | Building a model from beginning | Extreme    | Millions of examples |
| Transfer Learning | Starting from pre-trained foundation | Very High  | 10,000+ examples |
| Distillation | Creating smaller model from larger one | Medium     | Large dataset + teacher model |
| Domain-Specific Architecture | Custom architecture for specific use | Very High  | Varies |

This approach is reserved for cases requiring complete control over model architecture, when dealing with massive amounts of domain-specific data, or when intellectual property concerns require fully proprietary models.

#### E. Orchestration
**Coordinating multiple models and tools**

| Method | Description | Complexity | Data Needs |
|--------|-------------|------------|------------|
| Agent Frameworks | Self-directing AI systems | High | Varies |
| Tool Integration | Connecting AI with external tools | Medium | Tool documentation |
| Multi-model Pipelines | Chaining specialized models | High | Integration data |
| Planning Systems | Models that create and execute plans | High | Few-many examples |

Orchestration is necessary when single model capabilities are insufficient, tasks require complex multistep workflows, or when your application needs to integrate with multiple external tools or APIs.
For instance, when your Generative AI application requires retrieval of information from a ticketing system, an API and various other online resources, the orchestration of this retrieval and coordination of the results is required.

### Resource Requirement Comparison

Understanding the resource implications of each approach helps organizations plan effectively and higher resource requirements drives development cost:

| Approach | Development Time | Technical Expertise | Computational Resources | Data Requirements |
|----------|------------------|---------------------|-------------------------|-------------------|
| Prompt Engineering | Hours-Days | Low-Medium | Minimal | None-Few examples |
| RAG | Days-Weeks | Medium | Medium | Document corpus |
| Fine-tuning (LoRA) | Days-Weeks | Medium-High | Medium-High | 100s-1000s examples |
| Full Fine-tuning | Weeks | High | Very High | 1000s+ examples |
| Custom Development | Months | Very High | Extreme | 10,000s+ examples |
| Orchestration | Weeks | High | Varies | Varies |

## Prescriptive Decision Framework

When implementing generative AI solutions, use this decision framework to determine which customization approach(es) will best meet your requirements:

### Step 1: Evaluate Technical and Resource Constraints

First, assess your practical limitations:

- **If you have minimal AI expertise (team with limited ML experience):**
  - Begin with prompt engineering
  - Consider managed RAG solutions if you need factual knowledge integration

- **If you have moderate AI expertise (team with some ML experience):**
  - Consider RAG and parameter-efficient fine-tuning (LoRA/QLoRA)
  - Evaluate orchestration for multi-step workflows

- **If you have strong AI expertise (dedicated ML engineers):**
  - All approaches are viable; select based on requirements in steps 2-3

- **If you have limited computational resources:**
  - Avoid full fine-tuning and custom model development
  - Prioritize prompt engineering, RAG, and parameter-efficient methods (QLoRA)

- **If you have significant time constraints (need solution in <2 weeks):**
  - Implement prompt engineering immediately
  - Add basic RAG if knowledge integration is important

### Step 2: Identify Primary Performance Requirements

Next, determine your most critical performance needs:

- **If factual accuracy and up-to-date information are most critical:**
  - Implement RAG as your foundation
  - Combine with prompt engineering for formatting/style guidance
  
- **If consistent response style, tone, and format are most critical:**
  - Implement fine-tuning if you have 100+ high-quality examples
  - Otherwise, use extensive prompt engineering with system instructions

- **If domain-specific terminology and knowledge are most critical:**
  - If you have 500+ domain examples: Use LoRA fine-tuning
  - If you have extensive documents but few examples: Implement RAG
  - If you have neither: Use few-shot prompting with domain examples

- **If task complexity and multi-step reasoning are most critical:**
  - Begin with chain-of-thought prompting
  - If unsatisfactory, implement orchestration with specialized components

- **If cost efficiency at scale is most critical:**
  - Fine-tune smaller models rather than using larger ones with complex prompts
  - Consider distillation if deploying at very high volume

### Step 3: Apply Differentiated Strategy Based on Available Data

Finally, refine your approach based on available data.
In the following, we refer to examples as an input-output pair that sets a baseline of what is expected, i.e., at least an input prompt with the corresponding/desired output of the Generative AI solution.

- **If you have 0-10 examples of desired outputs:**
  - Use prompt engineering exclusively (zero/few-shot methods)

- **If you have 10-100 high-quality examples:**
  - Use few-shot prompting and template creation
  - Consider experimenting with QLoRA on models with few parameters

- **If you have 100-1000 high-quality examples:**
  - Use LoRA/QLoRA fine-tuning on appropriately sized models
  - Consider combining with RAG for knowledge integration

- **If you have 1000+ high-quality examples:**
  - Full fine-tuning becomes viable (if you have computational resources)
  - Consider model distillation for deployment efficiency

- **If you have a large document corpus but few examples:**
  - Implement RAG as your primary approach
  - Use prompt engineering to guide the RAG system behavior

- **If you have specialized use cases no existing model handles well:**
  - Only pursue custom model development if you have:
    - 10,000+ relevant examples
    - Necessary technical expertise
    - Significant computational resources
    - Time for extended development cycles

### Step 4: Implementation Roadmap

For most use cases, follow this phased implementation approach:

1. **Phase 1 (Weeks 1-2):**
   - Select a foundational model for starting the work, continuously evaluate this choice.
   - Implement baseline solution using prompt engineering
   - Assess performance gaps and prioritize improvements

2. **Phase 2 (Weeks 3-6):**
   - Add RAG if knowledge integration is needed
   - Begin collecting/preparing data for fine-tuning if needed

3. **Phase 3 (Weeks 7-12):**
   - Implement fine-tuning for consistent style/behavior
   - Develop orchestration components for complex workflows

4. **Phase 4 (Ongoing):**
   - Continuously evaluate performance
   - Collect user feedback and new examples
   - Refine approaches based on evolving requirements

## Making it Practical

When building generative AI applications, the choice of customization approach directly impacts development time, resource requirements, and system performance. Here's how to apply this taxonomy to real-world scenarios:

### Progressive Implementation Examples

Real-world implementations often layer multiple approaches, starting simple and adding complexity as needed:

1. **Customer Support Solution**
   - **Initial**: Prompt engineering with role instructions and format specifications
   - **Enhance**: Add RAG with company documentation, policies, and FAQs
   - **Optimize**: Fine-tune with historical support conversations for consistent tone and handling of common scenarios
   - **Extend**: Add orchestration with ticketing systems, CRM access, and human escalation

2. **Legal Document Analysis**
   - **Initial**: Prompt engineering with specialized legal instructions
   - **Enhance**: RAG with relevant case law and regulatory documents
   - **Optimize**: Fine-tune with expert-reviewed legal analyses
   - **Extend**: Orchestrate with document processing tools and verification workflows

3. **Product Recommendation Engine**
   - **Initial**: Prompt engineering for recommendation formats
   - **Enhance**: RAG with product catalog and customer reviews
   - **Optimize**: Fine-tune with successful recommendation patterns
   - **Extend**: Orchestrate with inventory systems and personalization models

This progressive approach allows organizations to balance immediate needs with long-term goals, allocating resources efficiently while continuously improving capabilities.

### Key Considerations for Implementation

- **Start simple**: Always begin with prompt engineering to establish a baseline before moving to more complex solutions
- **Focus on data quality**: The success of RAG and fine-tuning depends heavily on the quality of your document corpus or training examples
- **Balance specialization and generality**: Highly specialized models excel at narrow tasks but may perform poorly on everything else
- **Consider hybrid approaches**: Most production systems combine multiple customization techniques
- **Plan for maintenance**: More complex customization approaches require ongoing updates and monitoring.
- **Plan for Model Evolution**: Foundational models are frequently updated and new models are frequently released. Any solution should be able to change the foundational model without a lot of engineering work. 
- **Measure improvements**: Track key performance metrics to validate that each new customization layer delivers meaningful benefits

### Industry-Specific Considerations

Different industries have unique needs that influence customization decisions:

- **Healthcare**: Prioritize RAG for up-to-date medical knowledge and compliance, with careful fine-tuning for consistent terminology
- **Financial Services**: Use RAG for current regulations and orchestration for multistep compliance workflows
- **Retail**: Combine prompt engineering for customer interactions with fine-tuned recommendation engines
- **Manufacturing**: Implement RAG for technical documentation and orchestration for process workflows
- **Legal**: RAG for case law and fine-tuning for jurisdiction-specific language and format requirements

By understanding the strengths and limitations of each customization approach, organizations can build a roadmap that delivers immediate value while establishing the foundation for more sophisticated capabilities as needs evolve.

## Get Hands-On

- [Bedrock Model Customization Workshop Notebooks](https://github.com/aws-samples/amazon-bedrock-customization-workshop){:target="_blank" rel="noopener noreferrer"}
- [Fine-tune Llama 3 models on SageMaker JumpStart](https://github.com/aws/amazon-sagemaker-examples/blob/default/%20%20%20%20generative_ai/sm-jumpstart_foundation_llama_3_finetuning.ipynb){:target="_blank" rel="noopener noreferrer"}
- [RAG Application using AWS Bedrock and LangChain](https://dev.to/aws-builders/rag-application-using-aws-bedrock-and-langchain-140b){:target="_blank" rel="noopener noreferrer"}
- [Workshop: Innovate on enterprise data with generative AI & Amazon Q Business application](https://catalog.workshops.aws/amazon-q-business/en-US){:target="_blank" rel="noopener noreferrer"}

## Further Reading

- [Parameter-Efficient Fine-Tuning Methods](https://arxiv.org/abs/2312.12148){:target="_blank" rel="noopener noreferrer"}
- [LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation){:target="_blank" rel="noopener noreferrer"}
- [Best practices to build generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/best-practices-to-build-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}

## Contributors

Author/s:

 - Markus Bestehorn - Tech Lead Generative AI EMEA 

Primary Reviewers:

 - Yibo Liang - Generative AI Specialist SA 
 - Andrew Hood - Head of Program Development 

Additional Reviewer/s: 

 - Ana-Maria Olaru - Sr. Program Manager 
 - Emily Ransley - Generative AI Specialist SA 
 - Michael Gerrity - CSM Snr. Leader Germany 
 - Christoph Schniedrig - Head Of Technology 
 - Arlind Nocaj - Sr. GTM SSA AIML GenAI 
