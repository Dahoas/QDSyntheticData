# [Impossible Distillation: from Low-Quality Model to High-Quality Dataset & Model for Summarization and Paraphrasing](https://arxiv.org/abs/2305.16635)


## Summary

Distills data from a weak language model to improve itself via strong supervision from a critic. The tasks are paraphrasing and summarization.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

- Critiquing
- Self-training

## Benchmarks

Tasks evaluated.

- ParaBank1/2
- ChatGPT-Para

## Metric Results

- Paraphrase similarity is measured using BLEU. NLI is also used to assess if statements are contradictory. ROUGE isalso used to measure dissimilarity
- Filtering is done by removing all pairs which have entailment above a threshold and keeping the response with the highest entailment score

## Paper Tags

1. JUDGE
2. SYNTH
