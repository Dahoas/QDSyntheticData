# [LMD3: Language Model Data Density Dependence](https://arxiv.org/abs/2405.06331)

## Summary

This work develops a framework to estimate the density of data around a certain point, with the aim being to understand whether training data density around a testing point leads to improved performance. They propose a simple method of synthetically increasing the density around a data point by paraphrasing the data. Unsurprisingly, they find that by increasing the density around a testing data point leads to improved performance.

## Relevance to survey topic (1-5)

Relevance: 1

## Algorithms

- KDE
- DEANN

## Benchmarks

- MMLU

## Paper Tags

None

## Other comments

This probably isn't new information, but this work is a good reminder that paraphrasing is a good method for generating synthetic data.