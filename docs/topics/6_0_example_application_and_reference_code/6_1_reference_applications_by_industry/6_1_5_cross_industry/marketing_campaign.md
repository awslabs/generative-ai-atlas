<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Next-Generation Marketing Campaign

**Content Level: 300**

## Suggested Pre-Reading

* [Meta-prompting](../../../2_0_technical_foundations_and_patterns/2_3_core_archtectural_concepts/2_3_2_prompt_engineering/2_3_2-7_composition/composition.md)
* [Multimodal Retrieval Augmented Generation (RAG)](../../../3_0_architecture_and_design_patterns/3_3_retrieval_augmented_generation/3_3_4_multi_modal_rag/3_3_4_multi_modal_rag.md)
* [Image Generation](../../../3_0_architecture_and_design_patterns/3_1_system_and_application_design_patterns_for_genai/3_1_2_architecture_patterns_by_application_type/3_1_2_3_multimodal_ai_system/3_1_2_3_2_image_generation/image_generation_doc.md)
* [Human-in-the-loop (HITL)](../../../3_0_architecture_and_design_patterns/3_1_system_and_application_design_patterns_for_genai/3_1_1_foundation_architecture_components/3_1_1_8_additional_components/3_1_1_8_1_human_in_the_loop/3_1_1_8_1_human_in_the_loop.md)
* [Amazon Nova foundation models](https://aws.amazon.com/ai/generative-ai/nova/){:target="_blank" rel="noopener noreferrer"}

## TL;DR
The Next-Generation Marketing Campaign solution provides an AI-powered solution that accelerates the creation of engaging images for marketing campaigns. It allows marketing teams to create multiple ideas, in minutes, to accompany ads, products, and campaigns. This solution utilizes past campaign data to inform new creative directions. It combines text-to-image generation, multimodal embeddings for searching reference images, and an intuitive workflow to accelerate campaign development while maintaining human oversight. The solution leverages Amazon Bedrock and Nova models to create campaign images and Amazon OpenSearch Service for image search and retrieval.

## Industry
**Cross-industry**: This solution has broad applicability across industries that require marketing campaign creation and visual asset generation. 

* The **advertising and marketing industry** can generate and iterate on campaign visuals, reducing time-to-market and production costs while maintaining creative quality. 
* In the **retail and e-commerce sector**, online retailers can create compelling product imagery and promotional materials at scale, adapting to seasonal changes and promotions. 
* **Media and entertainment companies** can generate promotional materials and social media assets efficiently while maintaining brand consistency. 
* **Professional services firms** can create polished marketing materials and client presentations with reduced reliance on external creative resources.

## Business situation
Marketing teams need to produce high-quality creative assets rapidly while maintaining brand consistency and campaign effectiveness. Traditional creative processes are time-consuming and expensive as they require multiple rounds of revisions between stakeholders. Marketing teams need to accelerate ideation and asset generation, while leveraging insights from past successful campaigns. However, these teams lack tools that combine creative flexibility with operational efficiency. Previous attempts to streamline visual asset creation have either sacrificed quality for speed or required technical expertise. 

## When to use
This solution is useful for organizations looking to enable marketing teams to create visual assets across multiple campaigns without proportionally increasing resources.

## Benefits
This solution balances creative quality and automation with human oversight. It delivers the following benefits through Gen AI-powered automation:

**Business Benefits**

* Enables marketing teams to create custom images using AI, eliminating the need for specialized knowledge in prompt engineering.
* Reduces cost and complexity of image creation, enabling organizations to respond quickly to market trends and opportunities, while maintaining control over the creative process.
* Analyzes metadata from past campaigns to identify and reuse content that performed well against specific KPIs, such as engagement rates, click-through rates, or follower growth.
* Decreases production time of campaign visuals from weeks to minutes, allowing organizations to allocate resources more efficiently.

**Technology Benefits**

* Leverages foundation models for generation of high-quality images. 
* Implements prompt engineering through meta-prompting, removing the need for specialized expertise in this area. 
* Allows users to search for historical campaigns that worked in the past, simplifying the creation and increasing the effectiveness of new campaigns. 

## Architecture
This solution implements a serverless architecture that utilizes Amazon Bedrock to generate creative assets and Amazon OpenSearch Service for search capabilities. The architecture consists of two main components: visuals generation and image search engine, as described below.

<div style="margin:auto;text-align:center;width:100%;"><img src="./assets/marketing_architecture_full.png" alt="Multi-agent" width="800"/></div>

### Image search engine

The image search engine helps users find relevant assets from past campaigns by indexing and retrieving them based on the new campaign’s context. The search engine is implemented in a multi-step process:

* **Index creation**: Users upload images to Amazon S3 for storage, which triggers the indexing workflow. AWS Step Functions orchestrates three Lambda functions:
    * The first function uses Nova Pro to generate detailed image descriptions.
    * The second function leverages Titan Multimodal Embeddings to create the vector representation of both images and campaign description.
    * The third function stores vector embeddings and metadata in OpenSearch Serverless.
* **Search and Retrieval**: This function uses the vector search capabilities in OpenSearch Serverless. This capability enables image retrieval based on both semantic similarity and historical performance metrics such as click-through rates. Retrieved images and their performance data inform new campaign creation through a recommendation system. When a new campaign is being created, this function can identify and retrieve relevant past campaigns, providing valuable insights and inspiration to the user.

### Visuals generation

The visuals generation component allows users to create images for marketing campaigns. The solution implements a workflow that guides users from campaign description through image generation. The process begins with a user providing a description for a new campaign, including product, objectives, and target audience. The solution implements four stages to create a campaign: 

* **Campaign recommendation**: Performance data of past campaigns enriches new campaign creation through vector similarity search. This function converts the user's campaign input into a vector embedding and performs a similarity search to retrieve the most relevant images from past campaigns. Users can select the campaign images that best align with their creative vision to use them as a reference.
* **Meta-prompt creation**: Meta-prompting is a technique where one foundation model is used to generate or optimize prompts for another foundation model. Meta-prompting removes the need for prompt engineering expertise. This function analyzes the user's inputs, understands the context and requirements, and then crafts a prompt with Nova Pro to help generate visuals. This function can also incorporate learnings from past successful campaigns, adapting its prompt generation over time to improve outcomes.
* **Image generation**: Users have the option to edit the AI-generated prompt created in the previous step. This function takes the optimized prompt and uses Amazon Bedrock's Nova Canvas, a text-to-image model, to generate professional-quality campaign visuals in seconds. Generated images are stored in an Amazon S3 bucket, with their metadata and embeddings indexed in OpenSearch for future reference. Nova Canvas applies an invisible watermark to generated images to promote safe and transparent AI development.
* **Campaign management**: This function manages the lifecycle of campaign data in Amazon DynamoDB. It maintains campaign metadata, including performance metrics. This campaign data enriches the feedback loop, helping improve asset generation for future campaigns.

It is important to highlight that, during visual generation, the solution allows for human-in-the-loop (HITL) orchestration to validate generated content and help minimize the risk of harmful content reaching end users.

**AWS Services Used:**

* Amazon Bedrock is used to invoke the Amazon Nova Pro, Amazon Titan Multimodal Embeddings, and Amazon Nova Canvas models using a common API. 
* Amazon Lambda functions are used to implement visuals generation and image search capabilities.
* Amazon DynamoDB database stores campaign information.
* Amazon API Gateway manages all API operations.
* Amazon Cognito is used to manage user authentication and authorization.
* An Amazon OpenSearch Serverless index is created to store the information of past campaigns.
* AWS Step Functions is used to orchestrate the campaign's indexing workflow.
* Amazon S3 to store generated images.

## Gen AI patterns used
The solution implements several key generative AI patterns:

* [**Meta-prompting**](../../../2_0_technical_foundations_and_patterns/2_3_core_archtectural_concepts/2_3_2_prompt_engineering/2_3_2-7_composition/composition.md): This solution uses Amazon Nova Pro to generate prompts for Amazon Nova Canvas. This approach removes the need for users to have expertise in prompt engineering, making the system more accessible and consistently producing high-quality results.
* [**Multimodal Retrieval Augmented Generation (RAG)**](../../../3_0_architecture_and_design_patterns/3_3_retrieval_augmented_generation/3_3_4_multi_modal_rag/3_3_4_multi_modal_rag.md): The solution leverages the Amazon Titan Multimodal Embeddings model to create vector representations of images of past campaigns. This pattern enriches the generation process with relevant historical data. It then retrieves images, based on image description, to inform new creative directions.
* [**Multimodal Processing**](../../../3_0_architecture_and_design_patterns/3_1_system_and_application_design_patterns_for_genai/3_1_2_architecture_patterns_by_application_type/3_1_2_3_multimodal_ai_system/3_1_2_3_2_image_generation/image_generation_doc.md): The solution combines text analysis and image generation through specialized foundation models. Amazon Nova Pro handles text processing and prompt generation, while Amazon Nova Canvas manages image creation, allowing for a seamless flow from text input to visual output.
* [**Human-in-the-loop (HITL)**](../../../3_0_architecture_and_design_patterns/3_1_system_and_application_design_patterns_for_genai/3_1_1_foundation_architecture_components/3_1_1_8_additional_components/3_1_1_8_1_human_in_the_loop/3_1_1_8_1_human_in_the_loop.md): User can validate generated content and help minimize the risk of harmful content reaching end users.

## AWS Well-Architected Best Practices

### Operational Excellence

#### [GENOPS02-BP01: Monitor all application layers](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp01.html){:target="_blank" rel="noopener noreferrer"}
The solution tracks model performance metrics, workflow execution statistics, and resource utilization patterns. This monitoring enables rapid identification and resolution of processing bottlenecks while maintaining performance.

#### [GENOPS02-BP02: Monitor foundation model metrics](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp02.html){:target="_blank" rel="noopener noreferrer"}
The solution implements monitoring across all foundation model interactions in Amazon Bedrock. CloudWatch metrics track key performance indicators including invocation counts, latency, token usage, and error rates. 

#### [GENOPS04-BP01: Automate generative AI application lifecycle with infrastructure as code (IaC)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops04-bp01.html){:target="_blank" rel="noopener noreferrer"}
The solution uses infrastructure as code deployment patterns for generative AI applications through AWS CDK.

### Security Pillar

#### [GENSEC01-BP01: Grant least privilege access to foundation model endpoints](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec01-bp01.html){:target="_blank" rel="noopener noreferrer"}
The solution implements Cognito-based authentication for API access, so that only authorized users can interact with the foundation models.

#### [GENSEC02-BP01: Implement guardrails to mitigate harmful or incorrect model responses](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec02-bp01.html){:target="_blank" rel="noopener noreferrer"}
Nova Canvas applies an invisible watermark to generated images to promote safe and transparent AI development.

### Reliability Pillar

#### [GENREL03-BP01: Use logic to manage prompt flows and gracefully recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03-bp01.html){:target="_blank" rel="noopener noreferrer"}
AWS Step Functions handles error conditions gracefully and enables reliable execution of the multi-step generation process.

### Performance Efficiency Pillar

#### [GENPERF02-BP03: Select and customize the appropriate model for your use case](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf02-bp03.html){:target="_blank" rel="noopener noreferrer"}
The architecture utilizes Nova Pro for prompting and Nova Canvas for image generation.

### Cost Optimization Pillar

#### [GENCOST01-BP01: Right-size model selection to optimize inference costs](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost01-bp01.html){:target="_blank" rel="noopener noreferrer"}
The solution selects models based on the specific requirements of each task, balancing performance and cost.

#### [GENCOST03-BP01: Reduce prompt token length](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp01.html){:target="_blank" rel="noopener noreferrer"}
The meta-prompting system is designed to generate concise, effective prompts, minimizing token usage and associated costs.

### Sustainability Pillar

#### [GENSUS01-BP01: Implement auto scaling and serverless architectures to optimize resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus01-bp01.html){:target="_blank" rel="noopener noreferrer"}
The solution leverages serverless technologies such as Bedrock, Lambda, Step Functions, and DynamoDB to minimize idle resources and optimize energy consumption.

## Design tradeoffs
The solution made several key design tradeoffs:

* **Image creation**: The solution prioritizes data-driven decision making over unconstrained creative exploration. It explicitly uses past successful campaigns to influence new creative generation. 
* **Metaprompting**: The solution employs metaprompting instead of few-shot learning. While few-shot learning yields accurate results, its higher token requirements per invocation increase both costs and latency.
* **Model scalability**: Even though functionality is implemented as Lambda functions, it is important to note that the overall scalability is constrained by the rate limits of the models your organization selects. This means there is an upper limit to the number of requests that can be processed within a given time frame.
* **Human Control**: The solution generates five images initially and then allows on-demand generation. This represents a balance between automated bulk creation and giving marketing teams control over the iteration process. 

## Common customizations
Common customizations include:

* **Brand guidelines**: Implement custom brand guidelines as constraints in the prompt generation process. This could involve creating a database of brand-specific terms, color palettes, and style guides that the meta-prompting system can reference when crafting prompts for Nova Canvas.
* **Product catalog integration**: Integrate with your organization’s product catalog to automatically generate promotional images for new or seasonal items. This might involve creating a Lambda function that triggers image generation based on inventory updates.
* **Compliance**: Customize the workflow to include additional steps for compliance checks and rights management. This could be implemented by adding extra nodes to the Step Functions workflow that interact with rights management databases or trigger human reviews for sensitive content.
* **Multi-Asset generation**: Extend the solution to generate additional assets, such as copy, videos, presentation decks, or reports. This could involve integrating additional generative AI services, expanding the capabilities beyond image creation.

## Further Reading
* [Next generation marketing campaigns - Github repository](https://github.com/aws-samples/generative-ai-ml-latam-samples/tree/main/blueprints/genai-marketing-campaigns){:target="_blank" rel="noopener noreferrer"}

## Contributors
**Author:** Guillermo Tantachuco - Principal AI Technologist 

**Reviewer:** David Laredo - Sr. Prototyping Architect, PACE 