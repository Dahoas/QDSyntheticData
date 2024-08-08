# [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://arxiv.org/abs/2403.16952)

## Summary

Predicts pre-training validation loss on components of training mixture via exponential of linear combination of mixture ratios: $L_i(r_1,...,r_M) = c_i + k_iexp(\sum_{j=1}^Mt_{i,j}r_j)$ ($r_j$ is mixture ratio, $c_i, k_i, t_{i,j}$ are fit parameters). Achieves same loss after training for 100B tokens on SlimPajama as 48% more training on default mixture.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

Just different proportions of pre-defined data sources.

## Benchmarks

Tasks evaluated.

pre-training validation loss.
- pile-cc
- github

## Metric Results

- No quality metric
- Diversity measured via mixture ratios

