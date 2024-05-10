# [Tree of Thoughts](https://arxiv.org/abs/2305.10601)

## Summary

Improves LLM output diversity by combing LLM with BFS search heuristic. Asks LLM to propose steps at each node and then asks LLM to evaluate most promising node based on rubric.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

- LLM as a Judge
- Search: BFS

## Benchmarks

Tasks evaluated.

- Game of 24
- Crosswords
- Poetry

## Metric Results

- Diversity is measured as number of states visited

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. DIVERSITY
2. SEARCH
