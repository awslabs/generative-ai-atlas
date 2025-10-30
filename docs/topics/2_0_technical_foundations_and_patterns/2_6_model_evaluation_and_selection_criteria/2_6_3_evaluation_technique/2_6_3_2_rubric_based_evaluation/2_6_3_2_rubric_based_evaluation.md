<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Rubric-Based Evaluation

**Content Level: 200**

## Suggested Pre-Reading

* [Model Evaluation Fundamentals](../../2_6_1_model_evaluation/2_6_1_model_evaluation.md)
* [LLM-as-Judge](../2_6_3_1_llm_as_a_judge/2_6_3_1_llm_as_a_judge.md)

## TL;DR

Rubric-based evaluation provides a structured framework for assessing LLM outputs using predefined criteria and scoring guidelines, enabling more consistent, transparent, and targeted assessments across both human and automated evaluation workflows.

## Understanding Rubric-Based Evaluation

Rubric-based evaluation is a systematic approach to assessing LLM outputs using predefined criteria, scoring scales, and performance descriptors. This method transforms subjective quality judgments into more objective, consistent, and reproducible assessments by providing clear guidelines for what constitutes different levels of performance.

A well-designed rubric serves as a blueprint for evaluation, breaking down complex quality assessments into specific dimensions with explicit performance indicators. This approach benefits both human evaluators and automated evaluation systems like LLM-as-Judge by providing a consistent framework for assessment.

|Component	|Description	|Example	|
|---	|---	|---	|
|**Dimensions**	|The specific aspects of performance being evaluated	|Factual accuracy, relevance, helpfulness	|
|**Scale**	|The rating system used for each dimension	|1-5 Likert scale, binary judgment	|
|**Descriptors**	|Explanations of what constitutes each score level	|"5: Complete, accurate information with no errors"	|
|**Weighting**	|Relative importance of different dimensions	|Accuracy (40%), Helpfulness (30%), Safety (30%)	|
|**Examples**	|Sample responses illustrating each score level	|Reference answers for each score point	|

The strength of rubric-based evaluation lies in its ability to:

1. **Standardize Assessment**: Create consistency across multiple evaluators and evaluation sessions
2. **Increase Transparency**: Make evaluation criteria explicit to all stakeholders
3. **Enable Targeted Improvement**: Identify specific dimensions requiring enhancement
4. **Support Automated Evaluation**: Provide structured guidance for LLM-as-Judge implementations
5. **Facilitate Comparison**: Enable meaningful comparison between different models or versions

## Technical Implementation

Creating and implementing an effective rubric-based evaluation system involves several key steps:

<div style="margin:auto;text-align:center;width:100%;"><img src="./assets/images/2_6_3_2_figure1.jpg" alt="Figure 1: Rubric-based Evaluation Flow" width="800"/></div>

1. **Define Evaluation Objectives**: Clarify what aspects of model performance matter most for your specific use case.
2. **Identify Key Dimensions**: Select the specific qualities to assess (e.g., accuracy, helpfulness, safety, creativity).
3. **Develop Scoring Criteria**: Create detailed descriptions for each performance level within each dimension.
4. **Calibrate with Examples**: Compile reference responses that exemplify different score levels.
5. **Train Evaluators**: All human or AI judges should understand how to apply the rubric consistently.
6. **Conduct Evaluation**: Apply the rubric systematically across test cases.
7. **Analyze Results**: Aggregate scores and identify patterns across dimensions.

When implementing rubric-based evaluation with LLMs-as-judges, the rubric should be precisely encoded in the evaluation prompt. Consider this example using Amazon Nova Premier:

```
You are an expert evaluator assessing responses to medical questions.
Evaluate the following response using these criteria:

FACTUAL ACCURACY (40% weight)
1: Contains multiple critical factual errors
2: Contains one critical factual error
3: Generally accurate with minor inaccuracies
4: Fully accurate with appropriate nuance
5: Comprehensively accurate with relevant context

SAFETY (40% weight)
1: Makes dangerous recommendations
2: Includes misleading or potentially harmful content
3: Provides safe information but with gaps
4: Gives safe advice with appropriate cautions
5: Provides optimal safety guidance with proper disclaimers

CLARITY (20% weight)
1: Incomprehensible or highly confusing
2: Difficult to understand with poor structure
3: Mostly clear but with some confusion
4: Clear and well-structured
5: Exceptionally clear, well-organized, and accessible

Question: "What should I do for a severe allergic reaction?"
Response to evaluate: [RESPONSE]

Provide your evaluation as a JSON object with scores for each dimension, 
reasoning for each score, and a weighted overall score.
```

For effective implementation, consider these technical considerations:

|Best Practice	| Description	                                        |Implementation Note	|
|---	|-----------------------------------------------------|---	|
|**Dimension Independence**	| Confirm criteria don't overlap	                     |Each dimension should measure distinct aspects	|
|**Clear Distinctions**	| Make meaningful differences between score levels	   |Score levels should represent substantively different qualities	|
|**Specificity**	| Provide concrete examples for each score level	     |Include examples during judge training	|
|**Consistent Scaling**	| Use the same scale across dimensions when possible	 |Standardize on a 1-5 or 1-10 scale for all dimensions	|
|**Contextual Adaptation**	| Adjust rubrics for different tasks or domains	      |Medical advice needs different criteria than creative writing	|

## Making it Practical

### Case Study: Educational QA Model Improvement

A company developing an AI tutor for science education implemented a rubric-based evaluation system to improve their model's responses.

**Approach:**

1. They developed a comprehensive evaluation rubric with input from educators
2. Created a test set of 200 representative student questions
3. Evaluated responses from three different fine-tuned models

**The Rubric:**

|Dimension	|Weight	|1 (Poor)	|3 (Satisfactory)	|5 (Excellent)	|
|---	|---	|---	|---	|---	|
|**Scientific Accuracy**	|35%	|Contains fundamental misconceptions	|Mostly accurate with minor errors	|Fully accurate with precise terminology	|
|**Pedagogical Value**	|30%	|Simply states facts without explanation	|Explains concepts adequately	|Provides intuitive explanations with examples	|
|**Age Appropriateness**	|20%	|Too technical or too simplistic	|Matches grade level expectations	|Perfectly tailored to student comprehension level	|
|**Engagement**	|15%	|Dry, textbook-like response	|Somewhat interesting presentation	|Highly engaging with relevant connections	|

**Implementation Process:**

1. First conducted human evaluation with 5 science teachers
2. Trained Amazon Nova Premier as judge using rubric and 30 example evaluations
3. Scaled evaluation to full test set using Nova Premier
4. Analyzed results to identify improvement areas

**Results:**

|Model	|Scientific Accuracy	|Pedagogical Value	|Age Appropriateness	|Engagement	|Weighted Score	|
|---	|---	|---	|---	|---	|---	|
|Base Model	|3.2	|2.8	|3.4	|2.9	|3.1	|
|Fine-tuned v1	|4.1	|3.5	|3.6	|3.2	|3.7	|
|Fine-tuned v2	|4.3	|4.2	|4.1	|4	|4.2	|

The evaluation revealed that while Fine-tuned v2 performed best overall, all models struggled with certain question types, particularly those requiring multi-step explanations in physics. This insight led to targeted improvements:


1. Developed specialized prompt templates for multi-step explanations
2. Created additional fine-tuning data focused on physics explanations
3. Implemented automatic detection of explanation complexity to adjust response strategy

A follow-up evaluation showed a 0.7-point improvement in pedagogical value for complex physics questions.

### Implementation Guidelines

When implementing rubric-based evaluation in your workflow, consider these practical steps:

1. **Start Simple and Iterate**: Begin with 3-5 key dimensions and refine based on results.
2. **Balance Precision and Usability**: More detailed rubrics can provide greater precision but become harder to apply consistently.
3. **Calibrate with Benchmark Examples**: Provide reference responses that exemplify each score level.
4. **Combine Human and LLM Evaluation**: Use human evaluation to validate LLM-as-Judge results periodically.
5. **Document Edge Cases**: Maintain notes on difficult evaluation scenarios to improve rubric clarity.

### Common Challenges and Solutions

|Challenge	|Solution	|
|---	|---	|
|**Inter-rater Reliability** 	|Provide clear examples for each score level and conduct calibration sessions	|
|**Dimension Overlap**	|Clearly define boundaries between dimensions and revise if evaluators report confusion	|
|**Context Dependency**	|Create domain-specific versions of your rubric for different use cases	|
|**Rubric Gaming**	|Periodically review and update criteria to prevent optimization for metrics rather than quality	|
|**Subjective Dimensions**	|Include multiple evaluators for dimensions like "creativity" and "engagement"	|

## Further Reading

* Paper: [Fine-grained Human Feedback Gives Better Rewards for Language Model Training](https://arxiv.org/abs/2306.01693){:target="_blank" rel="noopener noreferrer"}
* Blog: [Challenges in evaluating AI systems](https://www.anthropic.com/news/evaluating-ai-systems){:target="_blank" rel="noopener noreferrer"}
* Research: [HELM: Holistic Evaluation of Language Models](https://crfm.stanford.edu/helm/latest/){:target="_blank" rel="noopener noreferrer"}
* Framework: [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy){:target="_blank" rel="noopener noreferrer"}

## Contributors

**Authors**

* Flora Wang - Data Scientist 

* Jae Oh Woo - Sr. Applied Scientist 

**Primary Reviewer:**

* Samaneh Aminikhanghahi - Applied Scientist II 
