# [Forcing Diffuse Distributions out of Language Models](https://arxiv.org/abs/2404.10859)

## Summary

Fine-tunes llms to generate more diverse target distributions by training on the target $p^*$ via the loss: $\mathcal{L}(p_\theta) = -\sum_{y \in \mathcal{T}} p^*(y|x)log p_\theta (y|x)$ which is equivalent to minimizing KL divergence to some training data $\mathcal{T}$. They find diffuse training generalizes OOD to other tasks e.g. diversity of names improves diversity of fruits. They use this to construct a synthetic dataset of biographies.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

- Distribution matching to target distribution $p^*$ (minimizes KL with $\mathcal{L}(p_\theta) = -\sum_{y \in \mathcal{T}} p^*(y|x)log p_\theta (y|x)$ training objective)

## Benchmarks

Tasks evaluated.

- random number generation
- fruit generation
- biography generation

## Metric Results

- Quality is not measured
- Diversity is measured via 
  - entropy of output samples
  - coverage (number of unique samples)