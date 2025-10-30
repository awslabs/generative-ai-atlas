<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Popular Tools, Libraries and Frameworks for Model Development

**Content Level: 200**

## Suggested Pre-Reading
 - [Core Concepts and Terminology](../../../1_0_generative_ai_fundamentals/1_1_core_concepts_and_terminology/core_concepts_and_terminology.md)
 
## TL;DR

Generative AI has spawned a rich environment of **frameworks, libraries** and **tools** that streamline development lifecycle stages from model development, model customization to deployment, LLM orchestration and evaluation. These components not only facilitate development but also enable production-grade deployments through standardized deployment patterns, monitoring capabilities, and integration with cloud services like AWS SageMaker, Amazon ECS and Amazon EKS. While model development continues to evolve rapidly, this chapter focuses on commonly adopted components that reflect established patterns in model development and deployment. Key components span:

* **Frameworks:** Model development environments that enable model training, fine-tuning, and optimization
* **Libraries:** Core components like Hugging Face's offerings that provide the building blocks such as pre-trained models, training algorithms, and deployment optimizations
* **Tools:** Specialized software for model evaluation, performance monitoring, and production deployment

## Frameworks, Libraries and Tools

The following sections explore some of the **most common and influential components** in model development environment — focusing on how frameworks, libraries and tools enable model development, customization, inference, evaluation, monitoring and deployment. These components form the foundation for building production-ready generative AI models. While these categories help organize the discussion, they are not mutually exclusive or exhaustive. The goal here is to provide a **model development-to-deployment lens** with **common patterns** and **fundamental level concepts**—one that mirrors how ML Engineers and Data Scientists typically approach model development in practice. It's important to note that the perspective and list presented here may become outdated almost daily. Not only are model development technologies evolving rapidly, but the capabilities enabled by these tools themselves have exponentially accelerated the pace at which new frameworks, libraries and tools are being built, adopted, improved and replaced.

### Frameworks 

***Frameworks*** *- are the foundational software environments used to* ***develop, train, and evaluate** generative AI models. They provide the computational infrastructure and programming interfaces needed for model development, from initial training to production deployment. This section will mainly focus on three common subcategories of model development frameworks:*

#### **Model Development Frameworks**

Model development frameworks serve as the foundation for **training and experimenting with generative models**. These environments provide the computational infrastructure required to build deep neural networks and adapting through transfer learning. Here are three popular model development frameworks:

* **[Pytorch](https://pytorch.org/get-started/locally/){:target="_blank" rel="noopener noreferrer"}**:  PyTorch is a dynamic, Python-native framework widely adopted in **research** developed by Meta. It supports fast prototyping, flexible debugging, and is compatible with most GenAI model architectures. PyTorch’s offerings include a growing number of community tools for large-scale training and distributed compute, making it ideal for fine-tuning language and generative models.

* **[Tensorflow](https://www.tensorflow.org/){:target="_blank" rel="noopener noreferrer"}**: Similar to PyTorch, TensorFlow is a mature and production-focused framework developed by Google. With tools like TensorFlow Serving and TensorBoard, it is frequently used in **enterprise environments** where reproducibility, scalability, and monitoring are key concerns. While slightly more rigid than PyTorch, TensorFlow remains a strong choice for applications that require long-term support and robust deployment pipelines.

* **[Jax](https://github.com/jax-ml/jax){:target="_blank" rel="noopener noreferrer"}**: Jax is a functional, high-performance numerical computing library optimized for **large-scale distribution training** and differentiable programming also developed by Google. It is used primarily in research and by organizations training models across massive hardware clusters. JAX excels in cases where performance, mathematical transparency, and hardware acceleration are primary concerns.

#### **Evaluation and Quality Assurance Frameworks**

Evaluation frameworks provide objective methods to assess the performance and reliability of generative models. Here is a sample evaluation framework that helps guide model selection, prompt tuning, and output evaluation.

* **[DeepEval](https://github.com/confident-ai/deepeval){:target="_blank" rel="noopener noreferrer"}**: An evaluation framework that enables developers to create unit tests for LLM outputs, to help ensure accuracy, relevance and safety. DeepEval supports a wide range of metrics including hallucination, answer relevancy, RAGAS, etc. It also supports synthetic dataset generation for rigorous and customizable evaluations. 


#### **Model Development Tracing Frameworks**

Model development tracing frameworks provide visibility into the training process, enabling developers to monitor, debug, and optimize model development workflows. These frameworks offer logging, visualization, and analysis capabilities that help track training metrics, resource utilization, and model behavior throughout the development lifecycle. Here are two popular tracing frameworks that support efficient model development and optimization:

* **[Weights & Biases (wandb)](https://github.com/wandb/weave){:target="_blank" rel="noopener noreferrer"}**: Weights & Biases is a powerful framework for tracking, visualizing, and comparing model development experiments. It lets teams log hyperparameters, metrics, system information, and artifacts such as datasets, checkpoints, and models, all viewable in an interactive web dashboard. W&B integrates seamlessly with popular frameworks like TensorFlow, PyTorch, and scikit-learn, and offers features like hyperparameter tuning, collaborative reports, and both SaaS and self-hosted deployment options. 

* **[MLFlow](https://github.com/mlflow/mlflow){:target="_blank" rel="noopener noreferrer"}**: MLflow is an open-source framework by Databricks designed to manage the full model development lifecycle—from experiment tracking to deployment. It comprises four core modules: Tracking (logging runs, parameters, metrics, and artifacts), Projects (packaging code and dependencies), Models (standardized model formats), and Registry (versioning and stage promotion). Its strengths lie in reproducibility, collaboration, and flexibility across environments—from local machines to cloud or on-prem servers—with broad framework compatibility and support for experiment comparison, REST API serving, and model lifecycle management.

### Libraries 

***Libraries** – particularly from the Hugging Face environment – have become indispensable in model development. These libraries provide pre-trained models, algorithms, and interfaces that simplify building GenAI applications. Below are libraries for model development and customization and libraries for inference and deployment:* 

#### **Model Customization Libraries**

While frameworks lay the groundwork, model customization libraries build on them to provide modular access to pre-trained models and task-specific adaptations. These libraries help bridge the gap between general-purpose infrastructure and domain-specific generative tasks.

* **[Transformers (Hugging Face)](https://github.com/huggingface/transformers){:target="_blank" rel="noopener noreferrer"}**: Transformers is a foundational Huggingface library for working with pre-trained transformer models across natural language, vision, and audio tasks. It provides seamless integration with different frameworks (PyTorch, TensorFlow, and JAX), and includes utilities for tokenization, model loading, and text generation. Transformers simplify the access to state-of-art models and model development process. 

* **[Diffusers (Hugging Face)](https://github.com/huggingface/diffusers){:target="_blank" rel="noopener noreferrer"}**: Diffusers is a HuggingFace library tailored to diffusion-based generative models, such as Stable Diffusion. It abstracts complex denoising processes into reusable pipelines for text-to-image, image-to-image, and audio generation tasks. It plays a central role in creative and media-driven GenAI applications.

* **[TRL (Hugging Face)](https://github.com/huggingface/trl){:target="_blank" rel="noopener noreferrer"}**: TRL is a HuggingFace library designed to support reinforcement learning and post-training foundation models like DPO, PPO and SFT. It enables more aligned behavior from LLMs by offering interfaces for policy optimization techniques. TRL is key for organizations seeking to customize model outputs in response to qualitative feedback or domain-specific behavior.

* **[Accelerate (Hugging Face)](https://github.com/huggingface/accelerate){:target="_blank" rel="noopener noreferrer"}**: Accelerate is a HuggingFace library for model training acceleration. It supports multiple model acceleration techniques: FSDP, DeepSpeed, Mix Precision, etc. 

#### **Inference and Deployment Libraries**

Transitioning a generative model from development to production requires inference frameworks optimized for performance, hardware efficiency, and scalability. Here are common inference and deployment libraries support real-time interaction with generative models in cost-effective and latency-sensitive environments.

* **[vLLM](https://docs.vllm.ai/en/latest/){:target="_blank" rel="noopener noreferrer"}**: vLLM is a fast and easy to use library for LLM inference and serving. It used for high-throughput inference engine for LLMs with GPU acceleration. vLLM introduces a new scheduling and memory management system to maximize throughput. 

* **[ONNX runtime](https://github.com/microsoft/onnxruntime){:target="_blank" rel="noopener noreferrer"}**: ONNX Runtime is a cross-system library that supports optimized execution of models in the Open Neural Network Exchange format. It enables model portability between systems (e.g., CPU, GPU, specialized chips) and supports acceleration through backend-specific optimizations. ONNX Runtime inference can enable faster customer experiences and lower costs, supporting models from deep learning frameworks such as PyTorch and TensorFlow/Keras as well as classical machine learning libraries such as scikit-learn, LightGBM, XGBoost, etc.

* **[TensorRT](https://developer.nvidia.com/tensorrt){:target="_blank" rel="noopener noreferrer"}**: TensorRT is a deployment-focused SDK and libraries from NVIDIA that compiles and optimizes models for high-performance inference on GPU. It performs layer fusion, quantization, and memory optimization to reduce latency and increase throughput.

* **[AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/){:target="_blank" rel="noopener noreferrer"}**:  AWS Neuron is a comprehensive SDK and libraries designed for running deep learning and AI workloads on AWS Inferentia and Trainium-powered instances. It provides a complete toolkit including compiler, runtime, libraries, and development tools that support the entire machine learning lifecycle, while integrating with popular frameworks like PyTorch and JAX, and offering optimizations for both distributed training and inference through NxD Training and NxD Inference capabilities.

### Tools 

***Tools -** form the backbone of model development, training, and deployment. Large Language Models (LLMs) like Deepseek V3, Claude Sonnet 4 and Llama 4 serve as the foundational engines, processing and generating human-like text based on prompts.* *This section will cover foundation models and AWS AI ML tools:* 

#### Foundation Models

* **[Claude Models (Anthropic)](https://docs.anthropic.com/en/docs/about-claude/models/overview){:target="_blank" rel="noopener noreferrer"}** : Claude is a family of large language models (Claude Sonnet 4 and Claude Opus 4,1) developed by Anthropic. Claude models are designed with a focus on being **helpful, honest, and harmless**, incorporating Anthropic’s research on AI safety and alignment. Claude is also available via a chat interface and an API, similar to ChatGPT. It excels at many of the same tasks – from creative writing and summarization to coding – and is noted for being highly **steerable in personality and tone**. Claude is also accessible via Amazon Bedrock, indicating its relevance for enterprise cloud solutions.

* **[LLaMA Models (Meta)](https://www.llama.com/docs/model-cards-and-prompt-formats/){:target="_blank" rel="noopener noreferrer"}** : LLaMA is Meta's collection of open-source large language models (e.g Llama 3.1, Llama 3.2, Llama 4) ranging from 7B to 70B parameters, designed to help researchers advance their work in AI. It provides foundation models that developers can fine-tune for specific applications, while offering strong performance across various tasks including reasoning, coding, and knowledge-based Q&A, and has spawned numerous community-created derivatives and implementations.

* **[DeepSeek Models (High-Flyer)](https://api-docs.deepseek.com/quick_start/pricing){:target="_blank" rel="noopener noreferrer"}** : DeepSeek is a series of large language models (e.g. DeepSeek V3) developed by High-Flyer AI, featuring both base and chat models with different parameter sizes. It's designed to excel at coding, math, and reasoning tasks while maintaining strong general capabilities, and offers both open-source versions for research and commercial licenses for business applications, making it a versatile option for various AI implementation needs.


#### **AWS AI/ML Tools**

AWS also provides a suite of managed services and tools specifically designed for model development and deployment. Amazon SageMaker is a fully managed AWS services that offers end-to-end capabilities for building, training, and deploying machine learning models at scale. More information can be founded [here](https://aws.amazon.com/sagemaker/){:target="_blank" rel="noopener noreferrer"}

## Making it practical

The frameworks, libraries, and tools introduced in this chapter form the **technical fabric of modern model development**. They show up in ways both explicit and subtle, depending on where in the stages of the development lifecycle

* When **training or fine-tuning models**, frameworks (like PyTorch or TensorFlow), and libraries (like Transformers or TRL) can be chosen for model development. The choices made here will influence compatibility, cost, and model behavior in later stages.
* During **deployment planning**, inference libraries like ONNX Runtime or TensorRT become important for meeting latency or cost requirements. Understanding these trade-offs enables architects to recommend solutions that scale responsibly
* Once models are live, **deployment libraries** (like vLLM), **evaluation framework**(like DeepEval) **and tracing frameworks** (like Weights & Biases) are important for enabling robustness and faithfulness. 


**Fine-tuning Guidance**

When building domain-specific applications, customers will likely need to fine-tune foundation models on their data. For example, customers might use **PyTorch framework** with the **Transformers library** to fine-tune a base model on the company specific support documentation. Customers will need to consider whether to use PEFT techniques for efficient training, and **libraries like TRL for alignment.** **AWS Tools** like SageMaker makes this process easier by providing managed fine-tuning pipelines, while services like Amazon Bedrock offer custom model fine-tuning without managing infrastructure.

## Further Reading

* [Fine-tune Meta Llama 3.1 models for generative AI inference using Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/fine-tune-meta-llama-3-1-models-for-generative-ai-inference-using-amazon-sagemaker-jumpstart/){:target="_blank" rel="noopener noreferrer"}
* [Amazon Bedrock](https://aws.amazon.com/bedrock/){:target="_blank" rel="noopener noreferrer"}

## Contributors

Author/s:

 - Di Wu - Deep Learning Architect 

Primary Reviewers:

- Andrew Baird - Sr. Principal Solutions Architect 
- Don Simpson - Principal Technologist 
- Jagdeep Singh Soni - Sr. AI/ML Spec. SA 
- Fernando Galves - GenAI Solutions Architect 


