<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Model Serving in Generative AI

**Content Level: 200**

## Suggested Pre-Reading

- [Online Inference](../2_3_5-1_online_inference/online_inference.md)
- [Asynchronous Inference](../2_3_5-2_async_inference/async_inference.md)

## TL;DR

Model serving in Generative AI represents the processes and infrastructure needed to deploy large language models (LLMs) to production and manage them at scale for online or asynchronous inference. It's the bridge between trained models and their practical application, encompassing deployment strategies and operational management to enable reliable and cost-effective AI services.

## Understanding Model Serving

Model serving transforms LLMs into readily-available production AI services. Think of it as creating a restaurant kitchen where the chef (the model) needs the right equipment, space, and support staff to serve customers efficiently (model serving). Model serving abstracts the underlying infrastructure complexities. It implements a flexible deployment architecture that handles both pre-trained and custom-built LLMs through container-based and serverless architectures to address different workloads patterns and different operational needs. Container-based deployments provide granular control over runtime environments, scaling policies, and dependencies, suitable for models with specific resource requirements or custom libraries. With the serverless option, you can deploy models without managing the underlying infrastructure and scale them in and out based on your traffic patterns.
Behind the scenes, resource management plays an important role. Just as a kitchen needs the right appliances and staff, LLMs need appropriate computational resources. This might mean powerful GPUs for complex operations or efficient CPU allocation for lighter workloads. Memory management becomes particularly critical with LLMs, which can require significant resources just to load and maintain in a ready state.

## Making it Practical

There's no one-size-fits-all solution in model serving. Depending on your specific use case, requirements, and constraints, you can use Amazon SageMaker AI, Amazon Bedrock, or Amazon Elastic Kubernetes Service (EKS) for your model serving needs:

### **Amazon SageMaker AI**

With SageMaker AI, you can deploy a model into a secure and scalable environment. It supports the following deployment methods, depending on the type of inference:

* **Real-time inference**: For persistent, real-time endpoints that make one prediction at a time, you can deploy your model to SageMaker AI hosting services and get an endpoint that can be used for inference. You can deploy either [a single model or multiple models](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html){:target="_blank" rel="noopener noreferrer"} to the endpoint. These endpoints are fully managed and support [autoscaling](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html){:target="_blank" rel="noopener noreferrer"}.  It is important to note that EC2 Instances stay running until you shut them down.
* **Serverless Inference**: For workloads that have idle periods between traffic spikes and can tolerate cold starts, use Serverless Inference, which integrates with AWS Lambda to offer you high availability, built-in fault tolerance, and automatic scaling. There are two (2) ways to [deploy serverless inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html){:target="_blank" rel="noopener noreferrer"}: 
    * **On-demand**: SageMaker AI provisions and manages the compute resources for you. It automatically scales up and down as needed to handle your request traffic, and you only pay for what you use. 
    * **Provisioned Concurrency (optional)**: Provisioned Concurrency keeps your endpoints warm to have predictable performance and high scalability by initializing compute resources and having them ready to respond within milliseconds. It integrates with [Application Auto Scaling](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints-autoscale.html){:target="_blank" rel="noopener noreferrer"}, so that you can manage endpoints based on a target metric or on a schedule. In addition, you pay for the compute capacity used to process inference requests, billed by the millisecond, and the amount of data processed. You also pay for Provisioned Concurrency usage, based on the memory configured, duration provisioned, and the amount of concurrency enabled.
* **Asynchronous inference**: For requests with large payload sizes up to 1GB, long processing times, and near real-time latency requirements, [deploy an asynchronous inference endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-create-endpoint.html){:target="_blank" rel="noopener noreferrer"}. These endpoints are fully managed and support [autoscaling](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference-autoscale.html){:target="_blank" rel="noopener noreferrer"}. If you choose to use a SageMaker AI-provided container, you can increase the endpoint timeout and payload sizes from the default by setting the environment variables in the container. 
* **Batch transform**: To get predictions for an entire dataset, use [batch transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html){:target="_blank" rel="noopener noreferrer"}. To help optimize resource usage, you can configure the following deployment options: 1/ maximum number of concurrent transforms, which controls how many records are processed in parallel on each instance, 2/ maximum payload size, which determines how much data is sent to the container in each request; and, 3/ for large datasets, you can use multiple instances (up to 100) to process data in parallel, effectively scaling out your computation. Batch transform clusters are torn down when the job completes.

SageMaker AI supports built-in algorithms provided by AWS, which come with their own containers. Alternatively, you can use your own custom algorithms packaged in Docker containers. All inference types, except serverless, support GPU instances. After deploying your model to an endpoint, you can [update the models](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html){:target="_blank" rel="noopener noreferrer"} deployed to your endpoint, and [delete your endpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteEndpoint.html){:target="_blank" rel="noopener noreferrer"}.

### **Amazon Bedrock**

When you want to use a model in Amazon Bedrock, there's no deployment process as such. With the serverless nature of the service, you don't need to worry about choosing instance types, managing scaling, or maintaining infrastructure. Amazon has already done the heavy lifting by [making models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html){:target="_blank" rel="noopener noreferrer"} from Anthropic, AI21 Labs, Stability AI, Meta, and their own Nova and Titan models available through a simple API. Think of it as a subscription to a premium AI service rather than setting up your own AI infrastructure; and, you only pay for what you use. For extra security, you can keep all interactions private by using AWS PrivateLink, control access through IAM policies, and leverage data encryption using AWS Key Management Service (KMS). 
Also, Bedrock gives you the ability to deploy other models in addition to the selection of industry-leading models:

* **Customer Model Import**: You can also train select publicly available models and import them into Bedrock using the [Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html){:target="_blank" rel="noopener noreferrer"} feature. Currently, this feature only supports Llama 2/3, Mistral, and Flan architectures. 
* **Amazon Bedrock Marketplace:** It offers customers over [100 popular, emerging, or specialized models](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-model-reference.html){:target="_blank" rel="noopener noreferrer"}, that you can deploy it to an endpoint managed by SageMaker AI. You can choose your desired number of instances and instance types. Once the models are deployed, the models can be accessed through Bedrock’s APIs. Where applicable, the models can be used with Bedrock Playground, Agents, Knowledge Bases, Prompt Management, Prompt Flows, Guardrails, and Model Evaluation.

### **Amazon EKS** 

Amazon EKS is a managed Kubernetes service that simplifies deploying, managing, and scaling containerized applications using Kubernetes on AWS. You can create an [EKS cluster optimized for multi-node inference](https://awslabs.github.io/data-on-eks/docs/gen-ai){:target="_blank" rel="noopener noreferrer"} using [low-latency networking](https://aws.amazon.com/hpc/efa/){:target="_blank" rel="noopener noreferrer"}, [high-throughput storage](https://aws.amazon.com/efs/){:target="_blank" rel="noopener noreferrer"}, and high-performance instances that leverage [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/){:target="_blank" rel="noopener noreferrer"} and [NVIDIA GPUs](https://aws.amazon.com/nvidia/){:target="_blank" rel="noopener noreferrer"} to accelerate inference. To enable high-performance model serving, you can then use deployment tools such as:

* [Kubeflow on AWS](https://awslabs.github.io/kubeflow-manifests/){:target="_blank" rel="noopener noreferrer"}: You can use Kubeflow on AWS to build enterprise-ready machine learning (ML) applications on Amazon EKS. It supports many use cases, including computer vision, natural language understanding, speech translation, and financial modeling. [KServe](https://www.kubeflow.org/docs/external-add-ons/kserve/introduction/){:target="_blank" rel="noopener noreferrer"}, a Kubeflow component, solves production model serving for online or asynchronous inference. on Kubernetes. It delivers high-abstraction and performant interfaces for production-focused frameworks. KServe is also integrated with AWS Deep Learning Containers (DLCs) to run [inference](https://awslabs.github.io/kubeflow-manifests/docs/component-guides/kserve/aws-deep-learning-containers/){:target="_blank" rel="noopener noreferrer"} workloads.
* [ACK service controller for Amazon SageMaker](https://github.com/aws-controllers-k8s/sagemaker-controller){:target="_blank" rel="noopener noreferrer"}: The SageMaker Controller makes it easier for you to use Kubernetes as your control plane to train, tune, and deploy ML models in SageMaker AI, from your Kubernetes cluster. You can do so by using the Kubernetes API or Kubernetes command line utilities such as kubectl. 
* [SageMaker AI Components for Kubeflow Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/kubernetes-sagemaker-components-for-kubeflow-pipelines.html){:target="_blank" rel="noopener noreferrer"}: Kubeflow Pipelines (KFP) is a platform for building and deploying portable, scalable machine learning (ML) workflows based on Docker containers. These SageMaker AI components allow you to create and monitor native SageMaker AI training, tuning, endpoint deployment, and batch transform jobs from your Kubeflow Pipelines. 
* [Ray Serve](https://docs.ray.io/en/latest/serve/getting_started.html){:target="_blank" rel="noopener noreferrer"} with [vLLM](https://github.com/vllm-project/vllm){:target="_blank" rel="noopener noreferrer"}: Ray is an open-source distributed computing framework that enables scalable and efficient execution of machine learning inference workloads. vLLM is a high-throughput and memory-efficient inference and serving engine for large language models (LLMs), optimized for GPU execution.
* [NVIDIA Triton Inference Server](https://github.com/triton-inference-server){:target="_blank" rel="noopener noreferrer"}: It provides a cloud and edge inferencing solution optimized for both CPUs and GPUs. It leverages different backends to execute models such as PyTorch, [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM){:target="_blank" rel="noopener noreferrer"}, [vLLM-supported models](https://docs.vllm.ai/en/stable/models/supported_models.html){:target="_blank" rel="noopener noreferrer"}, among others.
* [NVIDIA NIM](https://aws.amazon.com/nvidia/nvidia-nim/){:target="_blank" rel="noopener noreferrer"}: It provides a streamlined approach to hosting LLM models like Llama3 within containerized environments. This allows you to leverage their private models while ensuring seamless integration with existing infrastructure. NVIDIA NIM is a part of NVIDIA AI Enterprise, available in the AWS Marketplace.

The choice between SageMaker AI, Bedrock and EKS is not always mutually exclusive. In some cases, you may benefit from using one or more of these services together. You can start with the basics, measure everything, and iterate based on real-world performance and feedback. For example, you can use Amazon Bedrock to quickly prototype and deploy a foundation model, and then use SageMaker AI to further refine and optimize the model for better performance. This pragmatic approach will help you build robust and efficient serving infrastructure for your Generative AI applications. 

## Get Hands-On

Experience is the best teacher in model serving. You can start by using a [foundation model from Amazon Bedrock](https://catalog.workshops.aws/amazon-bedrock/en-US){:target="_blank" rel="noopener noreferrer"} to understand the basics of model serving. Then, you can progress to [fine-tune a GenAI model](https://catalog.us-east-1.prod.workshops.aws/workshops/06dbe60c-3a94-463e-8ac2-18c7f85788d4/en-US/07aiml/02-genai){:target="_blank" rel="noopener noreferrer"} in Amazon SageMaker. Advanced practitioners can use [this blog post](https://aws.amazon.com/blogs/machine-learning/use-amazon-bedrock-tooling-with-amazon-sagemaker-jumpstart-models/){:target="_blank" rel="noopener noreferrer"} to deploy models from Amazon SageMaker JumpStart and register them with Amazon Bedrock, allowing you to access them through Amazon Bedrock APIs. 

## Further Reading

* [Amazon SageMaker: Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html){:target="_blank" rel="noopener noreferrer"}.
* [Amazon Bedrock: Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html){:target="_blank" rel="noopener noreferrer"}.
* [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html){:target="_blank" rel="noopener noreferrer"}.
* [Generative AI on EKS](https://awslabs.github.io/data-on-eks/docs/gen-ai){:target="_blank" rel="noopener noreferrer"}.

## Contributors

**Author:** Guillermo Tantachuco - Principal AI Technologist 

**Primary Reviewer:** Dmitry Soldatkin - Sr. ML Specialist SA 
