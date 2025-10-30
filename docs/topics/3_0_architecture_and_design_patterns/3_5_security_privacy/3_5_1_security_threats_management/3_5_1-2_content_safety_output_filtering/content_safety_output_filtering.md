<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Output Safety and Content Filtering

**Content Level: 200**

## Suggested Pre-reading

* [Detect and filter harmful content by using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html){:target="_blank" rel="noopener noreferrer"}
* [Components of a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html){:target="_blank" rel="noopener noreferrer"}

## TL;DR

The use of models in application stacks requires careful monitoring of outputs, as well as safety features to help ensure a high quality experience for end users. Some of these features include content filtering, toxicity detection, fact checking, output validation, redaction of sensitive information, intellectual property safeguards, and protections on training data. 

## Overview

The integration of AI models into application stacks requires safety measures and monitoring systems to protect user privacy and maintain the quality of model outputs. Content filtering employs algorithmic evaluation to prevent harmful or inappropriate content generation, essentially using one model to evaluate another's outputs for toxicity, hate speech, and policy violations. Fact checking and output validation aim to combat hallucinations and misinformation by comparing responses against information from reliable sources. Data privacy protections redact sensitive information like PII, PHI, financial data, and training data, all while preserving model functionality. These safety measures work together to enable responsible AI deployment while maintaining operational efficiency.

### Content filtering

Content filtering is a form of control that enable an AI model to provide outputs aligned with an organization's responsible AI and safety guidelines. Content filtering can take the form of using another model for toxicity detection, fact checking, and output validation (including consistency checks, hallucination detection, and automated reasoning). 

Toxicity detection employs specialized models to analyze and detect content that might be considered harmful. These models evaluate other models' outputs across different domains including hate speech, discrimination, and explicit content. The interaction between the model and the toxicity detection model amounts to an extra layer of safety to monitor the quality of the output. Fact checking provides another layer of safety in that it detects and prevents misinformation from reaching an end user. Fact-checking models function similarly to toxicity detection (in that it is a model evaluating another model), but the objective is to provide factual information by checking against verified sources. Finally, output validation helps to ensure response quality by using another model to monitor for consistency in the primary model's outputs, as well as using advanced analysis techniques to verify the soundness of a given models' reasoning. 

### Data privacy

In addition to the evaluation techniques employed by a comprehensive content filtering and safety control system to produce quality responses, data privacy measures encompass another layer of safety in AI systems. Just as a model can hallucinate and spread misinformation, a model can also output sensitive information when it is not intended. These controls encompass redaction of sensitive information like PII, PHI, and financial data. Data privacy also includes protection against generating content that resembles copyrighted intellectual property. 

Finally, protections can be incorporated into a stack that prevent leaking model training data into a model's output. For example, if we consider a language model trained on a dataset that includes PII, a privacy implementation might look like the following:

1. During training, the learning algorithm might add random noise to the gradients used to update the model's parameters. The amount of noise is controlled by a privacy budget, which balances data protection with model utility.
2. The model learns pattern recognition around personally identifiable data (or other sensitive data types), and consequently does not retain the specific details. The model learns to identify data that may have come from non-FM sources, like vector stores or data pulled from external systems through agents, and detect and reject, or obfuscate it at runtime.

In practice, when the model is asked to provide information about a topic, it will be able to do so without revealing identifiable data. 

### Guardrails 

Guardrails help ensure a model outputs content that is aligned with an organization's definition of what is appropriate. For example, a user attempting to generate instructions for certain harmful or illegal actions, might employ academic framing (or another one of the techniques discussed in [Prompt Injection and Jailbreaking](../3_5_1-1_prompt_injection_jailbreak/prompt_injection_jailbreak.md){:target="_blank" rel="noopener noreferrer"} to subtly guide the model toward producing a potentially harmful response. A model with well-defined guardrails may produce a response refusal, like this:

`I cannot and will not provide instructions for activities that may be harmful or illegal; however, I can suggest alternatives to your request that are safe and educational.`

When users persistently attempt to bypass guardrails in an AI application, the system will employ an escalating response mechanism designed to maintain security while preserving appropriate usage. An increment approach maintains a user-friendly tone while establishing clear boundaries around what is appropriate and what is not. For example, the first refusal may output as polite but firm, with a recommendation of safe alternatives. The refusals will increase in their firmness until the user receives a warning about abuse of the model, and possibly closing the user's session if the inappropriate prompts continue. This response system demonstrates how AI services can balance a user-friendly experience with security. Incremental refusals establish that responsible AI is not just a suggestion, but a requirement for continued use of the application. This approach of consistent communication of appropriate usage helps users understand their responsibilities when interacting with an AI model.

## Getting hands-on

Give guardrails a try in this [Guardrails for Amazon Bedrock workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/0720c7c4-fb23-4e43-aa9f-036fc07f46b2/en-US){:target="_blank" rel="noopener noreferrer"}

## Further reading

1. [AILuminate: Introducing v1.0 of the AI risk and reliability benchmark for MLCommons](https://arxiv.org/abs/2503.05731){:target="_blank" rel="noopener noreferrer"}
2. [Block harmful images with content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-mmfilter.html){:target="_blank" rel="noopener noreferrer"}
3. [Block harmful words and conversations with content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html){:target="_blank" rel="noopener noreferrer"}
4. [Build safe and responsible generative AI applications with guardrails](https://aws.amazon.com/blogs/machine-learning/build-safe-and-responsible-generative-ai-applications-with-guardrails/){:target="_blank" rel="noopener noreferrer"}
5. [Web content filtering through knowledge distillation of large language models](https://arxiv.org/abs/2305.05027){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author**

* Samantha Wylatowska - Solutions Architect 

**Reviewers**

* Alicja Kwasniewska - Senior Solutions Architect 

* Andrew Kane - GenAI Security/Compliance Lead 