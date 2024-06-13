# [Autonomous Data Selection with Language Models for Mathematical Texts](https://openreview.net/forum?id=bBF077z8LF)

ID:210

## Summary

Autonomous Data Selection (AutoDS) is a strategy to autonomously evaluate the mathematical quality and educational value of content. 
It uses a base LM for autonomous data selection to do continual pretraining for proficiency in mathematical reasoning.
It's a zero-shot prompting strategy to score the data relevance and value using a softmax function over logits for ‘YES’ and ‘NO’ tokens responses to meta-prompts. 
They believe this quantitative score function reduces the need for extensive data labeling for SFT and RLHF/DPO alignment or classifier training.
Introduces the open-source [AutoMathText](https://huggingface.co/datasets/math-ai/AutoMathText) dataset to address shortage of labeled high-quality mathematical training resources. 

## Relevance to survey topic (1-5)

Relevance: 2

## Algorithms

NA

## Benchmarks

-  Evaluates on MATH, GSM8K, BIG-Bench Hard (BBH) 

## Metric Results

- How is quality measured? Performance on benchmarks below
- How is diversity measured? NA
- Continual pretraining results:

Experiments: 

Continually pretrained a 7B-parameter Mistral LM over 3 epochs (taking LM-Scores of 0.75 to 1.). \\
MATH test accuracy post continual pretraining: OpenWebMath went from 10.50 to 13.68. \\
MATH test accuracy after fine-tuning on MetaMathQA: 26.98 to 28.06. 

They compare with baselines on pretrained Mistral-7B models continually pretrained for one epoch with approximately 2.5 billion tokens (taking LM-Scores of 0.6 to 1.) 
Results are a few percentage points above baselines for MATH (5-shot) GSM8K (5-shot) BIG-Bench Hard (3-shot). 

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. REASONING
2. DATASET - not synthetic, it's a curation method. 
3. JUDGE

## Other comments

Focus on autonomous content evaluation without the necessity for alignment fine-tuning or classifier training and an increase in pretraining token efficiency for this compared to previous continual pretraining works. 

Preprompts model, then asks questions like: \\
1. Does the text exhibit elements of mathematical intelligence? Respond with YES or NO\\
2. Is the text suitable for educational purposes for YOURSELF in the field of mathematics?\\
Respond with YES or NO

LLM judge is Qwen-72B base model. \\
Data sources are  Common Crawl (specifically, the OpenWebMath subset, arXiv (via the RedPajama dataset), and GitHub (Algebraic Stack dataset subset of the Stack dataset). - over 200GB of data

