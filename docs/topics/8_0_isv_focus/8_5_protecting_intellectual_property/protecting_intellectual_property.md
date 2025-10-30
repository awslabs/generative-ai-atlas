<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Protecting Intellectual Property: Yours and Your Customers'



**Content Level: 200**


## Suggested Pre-Reading

[Previous page: Secure Multi-tenancy](../8_4_secure_multitenancy/secure_multitenancy.md) 

## TL;DR

When creating generative AI applications, ISVs must consider the security of their intellectual property (IP). When doing prompt engineering, there are various categories of information brought together to generate a response:

* The system prompt (including output instructions) created by the ISV.
* Possibly dynamic RAG context brought by the ISV.
* The user's input prompt.
* Possibly dynamic RAG context brought by the user.

ISVs must protect their prompts and their proprietary contextual data. Users must protect their contextual data as well. This leads to a situation where IP security must be successfully balanced with customer trust.

The choices made here have broader impacts, which will also be briefly discussed.

## Solutions to protect IP: yours and your customers'

AWS and other cloud providers must solve for this balancing act with every managed service: it's not new to generative AI. AWS handles it in the following ways:

* Managed service accounts that AWS owns and where AWS retains responsibility for secure multi-tenancy of the managed service (like Bedrock, Lambda, DynamoDB, etc).
* A choice of connecting to the AWS services either through the public service endpoint (still within AWS's network, not on the public internet, but in AWS's public address space), or through a private link that connects the customer's VPC to the VPC of the AWS managed service.
* A guarantee to never log customer payloads, only the minimum information needed for billing and audit trail purposes. 
* A feature for customers to log their own payloads if they so choose.

In this way AWS maximizes the service security and maintainability, while also allowing customers to maximize their privacy and providing them optional payload observability.

When using Amazon Bedrock specifically, customers can opt to log all model invocations' inputs, outputs, total tokens, model, total latency, the auth principal who invoked the model, and more. This is great for enabling customers to have model usage visibility, but it introduces an IP risk for ISVs.

If the customers are running the ISV's software in the customers' own accounts and they enable Bedrock model invocation logging, then the entire populated prompt will be sent to the customer's Bedrock invocation logs. That will represent IP leakage from the ISV in the form of their proprietary prompts and context being logged in customer accounts.

In order to protect against this IP loss, there are two possible paths, each with pros and cons:

1. The ISV handles all model invocations in their own accounts.

    * Pros:
        * No IP leakage from the ISVs' proprietary prompts.
        * Broader impacts:
            * Bedrock model billing goes against the ISV's accounts and they retain the usage to increase their own AWS discount power.
            * Keeping infrastructure in the ISV account makes it easier to operate. 
            * Customers can't accidentally delete deployed resources from outside of the ISV's software.

    * Cons:
        * Many customers want to keep their data inside their own accounts.
        * ISV still needs to redact ISV IP and deliver redacted logs to the customer if they enable payload logging.

    
2. The ISV deploys application resources to customers' accounts.

    * Pros:
        * Bedrock has an API call to check if model invocation logging is enabled. ISVs can use this to refuse model invocations if logging is enabled.
        * Broader impacts:
            * Bedrock model billing goes against the customer's account which lowers the ISVs' COGS.
            * Many customers prefer this method, to keep their data in their own accounts.

    * Cons:
        * Customers' devops administrators may accidentally delete application resources (EC2 instances, Lambda functions, data stores, etc) from outside of the ISV's application, complicating support.
        * ISVs lose the bargaining power with their cloud providers by moving the infrastructure and service usage out of their accounts and into their customers' accounts.
        * ISVs will lose IP if they don't ensure model invocation logging is disabled before running invocations.
            * ISVs will need customers to deploy into dedicated accounts where the customer agrees not to enable invocation logging, complicating the customer adoption.
            * ISVs will need to deliver redacted payload logs upon customer request, removing vendor prompt template and context.

ISVs should weigh the pros and cons above against their business goals and their customers' demand signals in order to find the right path for their business. Partnering with the account team from their cloud provider can help dive deeper into the topics above.

## Further Reading

See the next section for further reading on how to apply this in practice by control and data plane architectural design.

## Contributors

### Authors

* Dave Thibault - Sr. Applied AI Architect 

* Felix Huthmacher - Sr. Applied AI Architect 

### Reviewers

* Don Simpson - Principal Technologist 

* Felix Huthmacher - Sr. Applied AI Architect 




