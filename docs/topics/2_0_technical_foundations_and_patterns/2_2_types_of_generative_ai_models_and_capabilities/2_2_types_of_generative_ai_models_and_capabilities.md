<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Types of Generative AI Models and Capabilities

**Content Level: 200**



## Suggested Pre-Reading

 - [Core Concepts and Terminology](../../1_0_generative_ai_fundamentals/1_1_core_concepts_and_terminology/core_concepts_and_terminology.md) 
 - [Key Primitives](../2_1_key_primitives/index.md)

## TL;DR

Generative AI encompasses a diverse offering of models categorized by input/output modality, architecture, scale, access model, and specialization.
Text generation models (LLMs) range from small (1-10B parameters) to large (70B+) with corresponding trade-offs between performance and resource requirements.
Image generation primarily uses diffusion models, GANs, or transformer-based approaches, while multimodal models integrate multiple data types within unified architectures.
When selecting appropriate models for specific use cases, architects should evaluate performance requirements against resource constraints, consider deployment options (API-based, self-hosted, edge), and assess customization needs.
Rather than pursuing a one-size-fits-all approach, production systems often benefit from combining complementary models: faster smaller models for routine tasks, larger models for complex reasoning, and specialized models for domain-specific functions.

## Types of Generative AI Models and Capabilities
Following our exploration of [GenAI primitives](../2_1_key_primitives/index.md), this section examines the diverse landscape of generative AI models and their specific capabilities.
Understanding the distinctions between model types is important for architects and builders to select appropriate technologies for their use cases and design effective solutions that leverage each model's strengths while mitigating its limitations.

### The Generative AI Model Landscape

Generative AI encompasses a broad spectrum of models designed to create various forms of content.
While Large Language Models (LLMs) have received significant attention, other offerings include numerous model architectures optimized for different modalities and tasks. These models can be categorized by:

 - **Input/output modality**: Text-only, image, audio, video, or multimodal combinations
 - **Architecture**: Transformer-based, diffusion models, GANs, VAEs, etc.
 - **Scale**: Small specialized models vs. large foundation models
 - **Access model**: Open-source, commercial API-based, or private/proprietary
 - **Specialization**: General-purpose vs. domain-specific models 

### Text Generation Models

Text generation models currently represent the most widely deployed form of generative AI.
This section outlines different properties of LLMs and how these properties impact their applicability.
Modern LLMs are predominantly built on transformer architectures with varying sizes:

 - Small models (1-10B parameters): Models like Mistral 7B or Llama 2 7B offer reasonable performance with reduced computational requirements, enabling deployment in more constrained environments.
 - Medium models (10-70B parameters): Models such as Llama 2 70B or Claude Opus provide enhanced capabilities with moderate resource requirements.
 - Large models (70B+ parameters): Models like GPT-4, Claude or Mistral offer state-of-the-art performance but require significant computational resources.

The parameter count serves as a rough proxy for model capability, though architecture improvements and training methodology can sometimes enable smaller models to outperform larger ones on specific tasks.
Generally, the performance in tokens/sec is higher, the lower the number of parameters is.

Text generation models exhibit a range of capabilities that vary by model size and training approach:

 - **Text completion and chat**: Generating contextually relevant continuations of provided text prompts or maintaining coherent dialog.
 - **Content transformation**: Summarization, translation, paraphrasing, or format conversion
 - **Question answering**: Responding to queries based on general knowledge or provided context
 - **Reasoning**: Solving logical problems, performing calculations, or analyzing scenarios step-by-step
 - **Classification**: Categorizing text into predefined groups or extracting structured information
 - **Creative writing**: Generating stories, poetry, scripts, or other creative content

### Image Generation Models

Image generation models create visual content from descriptions or other images.
These models have evolved rapidly, with several key architectures emerging.

Architectural Approaches

 - **Diffusion models**: Currently dominant in image generation, these models gradually transform random noise into coherent images by reversing a noise-addition process. Examples include Stable Diffusion, DALL-E, and Midjourney.
 - **Generative Adversarial Networks (GANs)**: Earlier architectures featuring generator and discriminator networks competing to improve output quality. While less common for new models, GAN approaches like StyleGAN remain relevant for specific applications.
 - **Transformer-based approaches**: Adapting LLM approaches to image tokens, enabling unified architectures across modalities and models that can create mixed output.

Modern image generation models support various control mechanisms:

 - **Text-to-image generation**: Creating images from textual descriptions
 - **Image-to-image transformation**: Modifying existing images based on instructions, e.g., removing/inserting a background.
 - **Inpainting and outpainting**: Filling in missing parts of images or extending them beyond their original boundaries
 - **Style transfer**: Applying artistic styles from reference images
 - **Control inputs**: Using additional inputs like depth maps, edge detection, or pose estimation to guide generation

### Multimodal Models

Multimodal models integrate multiple forms of data (text, images, audio, video) into unified systems that can process and generate across different modalities.

Common Multimodal Combinations

 - Vision-language models (VLMs): Combining vision and language understanding for tasks like image captioning, visual question answering, and text-to-image generation. Examples include GPT-4 Vision, Claude 3 Opus, and Gemini.
 - Audio-language models: Processing speech recognition, text-to-speech, music generation, and audio understanding. Examples include Whisper, AudioLDM, and MusicLM.
 - Video generation models: Creating video content from text descriptions or image inputs. Examples include Sora, Runway Gen-2, and ModelScope.

Unified Architectures

Recent advances have moved toward unified architectures that can handle multiple modalities within a single model:

Text prompt → Multimodal model → Generated image
Image input → Multimodal model → Text description
Text prompt → Multimodal model → Generated video

These unified architectures simplify deployment and enable cross-modal tasks that previously required multiple specialized models.

#### Model Architectures

The underlying architecture of a generative AI model fundamentally shapes its capabilities, computational requirements, and appropriate use cases.
Modern generative AI relies on several distinct architectural approaches:

- **Transformer-based Models**: Use self-attention mechanisms to process input data in parallel, capturing relationships between elements regardless of distance. They power most modern LLMs including GPT-4, Claude, and Llama. While excellent at modeling dependencies and highly parallelizable, their memory requirements grow quadratically with sequence length.

- **Diffusion Models**: Generate content by gradually denoising random patterns into structured outputs. Currently dominant in state-of-the-art image generation (Stable Diffusion, DALL-E) and emerging in video (Sora). They produce highly detailed outputs but require multiple sampling steps, making inference computationally intensive.

- **Generative Adversarial Networks (GANs)**: Feature generator and discriminator networks that compete, with the generator creating content and the discriminator evaluating realism. Examples include StyleGAN for faces and Pix2Pix for image translation. They can produce sharp outputs with efficient inference but are challenging to train.

- **Variational Autoencoders (VAEs)**: Encode inputs into a compressed latent representation before decoding into generated outputs. Often used as components within larger systems, particularly in image generation pipelines, they enable controlled generation but may produce less detailed outputs.

Architecture selection significantly impacts deployment considerations including training costs, inference speed, scaling properties, and adaptability to different modalities. While transformers currently dominate language models, specific use cases may benefit from alternative architectures based on performance requirements and resource constraints.




### Accessibility - Open vs. Closed Models

LLMs for text, image and video generation can be classified based on their accessibility:

 - Closed/API-only models: Commercial services like GPT-4, Claude, and Gemini provide access through APIs without revealing model weights or architecture details. These typically offer high performance but may have usage restrictions and pricing based on token consumption. 
 - Open-weight models: Models like Llama 2, Mistral, and Falcon release their weights publicly, allowing organizations to run and modify them independently. These models enable greater customization and potentially lower operational costs but may require significant infrastructure for deployment. 
 - Fully open-source models: Models that release not only weights but also training methodologies and data, enabling complete reproducibility and modification.

As discussed in the corresponding section, customization of model weights, e.g., through [fine-tuning](../2_1_key_primitives/2_1_8_fine_tuning/2_1_8_fine_tuning.md), requires LLMs whose weights have been published or specific services that allow for such customizations with closed-weight LLMs.
This means, unless the provider of a closed/API-only model provides fine-tuning capabilities through other means, the models are not open for fine-tuning.
One example for such fine-tuning capabilities is Anthropic Claude, where fine-tuning is available on [Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/){:target="_blank" rel="noopener noreferrer"}.


### Specialization & Domain-Specific Models

While general-purpose models continue to expand their capabilities, specialized models optimized for specific domains offer advantages for certain applications.

#### Code Generation Models

Models specialized for programming tasks, such as GitHub Copilot (based on OpenAI Codex), Amazon CodeWhisperer, and StableCode, offer enhanced performance for:

 - Code completion: Suggesting completions for partially written code
 - Code generation: Creating entire functions or programs from natural language descriptions
 - Code translation: Converting code between programming languages
 - Documentation generation: Creating documentation from code or vice versa

#### Scientific Models

Specialized models have emerged for scientific applications:

 - Protein structure prediction: Models like AlphaFold revolutionizing computational biology
 - Drug discovery: Models generating and evaluating potential new compounds
 - Materials science: Predicting properties of novel materials

#### Industry-Specific Models

Models tailored to specific industries with specialized vocabularies and knowledge:

 - Legal: Contract analysis, case research, and legal document generation
 - Healthcare: Clinical documentation, medical literature analysis, and diagnostic assistance
 - Financial: Market analysis, risk assessment, and regulatory compliance

### Model Selection Considerations

When selecting appropriate models for specific use cases, architects should evaluate:

Performance vs. Resource Requirements

 - Inference latency: Response time requirements for the application
 - Throughput needs: Peak volume of requests the system has to handle
 - Cost structures: Token-based pricing for API models vs. infrastructure costs for self-hosted models

Deployment Options

 - Cloud API services: Simplest integration with pay-per-use pricing
 - Managed deployments: Cloud services offering dedicated model deployments
 - Self-hosted options: On-premise or cloud infrastructure running open-weight models
 - Edge deployment: Quantized or distilled models running on local devices

Integration Requirements

 - API stability: Commercial APIs may offer more stable interfaces than self-deployed options
 - Customization needs: Requirements for fine-tuning, RAG integration, or specialized outputs
 - Security and compliance: Data processing limitations and regulatory requirements

### Emerging Capabilities and Future Directions

The generative AI landscape continues to evolve rapidly, with several emerging trends:

 - Agentic systems: Models that can plan and execute multi-step tasks, interact with external tools, and maintain long-term goals
 - Multimodal reasoning: Enhanced capabilities to reason across different forms of information
 - Increased efficiency: More capable smaller models through architectural innovations
 - Specialized vertical solutions: Industry-specific models with enhanced domain knowledge
 - Enhanced customization: More efficient fine-tuning and adaptation techniques

## Making it Practical

Understanding the landscape of generative AI models is important for selecting appropriate technologies and designing effective solutions.
Here's how to apply this knowledge in real-world scenarios:

### Model Selection Framework

When approaching a generative AI project, consider this decision framework:

1. **Identify your primary modality needs**: Determine whether your use case requires text, image, video, or multimodal capabilities
2. **Assess performance requirements**: Consider acceptable latency, throughput needs, and quality thresholds for your application
3. **Evaluate resource constraints**: Balance compute resources, budget limitations, and operational requirements
4. **Determine customization needs**: Decide if you need fine-tuning, domain adaptation, or RAG integration
5. **Consider compliance and security**: Account for data privacy, regulatory requirements, and deployment restrictions

### Practical Trade-offs to Consider

#### Text Generation Models

- **Small models (1-10B parameters)**: Consider these when response time is critical, when deploying in resource-constrained environments, or for high-volume, cost-sensitive applications. While they may have limitations with complex reasoning, recent models like Mistral 7B offer impressive capabilities for their size.

- **Medium to large models (10B+ parameters)**: Appropriate when accuracy, nuanced understanding, and sophisticated reasoning are priorities over speed and cost. These models excel at complex tasks but require more substantial resources and typically incur higher costs.

#### Image Generation

- **API-based services**: Ideal for teams without specialized ML infrastructure who need quick integration. Consider these for prototyping or when customization requirements are minimal.

- **Self-hosted diffusion models**: Appropriate when you need control over the deployment environment, have specific customization requirements, or face data privacy constraints that prevent using third-party APIs.

### Deployment Considerations

The choice of deployment approach significantly impacts operational characteristics:

- **Cloud API services**: The fastest path to implementation with minimal infrastructure management. Costs scale with usage, which is advantageous for variable workloads but potentially expensive for high-volume applications. Example: Amazon Bedrock.

- **Self-hosted models**: Provide greater control and potentially lower per-inference costs for high-volume applications, but require expertise to deploy and maintain. Consider this approach when you have specialized needs or high sustained usage. Example: Amazon Sagemaker or EC2 instances.

- **Edge deployment**: Necessary when internet connectivity is unreliable or when real-time processing is required without network latency. This typically requires significant model optimization through techniques like quantization.

### Real-World Application Patterns

#### Complementary Model Architectures

Rather than selecting a single "best" model, many production systems use multiple models in concert:

- A smaller, faster model for initial processing or high-volume tasks
- A larger, more capable model for complex cases where the smaller model's confidence is low
- Specialized models for domain-specific components of the workflow

#### Task-Specific Optimization

Instead of using general-purpose models for everything:

- Use code-specific models like Amazon Q Developer or Anthropic Claude for software development tasks
- Employ domain-tuned models for industry-specific applications
- Apply RAG techniques to enhance general models with specialized knowledge

#### Multimodal Integration

As business applications increasingly span different data types:

- Consider whether separate specialized models or a unified multimodal model best serves your use case
- Evaluate the trade-offs between end-to-end multimodal systems versus pipelines of specialized models
- Plan for how different modalities will be synchronized and integrated in your application flow

By understanding the diverse landscape of generative AI models and their capabilities, you can make more informed architectural decisions that balance performance, cost, and functionality for your specific use cases.

## Further Reading
 - [Articificalanalysis.ai - LLM Benchmark Dashboard](https://artificialanalysis.ai//){:target="_blank" rel="noopener noreferrer"}
 - [lmarena.ai](https://lmarena.ai/){:target="_blank" rel="noopener noreferrer"}
 - [Amazon Bedrock Model Evaluations](https://aws.amazon.com/bedrock/evaluations/){:target="_blank" rel="noopener noreferrer"}
 - [Understanding LLM Evaluation and Benchmarks: A Complete Guide](https://www.turing.com/resources/understanding-llm-evaluation-and-benchmarks){:target="_blank" rel="noopener noreferrer"}


## Contributors

Author/s:

 - Markus Bestehorn - Tech Lead Generative AI EMEA 

Primary Reviewers:

 - Yibo Liang - Generative AI Specialist SA 
 - Emily Ransley - Generative AI Specialist SA 

Additional Reviewer/s: 

 - Ana-Maria Olaru - Sr. Program Manager 
 - Andrew Hood - Head of Program Development 
 - Dominic Murphy - Sr Mgr, Applied AI Architecture 
 - Gareth Faires - Sr Generative AI Specialist SA 
