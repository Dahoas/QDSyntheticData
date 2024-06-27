# [Soft Self-Consistency Improves Language Model Agents](https://arxiv.org/abs/2402.13212)


ID: Number of paper in list of papers (ordered by date of accepted pr)

## Summary

Introduce a variation of self-consistency sampling where instead of generating _k_ times and taking the majority vote, they generate _k_ times and for each:
    score(y) = f {P(yi |y<i, x) ∀i ∈ [1, n]}
where f is in [max, min, product] (dataset dependent). They then choose the action y with the highest score.


## Relevance to survey topic (1-5)

Relevance: 1

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- Sampling

## Benchmarks

Tasks evaluated.

- Bash
- WebShop
- ALFWorld

## Metric Results

- How is quality measured?
    Code tasks. success rate
- How is diversity measured?
    - nan

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. SAMPLING


## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

Anything else you found interesting/noteworthy.

## Questions

Questions you had about the paper
