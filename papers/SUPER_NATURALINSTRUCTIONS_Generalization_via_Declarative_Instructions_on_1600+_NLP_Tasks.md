# [SUPER-NATURALINSTRUCTIONS: Generalization via Declarative Instructions on 1600+ NLP Tasks](https://arxiv.org/abs/2204.07705)

## Summary

Collects a huge *meta-dataset* of 1600+ NLP tasks. Fine-tunes a T5 model on a subset and examines to generalization to unseen tasks. Examines three axes of scaling including number of instruction classes, number of instruction demonstrations, and model size. They find scaling both number of instruction classes and model size has a significant impact. Increasing number of intstruction demonstrations beyond 64 has no impact.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

No data is being generated.

## Benchmarks

1600+ tasks
- generation
- summarization
- qa
- translation
- etc...

## Metric Results

Not much emphasis on the impact of quality outside of carefully reviewing submitted tasks using crowd-workers.

They characterize diversity along three axes:
- instruction type
- language (english vs. non-english)
- domain (politics, medicine, etc...)

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. DIVERSITY

## Other comments

This paper is really focusing on evaluating the impact of diversity on OOD generalization (to some extent). They are not testing generalization in-distribution.