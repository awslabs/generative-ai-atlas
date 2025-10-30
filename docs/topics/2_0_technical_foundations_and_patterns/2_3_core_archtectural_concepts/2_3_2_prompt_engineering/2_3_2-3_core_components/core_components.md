<!--
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Core Prompt Components

**Content Level: 200**


## TL;DR

When crafting prompts for AI systems, three key components work together: System Messages establish the model's persona and behavioral framework, User Inputs deliver specific tasks or queries, and Reference Data supplies relevant context and information. Balancing these components effectively results in responses that are accurate, contextually appropriate, and aligned with intended guidelines.

Amazon Bedrock offers two primary interaction methods: (1) single-prompt invocation via InvokeModel (with InvokeModelWithResponseStream for streaming), which requires model-specific formatting for system instructions and works best for discrete tasks; and (2) conversational exchanges via Converse API (with ConverseStream for streaming), which provides a standardized interface across all models with explicit parameters for system messages and conversation history. The Converse API offers advantages including model independence, standardized request formats, and simplified tool integration, making multi-turn applications more maintainable and future-proof.

## System Messages

System messages (also often referred to as system prompts) are high-level instructions setting the overarching tone, style, or policy for the AI. In many modern chat-based frameworks, the system message is inserted at the start of the conversation and has priority over user messages. In professional or production contexts, system messages are frequently locked, so end-users of consumer-facing LLM applications cannot edit them. This helps the foundational rules remain in place.

System messages often clarify the LLM's role ("You are a helpful writing assistant."), outline the boundaries of acceptable behavior ("Do not provide disallowed content."), and specify the model's fundamental style ("Respond politely and concisely."). Because these messages stay active throughout the conversation, they help to guide every response the AI gives.

### Setting Context and Persona

The system message serves as a global instruction set for the model, establishing its operating parameters, persona, and constraints. This component is particularly powerful for controlling response characteristics without cluttering individual user queries:

```python
# Example system message components
system_message = '''You are a culinary expert specializing in restaurant reviews.
Your task is to provide balanced, informative summaries of dining experiences.
Focus on food quality, service, ambiance, and value.
Always maintain a professional tone and avoid hyperbole.
You must preserve the exact restaurant names as provided with NO modifications.'''
```

System messages influence all subsequent interactions, creating a consistent behavioral framework that persists throughout the conversation. They're ideal for:

- Defining expertise domains and specialized roles
- Establishing tone and communication style
- Setting constraints on response formats
- Defining responsible AI dimensions and usage limitations

## User Inputs

User inputs serve as the immediate prompts or questions posed to a language model. These inputs contain instructions about the desired task, any constraints or formatting requirements, and can include examples to guide the model's reasoning or style. Effective prompt design typically includes clearly labeled sections (such as "Task," "Constraints," "Format") paired with appropriate demonstrations when needed.

Clarity and specificity in prompts generally produce more accurate results. The approach to positive and negative instructions varies by model type. For text-to-image models, including what should be generated in the main prompt while placing restrictions in a separate negative prompt parameter often works best. For text-to-text models, incorporating both what to do and what to avoid can be beneficial. However, these practices vary by specific use case and model, so experimentation and thorough evaluation through programmatic methods, LLM-as-judge assessments, and human evaluation when applicable is strongly recommended.

For complex tasks, breaking the input into smaller steps or explicitly instructing the model to reason methodically can improve results. This technique, known as chain-of-thought prompting, guides the model through a structured thinking process. Additionally, providing examples within the user prompt (one-shot or few-shot prompting) can substantially enhance outcomes, particularly for complex or specialized tasks.

Refining user inputs is inherently iterative. When responses don't meet expectations, revising the prompt by adding constraints, clarifying instructions, or including relevant context can help steer the model toward better outputs in subsequent interactions.

It's important to note that some applications may function without direct user input (such as automated report generation or scheduled content creation), or might combine user prompts with other elements of prompt templates. Regardless of approach, validating user input is important to control token usage and ensure appropriate behavior.

### Specifying Tasks and Queries

User messages contain the specific instructions, questions, or content that the model needs to process. These components focus on communicating the immediate task rather than general behavior:

```python
# Example user message structure
user_message = {
    "role": "user",
    "content": [
        {"text": "Summarize this review of Casa Del Mar: 'The seafood paella was outstanding with perfectly cooked shrimp. Service was slow but friendly. Nice ocean view but prices are on the higher side.'"}
    ]
}
```

Effective user messages are:
- Clear and specific about the requested task
- Properly structured with appropriate context
- Focused on a single coherent request
- Free from contradictions or ambiguities

## Context

Context is any relevant supplementary information that can guide the model in generating an appropriate response accurately. Context can help the model to generate accurate and informed responses. This can range from simple clarifications to extensive reference materials:

- **Simple disambiguating context**: Single words or phrases that clarify meaning (e.g., "Paris, France" vs. "Paris, Texas" or "Paris Hilton")

- **Background information**: Brief details that frame the request (e.g., "I'm planning a vacation" or "I'm writing a historical paper")

- **Few-shot examples**: Demonstrating the expected reasoning pattern or output format through examples within the prompt. For more details on this powerful technique, see the [Prompt Composition](../2_3_2-7_composition/composition.md){:target="_blank" rel="noopener noreferrer"} section.

- **Retrieved information**: Data pulled from external sources (e.g., vector stores or databases for tabular data) through Retrieval Augmented Generation (RAG) to ground the model's responses in factual information.

- **Conversation history**: Previous exchanges that provide context for the current interaction in multi-turn conversations.

Reference data significantly improves the model's ability to generate relevant, accurate responses, especially for domain-specific tasks or when current information is required. While not mandatory for every use case, incorporating relevant reference data often produces higher quality outputs than relying solely on the model's pre-trained knowledge.

When including reference data, be mindful of token consumption as this can substantially increase prompt length. Techniques like effective chunking, filtering for relevance, and strategic placement within the prompt can help optimize performance.

## Best Practices for Amazon Bedrock Prompt Engineering

The following best practices will help you maximize performance and reliability when working with Amazon Bedrock models:

### 1. Use Structured Prompt Templates

When working with Amazon Bedrock models, a clear sectional structure significantly improves performance.

The COSTAR framework provides an excellent foundation for organizing prompts, which can be implemented through explicit sectional templates.

#### The COSTAR Framework for Amazon Bedrock Models

COSTAR breaks down prompt engineering into six components:

```python
prompt_template = f'''
# Context
{provide_background_information}

# Objective
{define_specific_task}

# Style
{specify_writing_style}

# Tone
{set_appropriate_tone}

# Audience
{identify_target_audience}

# Response Format
{outline_required_structure}

# Input Data
{data_to_process}
'''
```

This structured approach ensures that Amazon Bedrock models receive clear, comprehensive instructions that address all aspects needed for optimal responses.

### 2. Leverage System Messages for Behavioral Constraints

System messages provide powerful control over model behavior, allowing you to establish consistent guidelines and constraints that persist throughout the conversation:

```python
import boto3

bedrock = boto3.client('bedrock-runtime')

# System message enforcing key constraints
system_message = '''You are a professional restaurant reviewer.
You must NEVER modify restaurant names as they appear in the input.
Present all prices using $ symbols.
All responses should be concise (under 50 words).'''

response = bedrock.converse(
    system=[{"text": system_message}],
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=[
        {
            "role": "user",
            "content": [{"text": "Summarize this review: 'Le Petit Bistro served excellent coq au vin ($28) and the atmosphere was charming, though parking was difficult.'"}]
        }
    ]
)
```

### 3. Be Explicit About Input Data Format and Expectations

When working with more extensive or complex data inputs, explicitly naming and describing input formats can reduce misinterpretation and improves response accuracy:

```python
context = '''I will provide restaurant review data with the following elements:
- RESTAURANT: The exact restaurant name (which must be preserved exactly as written)
- CUISINE: Type of cuisine offered
- PRICE: Price range in $ format
- COMMENTS: Customer feedback highlights'''

# Later in the prompt
data = '''
RESTAURANT: Nonna's Tratt
CUISINE: Italian
PRICE: $$
COMMENTS: Authentic pasta, friendly service, limited seating, noisy on weekends
'''
```

### 4. Position Critical Instructions Strategically

While you should experiment with your specific model, many language models pay particular attention to instructions at the beginning and end of prompts. For the most reliable enforcement of constraints:

- Place fundamental behavioral guidance in the system message
- Put context-setting information near the beginning of the user message
- Position critical formatting rules and final output requirements at the end of the prompt

### 5. Use Repetition for Critical Constraints

For absolutely critical constraints, strategic repetition across both system message and user instructions can significantly improve compliance, though effectiveness may vary by model so you should experiment with your specific use case:

```python
system_message = '''You must always preserve exact restaurant names with ZERO modifications.'''

instructions = '''
CRITICAL NAMING RULES:
1. USE ONLY the exact restaurant name as provided
2. DO NOT correct, expand, or modify restaurant names
3. If input shows 'Joe's BBQ', ONLY use 'Joe's BBQ' in output
4. 100% LITERAL interpretation of restaurant names is MANDATORY
'''
```

### 6. Control Temperature and Top-P for Consistency

Lower temperature and top-P values reduce randomness in model outputs, which typically produces more consistent adherence to formatting requirements (see [Temperature and Sampling](../2_3_2-5_temperature_sampling/temperature_sampling.md){:target="_blank" rel="noopener noreferrer"} for more details):

```python
response = bedrock.converse(
    system=[{"text": system_message}],
    modelId="anthropic.claude-3-sonnet-20240229-v1:0",
    messages=messages,
    inferenceConfig={
        'maxTokens': 300,
        'temperature': 0.1,  # Lower temperature for more deterministic output
        'topP': 0.3          # Narrower sampling for better format adherence
    }
)
```

### 7. Provide Clear "Golden Sample" Examples

For complex formatting requirements, explicit examples demonstrating correct and incorrect outputs can improve model performance:

```python
fs_examples = '''EXAMPLE:
Input Restaurant Name: 'Tony's Pizza'
CORRECT Output: Mentions 'Tony's Pizza' exactly as written
INCORRECT Output: Any modification like 'Tony's Pizzeria' or 'Tony's'

Input: "RESTAURANT: Sea Shore Sushi, PRICE: $$$"
CORRECT Output: "Sea Shore Sushi offers high-end dining ($$$) with..."
INCORRECT Output: "The Seashore Sushi restaurant is expensive with..."
'''
```

## Making it Practical

When building with GenAI, don't treat prompt design as an afterthought. It should be considered a core part of your solution architecture—just like you would with capacity planning, cost optimization, or security design. As you develop your applications, be mindful of how prompt components like system messages, context, and user inputs interact at scale.

For system messages, these top-level instructions often get repeated on every call, especially in stateless architectures. This repetition can bloat context size and inflate costs.

!!! note "Important security note: While system messages can help guide model behavior, they should never be relied upon as your only security mechanism. System message instructions can be overridden or manipulated by carefully crafted user inputs. Always implement security controls, input validation, output filtering, guardrails outside the LLM to properly safeguard your application."

Finally, it's important to recognize that user inputs are a powerful lever for controlling model behavior, without needing to change code or fine-tune the model. Clear, structured instructions often lead to more accurate, aligned responses than generic or vague queries.

### Real-World Application Scenarios

|Use Case|Core Components Applied|
|---|---|
|Support Chatbot|System persona + Contextual FAQ + User query|
|Writing Assistant|System tone + Examples of summaries + User draft|
|RAG System|Retrieved content as context + User request|
|Dev Tool|Code snippet in context + Format instruction (e.g., fix, optimize)|
|Automated Report|System instruction + Reference data (no user input required)|

## Get Hands-On

* [Hugging Face Spaces](https://huggingface.co/spaces){:target="_blank" rel="noopener noreferrer"}

## Further Reading

* [Learn Prompting - Prompt Structure](https://learnprompting.org/docs/basics/prompt_structure){:target="_blank" rel="noopener noreferrer"}
* [Understanding Key Elements of a Prompt](https://medium.com/@adheeshachamoddesilva/prompt-engineering-understand-the-key-elements-of-a-prompt-41c8742d7143){:target="_blank" rel="noopener noreferrer"}
* [LangChain - Chat Token Usage Tracking](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/){:target="_blank" rel="noopener noreferrer"}
* [Amazon Bedrock supported models and features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author/s:**

* Afia Khan - Associate SA - GenAI 

* Alicja Kwasniewska - Sr. Solutions Architect 

**Primary Reviewer:**

* Deepika Kumar - Solution Architect 

* Alicja Kwasniewska - Sr. Solutions Architect 

* Kihyeon Myung - Sr Applied AI Architect 

**Credits:**

* [Prompt Academy](https://www.promptingguide.ai/){:target="_blank" rel="noopener noreferrer"}
