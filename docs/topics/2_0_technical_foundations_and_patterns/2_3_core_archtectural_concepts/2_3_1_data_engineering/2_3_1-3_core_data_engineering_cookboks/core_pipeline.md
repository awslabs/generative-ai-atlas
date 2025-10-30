<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Data Engineering Cookbooks
We have now discussed the important concepts involved in creating and evaluating instruction-tuning datasets. These cookbooks offer code and guidelines to assist AI engineers in constructing practical data pipeline components that can be easily integrated into their projects.

## Prerequisites
While the code examples are primarily written in Python, the concepts can be adapted to any programming language, Model Providers or AWS services such as Glue using Spark or Ray engine.

### Semantic Deduplication Cookbook
Semantic similarity takes a different approach by focusing on the meaning of text to identity near-duplicates.

<div style="margin:auto;text-align:center;width:100%;">
  <img src="../2_3_1-3_core_data_engineering_cookboks/assets/data_formats-semantic-similarity.svg" alt="Responsible AI Dimensions" width="1000" style="margin: auto; text-align: center;"/>
</div>
In the previous section, we looked at different techniques that AI engineers use to improve data quality. In this cookbook, we will provide a practical code example of how to deduplicate datasets using the SemHash tool.
SemHash is a lightweight Python library that AI engineers can leverage in their data processing pipeline using semantic similarity.
#### How it works
At its core, the system takes in a collection of strings or dictionaries. You begin by initializing a model with a set of reference documents. This set is then used to deduplicate an incoming batch of documents. Any incoming document that is similar to a document from the reference set will be removed and stored separately, along with its approximate duplicates from the reference set.


Installation:
```shell
pip install semhash
pip install datasets #install huggingface datasets
pip install pandas
```

In this cookbook we are using [Hugging Face](https://huggingface.co/docs/datasets/en/index){:target="_blank" rel="noopener noreferrer"} datasets. We deduplicating a single dataset.
```python
from datasets import load_dataset
from semhash import SemHash
import pandas as pd

# Load a dataset
dataset = load_dataset("ag_news", split="train")
text = dataset["text"]
#optional count records
#len(text) 120000 records
# Initialize a SemHash instance
hash = SemHash.from_records(records=text)
# Deduplicate the texts
deduplicated_texts = hash.self_deduplicate().selected
#count dedup records
len(deduplicated_texts)
#output is 106900
#save dataset
df = pd.DataFrame(deduplicated_texts, columns=["text"])
df.to_csv("deduped_file.csv")
```

#### Further Reading:
[SemHash](https://github.com/MinishLab/semhash){:target="_blank" rel="noopener noreferrer"}


## Contributors

Author/s:

 - Tonny Ouma - Sr Applied AI Architect 

Primary Reviewers:

 - Randy DeFauw - Senior Principal SA 
 - Felix Huthmacher - Senior Applied AI Architect 