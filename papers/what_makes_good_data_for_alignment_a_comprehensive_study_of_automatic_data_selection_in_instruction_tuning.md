# [WHAT MAKES GOOD DATA FOR ALIGNMENT? A COMPREHENSIVE STUDY OF AUTOMATIC DATA SELECTION IN INSTRUCTION TUNING](https://arxiv.org/abs/2312.15685)

## Summary

Examines data selection for alignment along three axes: quality, diversity, and complexity. They evolve synthetic data along quality and diversity axes (in a manner similar to evol instruct) and evaluate using GPT-4 LLM as judge (from which they distill reward models).

They construct data pools by sampling SOTA LLMs (actually just combine existing chat datasets). Always only select 6K samples. Proposes evol complexity: a complexity measure based on evolution: evolves a small seed dataset and puts evolution trajectories in prompt (after which chatGPT is prompted to assess sample complexity)
- important since otherwise model assigns similar complexities to most samples
Also proposes EvolQuality which is similar to evol complexity.
- they validate these measures by filtering 6K samples of both SOTA and "base" level data to demonstrate the downstream fine-tuned model is performing well (so the metrics correlate well with downstream performance)

Their final algorithm prioritizes picking samples based on quality and complexity, then on diversity.
- Given data pool X, sample score each sample to get quality-complexity score
- pick samples in order of decreasing score that have sufficient diversity

Also presents scaling behavior of their method:
- DEITA peaks at 6K samples / 300K
- TAGLM decreases and then sharply increases when all samples are included
- Random just monotonically increases with more data

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- EvolInstruct
- DEITA (their method)

## Benchmarks

Tasks evaluated.

- MT-Bench
- AlpacaEval

## Metric Results

- Quality measured via distill LLM as a judge.
- Diversity measusred via embedding distance. Filter to maximize distance between nearest neighbors
    - also considred insTag diversity
- Complexity measured via 
    - instruction length
    - perplexity
    - directly scoring with chat-gpt
    - convert instruction to semantic tree and measure node number
    - use chat gpt to tag topics and count tags
    - EvolComplexity
        - supposedly a better measure for what we want


## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. COMPLEXITY
2. QUALITY
3. DIVERISTY
