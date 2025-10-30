<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Core Concepts and Terminology

**Content Level: 100**

## Suggested Pre-Reading

* None! This is a good place to start.

## TL;DR

Generative AI, powered by neural networks and Foundation Models, can understand and generate human-like content across various modalities. It operates through a prompt-response architecture, processing inputs as tokens and embeddings. While appearing magical to users, successful implementation requires careful attention to architectural best practices, security measures, and proper development processes.

## The Core of Generative AI

**Generative AI** represents a significant advancement in artificial intelligence, enabling machines to not only understand but also generate human-like text, images, and other forms of content. With the ability for systems to understand and produce natural human language at the level of complexity now possible through Generative AI systems, the applications are seemingly endless. 


### Neural Networks and Models

Central to this capability are **neural networks,** which have been a prominent computational algorithm for decades within the field of AI.  Neural networks are modeled after the human brain, and process information through layers of interconnected nodes. These networks are **trained** on extensive datasets to recognize patterns and are then capable of producing outputs based on previously unseen data inputs. The patterns of these outputs will closely align to those observed in the training data sets.  The trained neural network alongside the technical components required to interact with are packaged together in a deployable file called a **model.**  A specific model’s internal structure and contents will be defined by the machine learning framework used to produce it and the trained neural network within it.  Example machine learning frameworks that produce models include PyTorch (launched by Facebook, now maintained as a LinuxFoundation project), Tensorflow (Google), and Gluon (Amazon).    

### Foundation Models and LLMs

The type of AI models that represent the leap to Generative AI are called **Foundation Models**.  Foundation Models are trained on vast amounts of data (often measured in petabytes) that allow them to have broad and generally applicable knowledge about a great number of topics. These Foundation Models can then be adapted and specialized further using specialized data and tuning techniques, depending on the use case required.  Foundation Models that support use cases that use natural language as inputs/outputs are called **Large Language Models (LLMs)**.  LLMs have much of the generative AI spotlight on them in the public today, as the most common way that consumers currently interact with Generative AI is through LLM-based chatbot capabilities offered on platforms like ChatGPT.  

## Inputs & Outputs

Generative AI systems operate on a prompt-response architecture. **Prompts** comprise input data or instructional parameters that specify desired output characteristics. In a chatbot use case, the prompt would include the message sent by the end user to the AI bot.  The system generates **responses** based on these input parameters. Response quality correlates with contextual information availability, encompassing both immediate prompt data and supplementary background information provided for task comprehension.

### Tokens and Embeddings 
The fundamental operational units of generative AI systems are called **tokens**. Tokens can be word fragments, complete words, or individual characters. **Tokenization** is the mechanism by which input text from the prompt is segmented into these computational units via protocols specifically designed for that model. The **tokenizer** is an important piece of an AI model’s architecture, and it operates in conjunction with a **dictionary**, **** which maintains the standardized token understood by the model based on its training. AI models require this conversion process due to their inability to process raw text directly. 

The converted tokens are then converted again into a machine-ready format to be used in computation by the model, called **embeddings**. Embeddings are numerical vectors that indicate the location of a particular token within a high-dimension space. The process of designing the high-dimensional space and what vector a token is converted into has the goal of semantically similar tokens being placed close together in the space. So a particular location within the space implies things about the meaning and semantic characteristics of the tokens placed there. For example, the embedding vectors of semantically related terms such as "dog" and "puppy" should exhibit closer mathematical proximity than unrelated terms like "calculator." These vectorized representations encode semantic relationships between tokens, which enables the pattern identification and predictions performed by the Large Langauge Models to be connected to an understanding of the natural language that the embeddings represent.

### Modality
**Modality** refers to the data type available to be used as inputs and/or outputs in AI systems. While initial AI implementations focused on textual data processing, contemporary foundation models incorporate multi-modal capabilities spanning text, image, audio, and video data types. Each modality requires specific processing protocols, though fundamental concepts of tokenization, embeddings, and context remain applicable across modalities. Multi-modal processing capabilities enhance system versatility and expand potential applications.

## Key Architecture & Application Terminology

In order to interact with the models discussed above within an application context, it needs to be deployed and running.  **Model hosting** encompasses the infrastructure and operational frameworks required for AI model deployment and accessibility. Model hosting systems manage computational resource allocation, scaling mechanisms, and service delivery protocols. These systems facilitate model availability through standardized APIs, handle concurrent request processing, and maintain operational efficiency through load balancing and resource optimization procedures.  Amazon Bedrock is an example of a model hosting service.

### Prompt Engineering

**Prompt engineering** is the systematic design and optimization of input instructions given to AI language models to achieve desired outputs, similar to crafting well-structured API calls. Just as software architects design interfaces with specific parameters and expected responses, prompt engineering involves creating precise instructions that guide AI models to produce intended results. This practice includes clear structural organization, effective context management, implementation of proven patterns, incorporation of validation checks, and iterative optimization for improved performance.  See Further Reading for additional information about prompt engineering.

### Retrieval Augmented Generation (RAG) 

**Retrieval Augmented Generation (RAG)** is one of the most predominant architecture patterns for achieving production-level accuracy and performance when using generative AI models in production.  It can be thought of as a robust example of prompt engineering.  RAG enhances AI model response accuracy by incorporating external knowledge retrieval into the prompting and generation process. This architecture queries relevant information from **vector databases** - specialized systems that store and retrieve data as mathematical representations (vectors) of content - and injecting that information into the prompt as required context for the model to utilize when generating a response. The retrieval mechanism reduces **hallucinations** (instances where AI models generate false or fabricated information) by grounding responses with documented and trustworthy sources rather than relying solely on the model's trained parameters. Through this integration of external knowledge with the model's natural language capabilities, RAG systems provide more precise, factual responses, particularly excelling in scenarios requiring current information or domain-specific knowledge.  

### Agents & Agentic AI

Even though single prompt-response interactions with generative AI systems are in their early days, using generative AI to solve more complex and multi-step has quickly become a growing focus.  **Agentic AI** refers to artificial intelligence systems designed to autonomously pursue and complete objectives through a combination of planning, decision-making, and action execution capabilities. These **agents** employ sophisticated algorithms that enable them to understand tasks, break them down into subtasks, interact with their environment or other systems, adapt to changing conditions, and persist until goals are achieved. Unlike reactive AI systems, agentic AI demonstrates goal-directed behavior, maintains internal state awareness, and can orchestrate complex sequences of actions while making independent decisions based on their programming and environmental feedback. The pursuit of achieving standardized patterns, architectures, and services that help companies implement agentic AI systems is one of the fastest and most-invested in areas of technology today.

## Making it Practical

As you grow your expertise with generative AI, it is crucial for you to remember that there’s no magic here.  What appears to be magic to end users and beneficiaries of AI systems is known to you to still be software and architecture under the covers.   The AI systems you’ve interacted with and will design should follow a bevy of best practices in order to achieve the business goals desired as safely, quickly, and as efficiently as possible. 

The principles you’ve learned about modern architecture best practices, distributed systems design, security, etc. will all translate to building generative AI systems.  But you need to remember to “peel the onion” when thinking about all the layers and technical surfaces where those best practices might apply, because reaching production with a generative AI application is going to involve a number of novel stages in the development and pre-deployment processes, and a number of new components in the deployed runtime architecture.  

The set of foundational concepts and terms defined here should help you have an initial frame of reference when diving deeper into the various topics available to read about here.

## Further Reading

<a href="https://aws.amazon.com/what-is/prompt-engineering/" target="_blank" rel="noopener noreferrer">{Prompt Engineering}</a>

## Contributors

**Author:** Andrew Baird - Sr. Principal SA 

**Reviewer**: Don Simpson - Principal Technologist 