# [Generative AI for Synthetic Data Generation: Methods, Challenges, and the Future](https://arxiv.org/abs/2403.04190)

## Summary

This survey focuses on methods using LLMs to generate synthetic data without additional training. It discusses methods using prompt-engineering, methods of measuring data quality, techniques for using the data for training, and applications of synthetic data. 

The paper cites other papers that have a generation method and some downstream classifier task used for evaluation.

Main challenges identified include the correctness-diversity tradeoff, LLM hallucination, and data privacy problems. 

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms Mentioned

Prompt-engineering techniques
- MSP, AttrPrompt
- Verbalizer, MetaPrompt

Parameter-efficient task adaptation techniques
- ZeroGen, ZeroGen+, SuperGen, FewGen, ReGen, ProGen, AttrPrompt, MixPrompt

## Benchmarks Mentioned

Those used in the cited papers are in Table 1. 

## Metrics Mentioned

- most cited papers seem to evaluate quality based on increased performance of a classifier trained on the data
- ZeroGen is cited for identifying three attributes of synthetic data: diversity, correctness, naturalness
- ProGen proposes a "quality estimation module"

## Other comments

The paper also mentions that LLMs can introduce noise into the dataset, making regularization techniques necessary for stabilizing training on these datasets. ZeroGen+ and FewGen contain some such methods. 

## Questions


