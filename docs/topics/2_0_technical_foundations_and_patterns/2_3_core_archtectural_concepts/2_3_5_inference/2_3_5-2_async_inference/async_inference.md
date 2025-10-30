<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Asynchronous Inference in Generative AI

**Content Level: 200**


## Suggested Pre-Reading

 * [Responses: Understanding Model Outputs](../../../2_1_key_primitives/2_1_2_model_outputs/2_1_2_model_outputs.md)
 * [Online Inference](../2_3_5-1_online_inference/online_inference.md)

## TL;DR

Asynchronous inference allows the requestor to continue working without waiting for model predictions to complete - similar to how a restaurant server can take an order and attend to other tables while the kitchen prepares the food. When results become available, the requestor is notified. This non-blocking approach significantly improves efficiency, especially when processing large datasets.
For example, in medical imaging, traditional sequential processing would analyze patient scans one after another, creating a bottleneck. Instead, asynchronous inference allows healthcare systems to evaluate multiple diagnostic images (X-rays, CT scans, and MRIs) concurrently - just like that efficient server handling multiple orders at once. This parallel processing not only accelerates the diagnostic workflow but also enables faster patient care decisions.

## Understanding Asynchronous Inference

Instead of processing single prompts in real-time, asynchronous inference allows you to submit multiple prompts as a group, which are then processed asynchronously. This approach is particularly valuable when dealing with large volumes of requests or when immediate responses aren't necessary. Examples include: asynchronous embedding generation, LLM-as-judge evaluations, entity extraction, large-scale text classification, and bulk content analysis. For instance, businesses can use batch inference to generate embeddings for vast document collections, classify extensive datasets, or analyze substantial amounts of user-generated content efficiently.
At the heart of asynchronous inference are three main phases that work in harmony to manage the flow of requests and responses:

* **Data preparation:** Asynchronous inference requires careful preparation and validation of input data before processing begins. You should review the token limits for your chosen model and adjust your input text to fit within these limits. It’s important to identify the specific input format and data structure the model expects. Before processing your entire dataset, test with a small sample. This helps identify any formatting issues or processing errors early.
* **Job management:** Once a request enters the system, job management takes over. This critical component tracks the status of ongoing inference tasks, providing unique identifiers that allow clients to check on their requests' progress. It also handles the complexities of retry logic and error management, ensuring that tasks are completed successfully even in the face of temporary setbacks.
* **Output collection and analysis:** Once an inference task is complete, this phase temporarily holds onto the finished results, allowing for efficient retrieval when clients are ready to access them. It also manages the lifecycle of these results, ensuring that they're available when needed but don't consume resources indefinitely. You can then integrate those results into existing workflows or analytics systems.

## Making it Practical

Asynchronous inference presents itself as a compelling approach to handle diverse data processing tasks. For instance, call transcript summarization is a common use case for call center operations. As the volume of call data grows, traditional analysis methods struggle to keep pace, creating a demand for a scalable solution. Processing substantial volumes of text transcripts in batches has become an important task for businesses, in any industry, seeking to extract valuable insights from customer interactions. You can perform asynchronous inference using various features available in both Amazon SageMaker AI and Amazon Bedrock. While both Amazon Bedrock and Amazon SageMaker AI enable the development of ML and generative AI applications, they serve different purposes. This [decision guide](https://docs.aws.amazon.com/decision-guides/latest/bedrock-or-sagemaker/bedrock-or-sagemaker.html){:target="_blank" rel="noopener noreferrer"} will help you understand which of these services is the best fit for your needs, including scenarios in which both services can be used together to build generative AI applications.

### Amazon SageMaker AI

SageMaker AI provides multiple inference options so that you can pick the option that best suits your workload:

* [Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html){:target="_blank" rel="noopener noreferrer"}: Asynchronous inference is ideal when you want to queue requests and have large payloads with long processing times. Asynchronous Inference can support payloads up to 1 GB and long processing times up to one hour. You can also scale down your endpoint to 0 when there are no requests to process.
* [Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html){:target="_blank" rel="noopener noreferrer"}: Batch transform is suitable for offline processing when large amounts of data are available upfront and you don’t need a persistent endpoint. You can also use batch transform for pre-processing datasets. It can support large datasets that are GBs in size and processing times of days.

### Amazon Bedrock

To implement asynchronous inference in AWS you can leverage [batch inference in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html){:target="_blank" rel="noopener noreferrer"}. It efficiently processes large volumes of data using foundation models (FMs) where instantaneous results are not always a requirement.
One of the key advantages of batch inference is its cost-effectiveness. Amazon Bedrock offers select FMs for batch inference at 50% of the On-Demand inference price. Organizations can process large datasets more economically because of this significant cost reduction, making it an attractive option for businesses looking to optimize their generative AI processing expenses while maintaining the ability to handle substantial data volumes. 
Additionally, please keep in mind that job limits for batch inference can differ based on the model and region you're working with in Amazon Bedrock, as described in the [Amazon Bedrock service-level quotas.](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#limits_bedrock){:target="_blank" rel="noopener noreferrer"}

## Get Hands-On

This blog post offers a solution to handle the job limits for batch inference: [Automate Amazon Bedrock batch inference: Building a scalable and efficient pipeline](https://aws.amazon.com/blogs/machine-learning/automate-amazon-bedrock-batch-inference-building-a-scalable-and-efficient-pipeline/){:target="_blank" rel="noopener noreferrer"}. It guides you through implementing a queue management system that automatically monitors available job slots and submits new jobs as slots become available.

## Further Reading

* [Amazon Bedrock or Amazon SageMaker AI?](https://docs.aws.amazon.com/decision-guides/latest/bedrock-or-sagemaker/bedrock-or-sagemaker.html){:target="_blank" rel="noopener noreferrer"}
* [Amazon SageMaker AI: Batch transform for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html){:target="_blank" rel="noopener noreferrer"}
* [Amazon SageMaker AI: Asynchronous inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html){:target="_blank" rel="noopener noreferrer"}
* [Amazon Bedrock: Process multiple prompts with batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html){:target="_blank" rel="noopener noreferrer"}.
* [Amazon Bedrock offers select FMs for batch inference at 50% of on-demand inference price](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-bedrock-fms-batch-inference-50-price/){:target="_blank" rel="noopener noreferrer"}.
* [Enhance call center efficiency using batch inference for transcript summarization with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/enhance-call-center-efficiency-using-batch-inference-for-transcript-summarization-with-amazon-bedrock/){:target="_blank" rel="noopener noreferrer"}.

## Contributors

**Author:** Guillermo Tantachuco - Principal AI Technologist 

**Primary Reviewer:** Dmitry Soldatkin - Sr. ML Specialist SA 
