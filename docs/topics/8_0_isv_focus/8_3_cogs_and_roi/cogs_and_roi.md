<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# COGS and ROI

**Content Level: 100**

## Suggested Pre-Reading

[Previous page: Sell with AWS](../8_2_sell_with_aws/sell_with_aws.md) 

## TL;DR

Cost of goods sold (COGS) and return on investment (ROI) are just as critical to understand for AI projects as they are for traditional software projects. However, not all product owners understand how to estimate COGS and ROI for AI projects. This section aims to provide guidance to accelerate that understanding.

## Working backwards from ROI from the beginning

As with any software project, starting with a valuable use case is a key factor to eventual success. Without delivering value, software isn't of much use to the people who pay to build it or the people who pay to use it.

Like other projects ISVs take on, AI projects can be boiled down to two major categories of value delivery, with some common examples of use cases that are widely applicable across industry verticals:

1. Operational efficiency (lower expenses)
    * intelligent document processing & other process automation
    * code generation & understanding
    * social media analytics
    * productivity & chatbots, like:
        * helpdesk support case acceleration
        * information search, extraction, summarization, storage, and retrieval
        * external-facing bots for support case deflection
2. Product sales (higher revenue)
    * new AI products & features with attached revenue (like any of the ideas above)
    * marketing content generation to increase funnel & conversion rates
    * recommendation systems (with traditional recommender models, not LLMs, doing the number crunching) to increase funnel & conversion rates, and possibly LLMs to create content around the recommendations.

Ultimately profitable business decisions boil down to increased revenue and/or reduced expenses, both of which increase profits.

To that end, when estimating ROI, don't get bogged down in hard-to-define value metrics. Keep it simple and only count the metrics that are easy to count and concrete, like shorter time to complete currently manual processes. Projects should have positive ROI without needing to find hard-to-measure value metrics beyond the easy-to-measure ones. For example, for a support case acceleration system, measuring time to case resolution is an easy proxy for saving the time of support engineers. You don't also need to 

For example, in the case of helpdesk acceleration, if the average time spent to case resolution goes down from days or hours to minutes, then count the time savings for the support staff in closing cases faster. Don't worry about the additional ROI value represented by increased customer satisfaction or lower ticket queue depth. Those are harder to measure. The time savings alone should be in the 20X-100X ROI range depending on the cost of the workers. A defensible single ROI metric should be enough to justify AI projects without including more questionable metrics. Estimate the easily measurable metrics and don't dilute the value proposition or waste time with weaker metrics. Time to market is more valuable than the harder-to-measure metrics for ROI. Then when the harder-to-measure benefits come through, they are in addition to the ROI used to justify the project, and they didn't slow the project down.

By saving your valuable employees time by avoiding lower-value work, you free them up to deliver higher-value work for your company. It's easy to see AI automation as an opportunity to earn immediate ROI. However, thinking in terms of longer-term value, superpowered employees may deliver orders of magnitude more ROI than settling for the immediate ROI, and allow companies to start dramatically outcompeting in their chosen business space.

## Estimating COGS

As for estimating costs, the biggest difference from estimating non-AI workloads is the uncertainty of model invocation costs for a particular use case. The easiest way to estimate this is to enable model invocation logging and proceed with prompt engineering work. Then you will have counts of fully-loaded model invocations with not only user prompt tokens, but also RAG context and system prompts.

First get your prompts working the way you want them, then the token counts will stabilize. Until then, expect them to be in flux. Once you get prompts working, you can see the total average inputs and outputs and extrapolate by the per-token costs for the selected model. Then you can confidently estimate the model invocation costs for your application at higher scales of usage. 

Another AI-specific cost is the vector index component. The vector index stores chunks of text, a long list of floating point numbers that describes the text (the vector embedding), and any associated metadata you want to store with the data. Vector indexes can be hosted using common systems like OpenSearch or PostgreSQL. Therefore those may be better understood costs for ISVs than they may initially realize.

One difference to consider is the size of the vectors as a large percentage of the index records. A common vector size is an array 1024 dimensions long, and each spot in the array holds a 32-bit floating point number by default. That means that every record in your vector index may have 1024 * 4 bytes (32 bits/8 bits per byte). The vector size is the same for a chunk whether you passed in one word or the maximum number of tokens for that embedding model's attention window.

Bigger is not necessarily better with embedding models and dimension sizes. For example, Cohere models were top-10 on the [HuggingFace Massive Text Embedding (MTEB) leaderboard](https://huggingface.co/spaces/mteb/leaderboard){:target="_blank" rel="noopener noreferrer"} for many months. They use 512 dimension vectors. Customers should test for their use case and use the most efficiently sized model that meets their retrieval accuracy needs, because longer dimensions means more space for every record in the vector index, and slower performance at runtime to calculate longer vectors on incoming search queries. 

As with other topics, evaluations will be critical to help pick the right embedding model and chunking strategy.

## Further Reading

  * [AWS Pricing Calculator](http://calculator.aws/#/){:target="_blank" rel="noopener noreferrer"} for estimating cost of workloads.

## Contributors

### Authors

* Dave Thibault - Sr. Applied AI Architect 

* Felix Huthmacher - Sr. Applied AI Architect 

### Reviewers

* Don Simpson - Principal Technologist 

* Felix Huthmacher - Sr. Applied AI Architect 

