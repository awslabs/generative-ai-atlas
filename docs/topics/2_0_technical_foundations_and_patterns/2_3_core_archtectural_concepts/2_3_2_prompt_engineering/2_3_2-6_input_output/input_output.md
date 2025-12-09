<!--
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Input/Output Relationships

**Content Level: 200**

## TL;DR

Understanding how prompts affect model outputs is important for building reliable AI systems. Well-designed prompts work like agreements between system parts, using clear structure and instructions to get consistent results. Amazon Bedrock helps you test these prompts using both automatic measurements and AI-based evaluation—where another AI judges the quality, relevance, and accuracy of responses.

## Introduction

As large language models (LLMs) become more common in business applications, the connection between what we input (prompts) and what we get back (outputs) is important for building reliable AI systems.

Business systems need predictable results that work reliably in real-world situations. When companies use LLMs for important tasks like analyzing financial data, helping with healthcare decisions, or processing legal documents, any unexpected changes in the outputs can cause serious problems. Companies investing large amounts of money in AI technology need systems that behave predictably and produce appropriate responses, despite the inherently non-deterministic nature of LLMs.

Several issues should be considered when seeking consistent results from LLMs. First, the companies that create these models frequently update them, which can change how they respond to the same prompts. Second, settings like temperature and sampling parameters control how creative or focused the model's responses will be, and these need careful adjustment for each business use. Third, limits on how much information can be processed at once force engineers to make careful decisions about what to include in prompts. Finally, since many commercial models are black box, careful testing methods have to be developed.

## Output Control

As discussed earlier, parameters such as temperature and top-k/p control how deterministic the model's output is. When tuning these parameters, it's generally recommended to adjust one at a time during testing to understand each parameter's individual effect, though they can be used together in production once you understand their interaction.

There are also parameters for controlling the length and content of generated text. The max length parameter controls the number of output tokens, preventing the model from generating long, irrelevant outputs that increase costs.

Another parameter is a stop sequence. This parameter indicates a string that stops the model from generating more tokens. In this way, you can control what is being generated based on the content, not on the length of responses. For example, you can tell the model to generate a list with a specific number of items, by using N as a stop word.

Frequency and presence penalties help reduce repetitive words. Frequency penalty reduces repetition based on how often a token appears in the response. Presence penalty works similarly but applies the same penalty to any repeated word, regardless of how frequently it appears. While both can be used together, it's often better to start with one penalty type during testing to avoid over-constraining the model, which can lead to unnatural or overly rigid text.


## Core Mathematical Framework

Understanding prompt engineering through a mathematical lens helps engineers build more reliable and predictable AI systems. This framework provides a precise way to think about how different prompt designs affect model behavior, enabling systematic optimization rather than trial-and-error approaches. It also helps teams communicate about prompt engineering decisions and establish consistent practices across projects.

To understand prompt engineering at a formal level, we need a mathematical framework that precisely describes how prompts transform inputs into outputs. Think of this as creating a "recipe" that describes exactly how different ingredients (prompts, inputs, model parameters) combine to produce outputs.

**Basic Components:**

- *X*: All possible user questions or inputs

- *Y*: All possible model responses

- *V*: The model's vocabulary (all words/tokens it knows)

- *P*: A prompt function that takes user input and creates a structured prompt

- *f*: The language model itself

- *g*: A way to measure how good the output is

### Types of Prompts

Prompts can be categorized into three main types, each with different characteristics and use cases:

1. **Text-based prompts** (Discrete): Regular language prompts
2. **Embedding-based prompts** (Continuous): Mathematical representations
3. **Combined prompts** (Hybrid): Mix of both approaches

#### Text-Based Prompts

These are the standard prompts written in natural language that most practitioners use. They follow predictable patterns:

1. **Zero-shot prompts**: Instructions + user question
    - Format: [Instructions, Reasoning approach; User question]
2. **Few-shot prompts**: Instructions + examples + user question
    - Format: [Instructions, Reasoning approach, Example 1, Example 2, ...; User question]

The key insight is that effective prompts have consistent structure: they set context (I), explain the thinking process (T), and may include examples (e) before presenting the actual question.

**Zero-shot Example:**

- I = "You are a math tutor helping students solve algebra problems."

- T = "I should solve this step by step, explaining each operation clearly."

- x = "Solve the equation: 2x + 5 = 15"

**Few-shot Example:**

- I = "Classify the sentiment of the following text as positive, negative, or neutral."

- T = "I should analyze the emotional tone and word choices."

- e₁ = ("This movie was amazing!", "Positive")

- e₂ = ("I didn't enjoy the service at all.", "Negative")

- x = "The food was okay but the ambiance was great."

#### Embedding-Based Prompts

Instead of using words, these prompts work with mathematical representations (embeddings) that capture meaning in numerical form. This approach is primarily used in research and specialized applications where prompts can be automatically optimized.

- The user input gets converted to numbers that represent its meaning
- Special learned vectors are combined with this numerical representation
- This allows for automatic optimization of prompts without human intervention

#### Combined Prompts

These prompts mix regular text instructions with mathematical representations, allowing both human-readable instructions and automatic optimization. This approach combines the interpretability of text prompts with the optimization potential of embedding-based methods.

### Finding the Best Prompt

Prompt optimization means systematically finding the prompt that works best for your specific task. The mathematical way to think about this is:

**Goal**: Find the prompt that gives the highest average performance across all your test cases.

**Process**:
1. Define what "good performance" means for your task (accuracy, relevance, etc.)
2. Test different prompt variations on a validation dataset
3. Measure performance using your chosen metrics
4. Select the prompt that performs best on average

This systematic approach replaces guesswork with data-driven prompt improvement, leading to more reliable AI systems in production.

## Advanced Prompt Templates as Contract Specifications

In production environments, the abstract notion of a prompt function should be concretized into templates to reduce ambiguity in input-output behavior. These templates serve as explicit contracts between different components of an AI system.

### Template Design Principles

For a template to function as a reliable contract, it should adhere to several key design principles:

1. **Clear Structure**: Templates should clearly separate their different parts
2. **Clear Variable Handling**: All variable elements should be explicitly parameterized (any part that can change should be marked as a placeholder). For example, instead of "Analyze the sentiment of this customer review about our product", use "Analyze the sentiment of this {content_type} about {subject}: {input_text}" so you can reuse the template with different values
3. **Output Schema Enforcement**: Templates should include explicit output format specifications
4. **Failure Mode Handling**: Templates should include instructions for handling edge cases

```json
EXTRACTION_TEMPLATE = """
Given the following text, extract the specified entities in valid JSON format:

Text: {input_text}

Extract the following entities:
- Person names
- Organizations
- Locations
- Dates

Response must conform to this exact JSON schema:
{
  "type": "object",
  "properties": {
    "people": {"type": "array", "items": {"type": "string"}},
    "organizations": {"type": "array", "items": {"type": "string"}},
    "locations": {"type": "array", "items": {"type": "string"}},
    "dates": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["people", "organizations", "locations", "dates"]
}
"""
```

### How Prompt Templates Improve Consistency

1. **Structure and Expectations**: A fixed format reduces ambiguity for the model, leading to more predictable outputs
2. **Context Control**: Templates help ensure all required instructions or system context are always present
3. **Mitigation of Drift**: In production inference, prompt templates prevent variance caused by ad hoc prompts


### Template Limitations

1. **Determinism**: If randomness (e.g., temperature > 0) is used, even a consistent template won't yield identical results
2. **Complete Coverage of Edge Cases**: Templates might not handle ambiguous or adversarial inputs
3. **Model Drift**: Templates don't protect against changes in underlying model behavior over time

## Amazon Bedrock Prompt Evaluation

Amazon Bedrock offers a sophisticated approach to prompt evaluation through its "LLM-as-a-judge" methodology, which transforms the inherently subjective task of assessing prompt quality into a quantifiable process. This evaluation framework allows organizations to systematically measure both prompt effectiveness and the quality of generated responses against predefined criteria.

### LLM-as-Judge vs. Programmatic Evaluation

Unlike programmatic evaluation that relies on rigid, predefined metrics, LLM-as-judge evaluation employs another language model to make nuanced, holistic assessments of responses based on complex criteria such as contextual relevance, reasoning quality, and factual accuracy.

**Sample Evaluation Template:**
```
You are a prompt evaluation specialist assessing the quality of AI-generated content.
Review the prompt in the [PROMPT] tags and the response in the [RESPONSE] tags according to these evaluation criteria:

[PROMPT]
{{input}}
[/PROMPT]

[RESPONSE]
{{output}}
[/RESPONSE]

[PROMPT_EVALUATION_CRITERIA]
• Clarity and specificity of instructions
• Contextual information and background provided
• Role assignment or perspective framing
• Format and structure guidance
• Examples or demonstrations included
[/PROMPT_EVALUATION_CRITERIA]

[RESPONSE_EVALUATION_CRITERIA]
• Factual accuracy and technical correctness
• Relevance to the original prompt
• Structure and organization of information
• Absence of fabricated information
• Grammar and readability
[/RESPONSE_EVALUATION_CRITERIA]

Provide your evaluation in JSON format with the following structure:
{
"response_quality_score": [0-100 score],
"prompt_quality_score": [0-100 score],
"evaluation_rationale": [analysis of strengths and weaknesses],
"prompt_text": [original prompt content],
"response_text": [model response content],
"improvement_suggestions": [specific recommendations to enhance prompt effectiveness]
}

Return only the JSON object without additional commentary.
```

### Amazon Bedrock Programmatic Evaluation

Amazon Bedrock offers a structured approach to model evaluation through specialized task types that align with common AI applications:

- **General text generation**
- **Text summarization**
- **Question and answer**
- **Text classification**


## Error Handling

**Definition:** Error handling refers to the techniques and strategies used to identify, manage, and mitigate errors that occur during the processing of inputs and generation of outputs by the model.

**Common Errors:**
- **Out-of-Vocabulary (OOV) Words**: Words not present in the model's vocabulary
- **Hallucinations**: Incorrect or fabricated information generated by the model
- **Incoherent Responses**: Outputs that lack logical consistency or relevance

**Strategies for Error Handling:**
- **Input Validation**: Ensuring inputs are within expected format and range
- **Output Filtering**: Post-processing model outputs to remove or correct errors
- **Fallback Mechanisms**: Providing alternative responses when the model fails
- **User Feedback**: Incorporating feedback to continuously improve error handling
- **Guardrails**: Implementing predefined rules to prevent harmful content

## Making it Practical

### Common Pitfalls and Best Practices

#### Iterative Refinement
Most effective prompts evolve through multiple iterations. Don't settle for the first attempt. Keep seed constant and test various formulations and analyze the differences in outputs.

#### Leverage Open-Ended Interactions
Generative AI systems excel with exploratory, open-ended prompts rather than closed questions. Instead of "What is the capital of France?", try "Explain the historical significance of Paris becoming France's capital and how it shaped the country's development".

#### Parameter Tuning
Adjust output parameters strategically based on your goals:
- Lower temperature (0.1-0.4): For factual responses, code generation, or structured data
- Medium temperature (0.5-0.7): For balanced creativity and accuracy in content creation
- Higher temperature (0.8-1.0): For brainstorming, creative writing, or generating diverse alternatives

#### Model-Specific Optimization
Different AI systems have unique training backgrounds and capabilities. Tailor your approach accordingly:
- Research which models excel at your specific task type
- Adjust level of detail and terminology based on model strengths
- Consider specialized models for technical domains or creative applications

#### Critical Evaluation
Always verify model outputs, particularly for factual content. Be vigilant for:
- Hallucinations (plausible but incorrect information)
- Outdated knowledge based on training cutoff dates
- Logical inconsistencies or contradictions within responses
- Subtle biases or incomplete perspectives on complex topics

#### Best Practices for Using Prompt Templates in Inference
1. Combine with low temperature (e.g., temperature=0.0) for higher consistency
2. Test on diverse inputs to evaluate template robustness
3. Use prompt chaining for complex tasks
4. Store prompt versions for auditability and regression testing

!!! note "Important: While continuous and hybrid prompts offer powerful mechanisms for fine-tuned control, Amazon Bedrock does not currently support them. Amazon Bedrock users must rely on discrete, text-based prompts, which aligns with enterprise needs for transparency and interpretability."

## Further Reading

- [Building Guardrails for Large Language Models](https://arxiv.org/abs/2402.01822){:target="_blank" rel="noopener noreferrer"}
- [A Stitch in Time Saves Nine: Detecting and Mitigating Hallucinations of LLMs by Validating Low-Confidence Generation](https://arxiv.org/abs/2307.03987){:target="_blank" rel="noopener noreferrer"}
- [Evaluating prompts at scale with Prompt Management and Prompt Flows for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/evaluating-prompts-at-scale-with-prompt-management-and-prompt-flows-for-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}
- [Amazon Bedrock's LLM-as-Judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html){:target="_blank" rel="noopener noreferrer"}
- [Amazon Bedrock Evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks.html){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author/s:**

* Alicja Kwasniewska - Sr Solution Architect 

**Primary Reviewer:**

* Deepika Kumar - Solution Architect 

**Additional Reviewer:**

* Afia Khan - Associate SA - GenAI 

* Kihyeon Myung - Sr Applied AI Architect 