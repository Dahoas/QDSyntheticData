# [ZeroGen: Efficient Zero-shot Learning via Dataset Generation](https://arxiv.org/abs/2202.07922)

## Summary

This paper proposes ZeroGen, where given a downstream task, run unsupervised synthetic training data generation from scratch using carefully designed task-specific prompts, then training a much smaller model on this synthetic data. They evaluate quality in terms of correctness, and find increasing diversity via decoding schemes decreases performance. 

## Relevance to survey topic (1-5)

Relevance: ?

## Algorithms

- baselines
  - zero-shot prompting of PLMs
  - Supervised training on smaller model
- Decoding modes
  - Greedy
  - Top k = 5/40/80
  - Nucleus p=0.9
- Self-BLEU For diversity

## Benchmarks

- Text classification
  - IMDb
  - SST-2 ("low-resource")
- Natural Language Inference
  - QNLI
  - RTE ("low-resource")
- QA
  - SQuAD1.1
  - AdversarialQA

## Metric Results

- ZeroGen is better than zero-shot prompting on LLM because the models are task-specific, and improved inductive bias (narrowing the search space)
- ZeroGen outperforms fully-supervised human-annotated data with low-resource datasets because of larger dataset size
- That GPT-2 < GPT-Large < GPT2-XL is confirmed by the fact that data generated from these models increases in quality, as shown by downstream model performance. 
- Self-BLEU for diversity metric - Found diversity inversely correlated with model performance


## Other comments

- high sensitivity WRT prompts used to generate data
