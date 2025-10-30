<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Case Studies for Financial Services

**Content Level: 200**

## Suggested Pre-Reading

* [AWS: Generative AI for Financial Services](https://aws.amazon.com/financial-services/generative-ai/){:target="_blank" rel="noopener noreferrer"}

## TL;DR

Financial institutions are adopting increasingly complex use cases for generative AI, leveraging agentic workflows and integrating generative AI into customer-facing applications. AWS offers financial services institutions the services, AI capabilities, infrastructure, and security they need to leverage generative AI at scale, and drive innovation at an unprecedented pace. 

## Generative AI applications
This collection of case studies demonstrates how leading financial institutions are achieving measurable business outcomes through generative AI applications:

### S&P Global Ratings: Knowledge work automation
[S&P Global Ratings](https://www.spglobal.com/ratings/en){:target="_blank" rel="noopener noreferrer"}, the credit rating division of S&P Global, used Generative AI to accelerate the delivery of financial analysis and creation of supporting documentation, increasing capacity and improving time to market. In financial services and credit analysis, time is a precious resource. These documents are complex, with a variety of sections that require deep subject matter expertise to create, which is a time-consuming process. 
AWS collaborated with the Ratings team to develop a comprehensive AI solution for analysis document generation. This solution ingests a wide variety of internal documentation to retrieve, extract, and then generate documents section-by-section to augment analyst efforts. The solution empowers analysts to deliver faster results, driving value for S&P customers. It reduced manual effort, enhanced operational efficiency and time-to-market, and generated consistent positive user feedback with high engagement metrics. The solution uses Llama 3.2 90B Vision Instruct, BGE Large EN v1.5 for embeddings, Amazon SageMaker P5 instances, and Amazon OpenSearch for comprehensive analysis and automation.

### Travelers: Augment human capabilities
For all organizations with a customer service function, efficient classification and routing of queries enable customers to receive a speedy and accurate service experience. AWS collaborated with [Travelers](https://aws.amazon.com/blogs/machine-learning/how-travelers-insurance-classified-emails-with-amazon-bedrock-and-prompt-engineering/){:target="_blank" rel="noopener noreferrer"}, a leading property and casualty insurance carrier, to address this challenge.
Travelers receives millions of emails a year with agent or customer requests to service policies, with 25% of emails containing attachments (e.g. ACORD insurance forms as PDFs). Requests involve areas like address changes, coverage adjustments, payroll updates, or exposure changes. The main challenge was classifying emails received by Travelers into service request categories.
To achieve the optimal balance of cost and accuracy, the solution employed prompt engineering on a pre-trained Foundation Model (FM) with few-shot prompting to predict the class of an email, all built on Amazon Bedrock using Anthropic's Claude models. The teams manually analyzed over 4,000 email texts and consulted with business experts to understand the differences between categories. This provided sufficient explanations for the FM, including explicit instructions on how to classify an email. Additional instructions showed the model how to identify key phrases that help distinguish an email's class from the others. The workflow starts with an email, then, given the email’s text and any PDF attachments, the email is given a classification of 13 defined classes by the model.
The Travelers and AWS system uses prompt engineering, category condensing, document processing adjustments, and improved instructions. It yielded classification accuracy to 91%, a 23 point improvement compared to the original solution with just the pre-trained FM. Using the predictive capabilities of FMs to classify complex, and sometimes ambiguous, service request emails, the system will save tens of thousands of hours of manual processing and redirect that time toward more complex tasks. This solution demonstrates the practical application of GenAI to augment human capabilities. It is a great example of how organizations can use technology to optimize operations while maintaining focus on customer experience.

### Experian plc: A world of insight
[Experian plc](https://www.experianplc.com/newsroom/press-releases/2025/experian-accelerates-migration-to-aws-to-drive-innovation-with-g){:target="_blank" rel="noopener noreferrer"}, a global leader in data broker and consumer credit reporting, processes 6 million dispute documents annually through manual review processes. This creates high operational costs and resource intensity, while still requiring human validation for compliance. The system incurs long handling times to extract and standardize customer information from multiple input channels. Automating dispute reason classification creates an opportunity to optimize the current process.
AWS built a solution using state-of-the-art generative AI tools to extract customer information for identity matching and automate dispute reason code categorization. The system analyzes extracted content alongside credit report data, demonstrating reliable accuracy. As a result, the system went to production and achieved a 19% target reduction in handle time. Agents in live environment are using automated dispute categorization and one-click AI suggestions. 
The system significantly improved one-shot and first-pass acceptance accuracy of the dispute handling volume. The team delivered this initiative under budget using cost-optimized Amazon Bedrock models.
The framework is being reused for another use case, fraud detection, which is targeting 40% of traffic. The solution utilizes automated dispute classification, intelligent account extraction, and AI-powered identity matching capabilities built on Amazon Bedrock.

### PropHero: Intelligent AI advisor
[PropHero](https://aws.amazon.com/blogs/machine-learning/how-prophero-built-an-intelligent-property-investment-advisor-with-continuous-evaluation-using-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}, a property wealth management platform, needed to enhance customer engagement in property investment conversations. The company also wanted to provide accurate, knowledge-grounded advisory services to help users invest through their platform.
PropHero collaborated with AWS to develop a multi-agent advisory system using LangGraph and Amazon Bedrock 
models. The solution leverages a modular agent architecture that includes specialized agents, using Amazon Bedrock Knowledge Base for delivering relevant information. The knowledge base draws from PropHero's Australian and Spain Market database.
The PropHero AI advisor achieved 90% goal accuracy and gained strong adoption, with over 50% of users (and over 70% of paid users) actively using the system. The solution reduced customer service workload by 30% and achieved 60% cost savings through strategic model selection. The architecture leverages multiple Amazon Bedrock models including Anthropic Claude 3.5 Haiku, Amazon Nova Lite and Pro, and Cohere embedding and reranking models, supported by Amazon S3 for data storage, DynamoDB for conversation history, and a continuous evaluation system for quality monitoring. 


### Apoidea: AI-powered banking document extraction and processing
[Apoidea Group](https://aws.amazon.com/blogs/machine-learning/how-apoidea-group-enhances-visual-information-extraction-from-banking-documents-with-multimodal-models-using-llama-factory-on-amazon-sagemaker-hyperpod/){:target="_blank" rel="noopener noreferrer"}, a leading FinTech company, faced inefficiencies in banking document processing due to diverse formats, poor scan quality, and complex table structures. These issues required significant manual effort for tasks such as know your customer (KYC) procedures and loan applications.
By partnering with AWS, Apoidea fine-tuned Qwen2-VL-7B-Instruct model with LLaMA-Factory.
The solution reduced document processing time from 6 hours to 10 minutes and achieved 81.1% TEDS (Tree-Edit-Distance-based Similarity) score, approaching enterprise-grade accuracy. Apoidea estimated over 80% return on investment (ROI) for the fine-tuned model. The solution was deployed successfully across over 10 financial services institutions. Apoidea used Amazon SageMaker HyperPod for distributed model training, integrated with AWS Key Management Service (KMS) and AWS Identity and Access Management (IAM) to implement banking-grade security and compliance.

### Nomura Research Institute (NRI) : LLM customization on AWS Trainium and Inferentia
[Nomura Research Institute (NRI)](https://www.nri.com/en/index.html){:target="_blank" rel="noopener noreferrer"}, a leading think-tank and systems integrator, aimed to develop an innovative methodology for building practical, industry-specific small-scale LLMs. These models would deliver superior accuracy compared to large commercial alternatives while speeding up development through purpose built chips like AWS Trainium and AWS Inferentia.
AWS supported NRI by creating environments for Trainium and Inferentia for both training and inference of LLMs. The team provided detailed procedure documentation to support NRI's continuous pre-training based on their FSI-specific data corpus. The team also conducted experiments on synthetic data creation for instruction fine-tuning using LLM-as-a-Judge evaluation.
As a result, cost efficiency improved by 40% for training and 60-65% for inference compared to GPU. NRI's 8B LLM achieved a 9.6% accuracy improvement over GPT-4o, increasing from 76.7% to 86.3% accuracy.. The company leveraged AWS Trainium, AWS Inferentia for training and inference, and Claude 3.5 Sonnet via Amazon Bedrock for LLM-as-a-Judge evaluation capabilities.

### RDC.AI : Bringing trust to the lending lifecycle
[RDC.AI](https://aws.amazon.com/solutions/case-studies/richdataco-case-study/){:target="_blank" rel="noopener noreferrer"} is a software-as-a-service (SaaS) provider dedicated to helping banks unlock deeper customer insight, optimize lending decisions, and build stronger portfolios. RDC’s mission is to help banks leverage broader data sources, including transactional and behavioral information, to better assess customer viability and business health. Recognizing the need for AI-driven enhancements to make accurate decisions with vast amounts of customer data, RDC collaborated with AWS to build two key AI-driven assistants on Amazon Bedrock: the Data Science Assistant and the Portfolio Assistant. Utilizing AWS-supported models and tools, these assistants help data scientists and portfolio managers conduct model development, troubleshoot queries, analyze data, and gain insights into various segments.

The Data Science Assistant streamlines model validation and provide advanced data insights. Using Anthropic Claude in Amazon Bedrock, it generates accurate responses to technical questions and leverages retrieval-augmented generation for quick access to a knowledge base stored in Amazon OpenSearch Serverless. Thanks to this setup, the assistant can pull relevant information on demand, boosting productivity for RDC’s data science teams.

The Portfolio Assistant converts text to SQL, helping portfolio managers perform data-driven inquiries into loan portfolios without needing deep SQL expertise. The assistant accesses structured portfolio data stored in Amazon Aurora MySQL through natural-language-to-SQL conversion, enabling the assistant to answer queries and provide insights on portfolio performance, risk exposure, and growth opportunities. The Portfolio Assistant also handles high-level portfolio questions, manages iterative interactions for complex queries, and powers self-correction tools including query validation and result accuracy checks, and prompts for additional information when needed.

With the AI-driven assistants developed on Amazon Bedrock, RDC has significantly enhanced its platform, facilitating more precise and efficient credit assessments in business lending. Through an iterative approach, RDC rapidly advanced its generative AI capabilities, deploying the initial version to production in just three months. The solution also meets the stringent security standards required in regulated banking environments. 
Currently in pilot with leading Australian banks, RDC’s Data Science Assistant is estimated to increase the volume of pre-assessed credit offers for existing customers from below 50 percent to well above 50 percent, giving more businesses access to credit with fewer barriers. The platform’s observability also supports early identification of financial distress, empowering institutions to proactively assist at-risk clients and promote healthier portfolios.
As RDC brings this new offering into early adoption cycles with select financial institutions, the company is actively collaborating with beta customers to refine the solution, aligning on security, explainability, and compliance. 


## Making it practical ##

Financial institutions have moved beyond the limitations of legacy technology through exploration and determination. 
The financial services industry, like many others, is evolving in its generative AI journeys. It started with an internal focus to boost employee productivity. The real promise of generative AI is its power as a force multiplier that transforms operations, service delivery, and product creation. As confidence and capabilities have grown, many institutions are now exploring use cases centered on value creation and business growth.

### Drive Business Value with generative AI
To keep pace with rapid AI advancements, organizations should align new technologies with specific business outcomes and creating flexible platforms to integrate and evaluate emerging capabilities. Successful generative AI adoption is about building enterprise-wide capabilities that drive sustained business value.  To achieve this goal, organizations can start a Center of Excellence (COE) with a focused group before expanding, building a hub-and-spoke model that provides templated solutions across the organization, and focusing on consistent use case evaluation and responsible AI implementation. 

### AI Agents
AI agents are emerging as a transformative force in financial services. These AI agents think iteratively and execute complex workflows, helping to reinvent services like lending, underwriting, and claims processing. Organizations are using these capabilities to accelerate technology modernization, perform advanced research, identify novel investment opportunities, and develop deeply customized products and services.
Recent studies and anecdotal reports from the industry indicate that foundation models and generative AI are starting to approach the “trough of disillusionment” in [Gartner’s Hype Cycle for AI](https://www.gartner.com/en/articles/hype-cycle-for-artificial-intelligence){:target="_blank" rel="noopener noreferrer"}, as organizations seek reliable solutions for enterprise use.
AWS is addressing these challenges by combining generative AI with automated reasoning. [AWS has now integrated automated reasoning into its generative AI offerings](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/){:target="_blank" rel="noopener noreferrer"} through automated reasoning checks in [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/){:target="_blank" rel="noopener noreferrer"}. This approach, also known as symbolic AI or formal verification, provides mathematical, logic-based verification that aligns outputs with known facts rather than hallucinations. This is particularly crucial for regulated industries where precision is important.
Through Automated Reasoning checks in Amazon Bedrock Guardrails, organizations can transform their compliance policies and regulatory requirements into a mathematical format, enabling verification of AI outputs with complete certainty.

## Further Reading ##

* [Agentic AI in Financial Services: The future of autonomous finance solutions](https://aws.amazon.com/blogs/awsmarketplace/agentic-ai-solutions-in-financial-services/){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Author:** Guillermo Tantachuco - Principal AI Technologist 

**Reviewer** Randi Larson - Sr. GenAI Business Strategist, GenAI Innovation Center 

**Reviewer** Jared Kramer - Applied Science Manager, GenAI Innovation Center 

**Reviewer** Sirajus Salekin - Applied Scientist II, GenAI Innovation Center 

**Reviewer** Atanu Roy - GenAIIC Geo Leader, APJ/GCR, GenAI Innovation Center 

**Reviewer** Keiichiro Hoashi - Sr Generative AI Strategist, GenAI Innovation Center 

**Reviewer** Rossana Bianchi - Sr Generative AI Strategist, GenAI Innovation Center 

**Reviewer** Peiyang He - Sr Manager, Data Science, GenAI Innovation Center 

**Reviewer** Xuefeng Liu - Senior Data Science Manager, GenAI Innovation Center 
