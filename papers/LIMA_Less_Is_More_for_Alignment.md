# [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206)

## Summary

Shows Llama-2 70B can beat davinci-003 in preference win-rates with just 1000 high-quality instruction examples. Beyond this performance diminishes without expanding dataset diversity and quality. They also do ablations on Ablations on Data Diversity, Quality, and Quantity.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

Simply handcrafts extremely high-quality insruction training dataset by going through existing datasets.

## Benchmarks

- Alpaca

## Metric Results

- Quality is measured either via pairwise comparisons or on a likert scale measured by humans or gpt.
- diversity is measured based on instruction topic
