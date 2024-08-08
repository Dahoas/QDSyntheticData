# [Texygen: A Benchmarking Platform for Text Generation Models](https://arxiv.org/abs/1802.01886)

## Summary

Texygen is a fully open-sourced benchmarking platform for text generation models, maintaining a variety of metrics that evaluate the diversity, quality, and consistency, proposing multiple metrics are required to fully evaluate generated text. It provides both baseline models and automatically computable evaluation metrics. The metrics include “Document Similarity base Metrics” such as BLEU and EmbSim, “Likelihood-based Metrics” such as NLL-oracle and NLL-test, and a “Divergence-based Metric” called Self-BLEU.

## Relevance to survey topic (1-5)

Relevance: 2

- good to be aware of, but it's more GAN-centric and the metrics are more embedding-based

## Algorithms

Mostly benchmarks GAN techniques

## Metric Results

\* denotes proposed by this paper

- Document Similarity-based Metrics
  - BLEU
  - \*EmbSim (document similarity based on embeddings)
- Likelihood-based Metrics
  - NLL-oracle (how good generated data is fitted by oracle language model)
  - \*NLL-test (capacity to fit real test data)
- Divergence Metrics
  - \*Self-BLEU: average BLEU of each sentence (higher is less diversity)
