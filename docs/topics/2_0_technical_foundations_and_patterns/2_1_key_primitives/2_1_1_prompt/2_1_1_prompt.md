<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# The Input Interface - Prompts and common LLM Parameters

**Content Level: 300**



## Suggested Pre-Reading

- [Key Primitives](../index.md) 

## TL;DR

Prompts are the fundamental interface for communicating with LLMs, consisting of important components like instructions, context, examples, and constraints.
Combined with inference parameters (temperature, top_p, top_k) that control response randomness versus determinism, these elements form a powerful toolkit for shaping model behavior.
Effective prompt design significantly impacts both output quality and operational costs since most models charge based on token usage.
By strategically selecting parameters based on your use case—lower settings for factual tasks requiring consistency, higher for creative applications needing diversity—and implementing structured prompt templates, you can dramatically improve model performance.
Understanding these prompt fundamentals provides the foundation for implementing more advanced techniques like few-shot learning, chain-of-thought reasoning, and role-based prompting in production applications.

## The Input Interface - Prompts and common LLM Parameters

Prompts are the primary interface through which users and systems communicate with generative AI models.
A prompt is the input provided to the model that frames what is being asked and guides the model toward generating the desired output.
In its most basic form, the prompt describes the request to the LLM, but it can also contain additional information as text or binary information such as images.
Text-only LLMs only allow prompts to contain plain text. In contrast, multi-modal LLMs can also use audio, imagery or video in the prompt for processing.
[Section 2.2](../../2_2_types_of_generative_ai_models_and_capabilities/2_2_types_of_generative_ai_models_and_capabilities.md) provides further details on different types of models.
Besides the prompt, models also have different parameters.
While these vary from one LLM to another, there are three common ones that are generally supported by the majority of LLMs:

* **Temperature**: Controls randomness in the response generation. Lower values (near 0) make responses more deterministic and focused, while higher values (e.g., closer to 1) produce more diverse and creative outputs.
A temperature of 0 will consistently select the highest probability tokens, making responses more predictable.
* **Top_p**: Also known as nucleus sampling, this parameter determines the cumulative probability threshold for token selection. Typically, this value is from the range [0;1].
The model considers only the tokens whose combined probability mass reaches this threshold. Lower values (e.g., 0.5) restrict the model to higher probability tokens, while higher values (e.g., 0.9) allow more diversity.
* **Top_k**: Limits token selection to only the k most likely next tokens at each step. Typically, this is an integer value between 0 and 500.
A lower k value (e.g., 10) constrains the model to choose from fewer options, leading to more focused outputs, while higher values permit more variety.

These parameters allow developers to fine-tune the balance between deterministic responses and creative, diverse outputs depending on the specific application requirements. For tasks requiring high accuracy and factual correctness, lower temperature and more restrictive sampling settings are preferred. For creative applications like storytelling or ideation, higher values can yield more novel results.

### Anatomy of Effective Prompts

An effective prompt typically consists of several components:

* Context: Relevant background information to frame the request
* Instruction: The specific task or direction given to the model
* Examples: Sample inputs and outputs to guide the model (few-shot learning)
* Constraints: Limitations or requirements for the response format or content

Except for the instruction, all other parts of a prompt are optional, but the quality of the results will increase as these optional components are provided in the prompt. For example, a well-structured prompt might look like:

~~~
Context: You are a content specialist helping to create an email newsletter for a fitness company.
Instruction: Write a brief welcome section for new subscribers that introduces our monthly newsletter focusing on home workouts and nutrition tips.
Constraints: Keep it under 100 words, use a friendly tone, and include a clear call-to-action for readers to check out our website.
Example: For previous welcome sections, we've used this format:
"Welcome to the [Company] family! Each month, we'll deliver the latest fitness trends and practical tips straight to your inbox.
In this issue, we explore [topic 1] and [topic 2]. Ready to start your journey? Visit our resource library at [website] for more guidance."
~~~

The prompt above could be written without the sample welcome section that conveys basic information about the newsletter structure.
But if this information is missing, the likelihood of hallucinations will increase as the LLM will produce an output that is probable, but not necessarily aligned with the company's specific communication style and format.

### Prompt Engineering Techniques

Several approaches to prompt design have emerged as the field has evolved:

* Zero-shot prompting: Asking the model to perform a task without examples
* Few-shot prompting: Providing a small number of examples within the prompt
* Chain-of-thought prompting: Instructing the model to break down complex reasoning into steps
* System prompts: Initial instructions that set the behavior for the entire conversation
* Role-based prompts: Assigning a specific role to guide the model's perspective and expertise

The effectiveness of these techniques varies based on the model, task complexity, and specific requirements of your application.

## Making it practical
The way you craft prompts and configure model parameters directly impacts the performance, consistency, and cost-efficiency of your GenAI applications. When implementing LLMs in production environments, consider these practical aspects:

### Parameter Selection by Use Case

Different applications require different balancing of parameters:

- **Factual or deterministic tasks** (customer service, documentation generation, data extraction): Use lower temperature (0.0-0.3) and more restrictive top_p (0.5-0.7) settings to prioritize accuracy and consistency.
- **Creative tasks** (content generation, brainstorming): Use moderate to higher temperature (0.5-0.9) and less restrictive top_p (0.9-1.0) to encourage diverse outputs.
- **Hybrid applications** (conversational assistants): Consider a middle-ground approach (temperature 0.4-0.7) or dynamically adjust parameters based on the specific subtask being performed.

Remember that parameter adjustments fundamentally influence token selection probability, which affects both output quality and inference speed. Finding the right balance often requires experimentation with your specific use case.

### Prompt Design Considerations

When designing prompts for production applications:

- **Prompt length impacts costs**: Since most LLM providers charge by token count for both input and output, verbose prompts directly increase operational costs. Balance necessary context with conciseness.
- **Consistency requirements**: For enterprise applications requiring consistent outputs, combine structured prompts with lower temperature settings and example-based guidance (few-shot prompting).
- **Error handling**: Design your prompts to be robust against unexpected inputs. Include guidance on handling edge cases, unclear requests, or potentially problematic content.
- **Versioning**: Implement a versioning system for your prompts, especially for critical business processes. This enables A/B testing, auditing, and controlled updates.

### Testing and Iteration

Successful prompt engineering is an iterative process:

1. Start with a baseline prompt design
2. Test against diverse inputs representing real-world scenarios
3. Analyze failure modes and edge cases
4. Refine prompts to address identified weaknesses
5. Monitor performance in production environments

Consider implementing a prompt management system that allows for systematic testing, comparison, and optimization of prompts across different models and use cases.

### Integration with Application Architecture

Prompts don't exist in isolation—they're part of your broader application architecture:

- **Template systems**: Develop reusable prompt templates with placeholders for dynamic content
- **Parameter optimization**: Consider automated parameter tuning based on feedback or performance metrics
- **Fallback mechanisms**: Design graceful degradation paths when responses don't meet quality thresholds
- **Prompt chaining**: For complex tasks, break down problems into sub-prompts that build upon previous outputs

When working with AWS services like Bedrock, consider how prompt configuration interacts with other aspects like model selection, provisioned throughput, and streaming vs. non-streaming responses to optimize for your specific needs.

## Further Reading
- [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview){:target="_blank" rel="noopener noreferrer"}
- [AWS Prompt Engineering Best Practices](https://aws.amazon.com/blogs/machine-learning/prompt-engineering-techniques-and-best-practices-learn-by-doing-with-anthropics-claude-3-on-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}
- [Build generative AI applications with Amazon Bedrock Studio](https://aws.amazon.com/blogs/aws/build-generative-ai-applications-with-amazon-bedrock-studio-preview/){:target="_blank" rel="noopener noreferrer"}
- [Github: Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering){:target="_blank" rel="noopener noreferrer"}
- [Optimizing costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/){:target="_blank" rel="noopener noreferrer"}

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
