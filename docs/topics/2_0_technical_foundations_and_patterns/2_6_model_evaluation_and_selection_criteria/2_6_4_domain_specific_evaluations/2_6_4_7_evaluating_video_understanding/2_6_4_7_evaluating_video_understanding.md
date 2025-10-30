<!-- 
 Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 SPDX-License-Identifier: CC-BY-SA-4.0
 -->

# Evaluating Video Understanding Capabilities of Multi-Modal LLMs

**Content Level: 200**

## Suggested Pre-Reading

* [Evaluation Techniques](../../2_6_3_evaluation_technique/2_6_3_evaluation_techniques.md)

## TL;DR

Video understanding models extract insights from complex visual-temporal patterns. The field divides into two main categories:

**Short-Form Analysis:** Videos from platforms like TikTok and YouTube Shorts contain high-density information compressed into brief segments. Models should process every frame, as missing content can result in significant information loss.

**Long-Form Analysis:** Content such as movies, TV shows, sports broadcasts, and instructional videos exhibit temporal coherence and redundancy across extended sequences. Models should track narrative progression, recall past events, and maintain contextual memory over longer durations.

This section provides a comprehensive framework for evaluating Multimodal Large Language Model (LLM).


## 1. MLLM for Video Understanding

The rise of Multi-modal Large Language Models (MLLMs) has significantly advanced video comprehension by enabling models to process both text and visual inputs within a unified framework. Recent advancements have led to models like Amazon Nova Pro supporting expanded context windows, accommodating 300K combined text and visual tokens, thereby enhancing their ability to process longer video sequences. Despite this progress, there remains a gap in systematically evaluating MLLMs on long-form video tasks, especially in diverse real-world applications.


## 2. Benchmarking Datasets

Benchmarking plays a critical role in evaluating MLLMs for video comprehension. Video benchmarking datasets generally have videos, questions and ground truth answers. Often the benchmark datasets have answer decoys with the correct ground truth answer as one of the decoys and the task of the LLM is to analyze the video and choose the correct answer option given the question. Sometimes the datasets also provide audio transcripts which can be further leveraged by MLLMs for better video understanding.


## 3. Evaluation Framework

Video understanding evaluation can be categorized into two primary approaches:

1. **Open Comprehension Evaluation:** MLLMs generate free-form responses without answer options, requiring the model to produce relevant content solely from video (or additionally audio) understanding.
2. **Multiple-Choice Evaluation:** Models select from provided answer decoys, testing their ability to discriminate between correct and incorrect options based on video content.

### 3.1. Open Comprehension Evaluation

**LLM as a judge evaluation:** Large Language Models (LLMs) have emerged as powerful tools for evaluating Multimodal Large Language Models (MLLMs) on video understanding tasks. This approach offers several advantages over traditional metrics-based evaluation, providing nuanced assessment of model capabilities across various dimensions of video comprehension.

|Evaluation Approach	|Description	|Inputs Required by LLM Judge	|Key Assessment Dimensions	|Outcome Format	|
|---	|---	|---	|---	|---	|
|**Response Quality Assessment**	|Compare MLLM responses to ground truth answers	|Video question, MLLM response, ground truth answer	|Semantic similarity, factual accuracy, reasoning quality	|Numerical scores	|
|**Multimodal Grounding Verification**	|Verify responses are grounded in visual evidence using keyframe descriptions	|Video keyframe descriptions, MLLM response, question	|Hallucination detection, visual fidelity, evidence-based reasoning	|Pass/fail or graded assessment	|
|**Comparative Evaluation**	|Conduct head-to-head comparisons between different MLLMs or against ground truth	|Video question, responses from multiple MLLMs (or MLLM response and ground truth)	|Overall quality, relative performance	|Win/lose/tie verdicts	|
|**Reasoning Path Analysis**	|Assess quality and coherence of reasoning chains in responses	|Video question, MLLM response with reasoning chain, optional keyframe descriptions	|Logical consistency, inference validity, reasoning steps	|Qualitative or numerical assessment	|
|**Reverse Scoring**	|Ask LLM judge to answer the question using only MLLM-generated video descriptions	|Question, answer options, MLLM-generated video descriptions (without original video)	|Description completeness, information sufficiency, critical detail capture	|Correct/incorrect (binary) or accuracy score	|

### Example prompts: 


Prompt to compare MLLM responses to ground truth answers

```
## Task ##
You are an expert judge evaluating a candidate response to a video-related query from a multimodal model. Compare the candidate answer with the provided ground truth answer and assess the candidate responses' accuracy, coherence, and completeness. The question itself, the correct ’ground truth’ answer, and the candidate answer will be provided to you.

## SCORING SYSTEM ##
Score 0: No similarity with given ground ruth- Completely incorrect answer
Score 1: Low similarity with given ground truth- Largely incorrect answer
Score 2: High similarity with given ground truth— Largely correct answer
Score 3: Complete similarity with given ground truth— Entirely correct answer


## EVALUATION CRITERIA ##
Focus solely on semantic similarity with the ground truth answer(meaning)
Ignore grammatical differences
Provide only a single integer score (0, 1, 2, or 3)


## OUTPUT FORMAT ##
You should strictly follow this output format.
<score>[single integer 0-3]</score>
<reasoning>[Your reasoning for the score]</reasoning>

Here is the input question, groundtruth answer and candidate answer to be evaluated.
Question: {QUESTION}
Groundtruth answer: {GT_ANSWER}
Candidate answer: {CANDIDATE_ANSWER}
```


Prompt for reverse scoring 

```
## TASK DESCRIPTION ##

You are an AI assistant tasked with:
Evaluating the semantic similarity between a candidate answer and a correct answer
Verifying groundedness using multiple sources:
    1. Key frame descriptions (visual information)
    2. Audio transcript (spoken information)

## SCORING SYSTEM ##
Assign a score based on the following semantic similarity scale:
Score 0: No similarity - Completely incorrect answer 
Score 1: Low similarity - Largely incorrect answer 
Score 2: High similarity - Largely correct answer
Score 3: Complete similarity - Entirely correct answer,


## EVALUATION CRITERIA ##

Primary Criteria: 
1. Focus on semantic similarity (meaning)
2. Ignore grammatical differences 
3. Additional details in candidate answer are acceptable if they are:
    3.1 Grounded in the key frame descriptions OR audio transcript
    3.2 Don't contradict the groundtruth answer
4. Groundedness Rules:  If candidate answer contains extra details not in groundtruth, 
    4.1 Check if supported by key frames (visual evidence)
    4.2 Check if supported by audio transcript (verbal evidence)
    4.3 If supported by either source: Don't penalize
    4.4.If contradicted by either source: Lower the score
    4.5 If unverifiable through both sources: Lower the score
    4.6 Cross-Modal Verification: 
        Consider both visual and verbal information 
        Higher confidence in details confirmed by both modalities 
        Resolve any conflicts between visual and audio information
 

## OUTPUT FORMAT ##
Your response should strictly follow this format:
<score>single integer 0-3</score>
<reasoning>Brief justification (2-3 sentences explaining the score and groundedness assessment)</reasoning>
```



**Lexical Overlap  Metrics:**
Traditional lexical overlap metrics like BLEU and ROUGE offer fast, interpretable evaluations but struggle to capture the semantic flexibility of valid responses in multimodal contexts. More recent approaches like BERTScore and Answer Equivalence (BEM) aim to align closer with human judgment by focusing on meaning, paraphrase tolerance, and contextual relevance. The table below compares these metrics in the context of video-based LLM evaluation, highlighting their strengths, limitations, and best-fit

|Metric	|Description	|Pros	|Cons	|When to use	|
|---	|---	|---	|---	|---	|
|**BLEU**	|Measures *n*-gram precision (1–4) between generated and reference responses	|- Fast and well-known
- Penalizes irrelevant or short outputs	|- Rigid on phrasing
- Ignores semantics
- Fails with diverse valid answers	|The output is short, well-bounded (e.g., object names, actions) with predictable phrasing	|
|**BERTScore**	|Measures semantic similarity using contextual embeddings between output and reference	|- Captures paraphrasing
- Good for long, descriptive answers
- Language-agnostic	|- Doesn’t penalize hallucinations
- May over-credit semantically similar but incorrect info	|The model generates open-ended descriptions or insights that may vary in wording	|
|**BEM (Answer Equivalence)**	|Trained BERT-based model predicts if the answer is correct given question & reference	|- Sensitive to question relevance
- Credits semantically correct answers
- Human-aligned	|- Requires labeled data
- More complex setup
- Task-specific	|You care about semantic correctness and completeness of generated answers from video input	|
|**ROUGE**	|Measures recall of overlapping *n*-grams or sequences between output and reference	|- Captures key idea recall
- Tolerant to verbosity
- Common in summarization	|- Lexical-only
- Doesn’t reward paraphrasing
- Inflated scores for verbose outputs	|You want to verify if the model captured most relevant content from a long video	|




## Making It Practical

### 1. Configure Frame Sampling Strategy

* Short-form videos: Uniform sampling at 1-2 fps
* Long-form videos: Adaptive sampling with higher density at scene changes
* Prioritize uniform sampling over computationally heavy sampling techniques like CLIP or other deep-learning-based methods.
* If models just allow one image as input try making a grid from multiple images and using the grid as a single image input.

### 2. Design Evaluation Payload Format

* Structure consistent payloads with video metadata and ground truth answers
* Include timestamps for key events and support both multiple-choice and open-ended formats
* Its better choice to read images and videos directly from S3 if the model payload allows, which will make the payload much smaller in memory.

#### Implementing Evaluation Methods

#### 1. Multiple-Choice Evaluation

* Format prompts with clear questions and standardized answer options
* Define explicit instructions and consistent response extraction methods

#### 2. LLM as Judge Evaluation

* Use structured prompting templates with clear scoring criteria
* Include keyframe descriptions to verify visual grounding

#### 3. Batch Inference Implementation

* Process similar-length videos in batches to maximize throughput
* Implement parallel processing for frame extraction
* Group videos strategically to optimize GPU/CPU utilization

## Contributors

**Authors**

* Baishali Chaudhury - Applied Scientist II 
