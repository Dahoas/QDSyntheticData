# [Better Synthetic Data by Retrieving and Transforming Existing Datasets](https://arxiv.org/abs/2404.14361)

## Summary

Generates synthetic datasets for a target task by retrieving similar publicly available synthetic datasets and formulating a "transformation plan" based on the target and structure of public dataset. Improves perf. on big-bench tasks by average of 5% over baselines.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

Everything is more or less zero-shot (no domain specific human knowledge required).

## Benchmarks

6 big-bench tasks
- Time
- code
- math
- c&e
- russian
- impl

## Metric Results

DataTune supposedly improves both quality and diversity

- No measure of data-quality
- Diversity is measured with ROUGE thresholding (two sentences are the same given a high enough rouge score). Also measures bi-gram similarity 
    - also measures problem difficulty via asking chat-gpt to rate on a scale of 1-5


## Other comments

Clearly works best for domains which already have high-quality existing synthetic datasets available (e.g. math and code).

## Questions

Why no testing on MATH/GSM8K? Why only big-bench?
