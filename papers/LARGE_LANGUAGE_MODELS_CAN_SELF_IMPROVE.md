# [Large Language Models Can Self-Improve](https://arxiv.org/abs/2210.11610)

## Summary

Using a large LLM (PALM) to label unlabeled data via self-consistency (SC) can be used to construct a synthetic fine-tuning dataset leading to improved performance. Also explores question generation and labeling using few-shot question prompting and SC labeling.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- self-consistency
- self-training

## Benchmarks

Tasks evaluated.

- Arithmetic (GSM8K, DROP)
- Commonsense (OpenBookQA, ARC)
- NLI (ANLI)

## Metric Results

- Answer quality is measured through the confidnce of the SC labels.
- Diversity is not explicilty measured. Multiple question formats are used to prevent overfitting.

Numbers on benchmarks go up generally, though not by a shocking amount. Improvement on OOD tasks is also demonstrated (AQUA, SVAMP, StrategyQA, RTE, MNLI-M/MM).

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. SYNTH

## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

Anything else you found interesting/noteworthy.

## Questions

Questions you had about the paper
