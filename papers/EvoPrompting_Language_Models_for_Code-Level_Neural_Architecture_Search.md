# [EvoPrompting: Language Models for Code-Level Neural Architecture Search](https://arxiv.org/abs/2302.14838)

## Summary

Runs an LLM guided evolutionary algorithm to optimize neural networks architectures for downstream task while minimizing size. Mutation is accomplished via few-shot prompting.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

- Evolutionary algorithm

## Benchmarks

Tasks evaluated.

- Cifar10
- Mnist
- GNN CLRS

## Metric Results

Surprisingly not much discussion of quality or diversity.

## Paper Tags

- EVO

## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

It is important to *warm-start* the method with existing good architectures. Otherwise not much improvement will be found.
Only seems to non-trivially outperform few-shot sampling in one specific benchmark.