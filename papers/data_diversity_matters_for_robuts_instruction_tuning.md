# Data Diversity Matters for Robust Instruction Tuning



## Summary

Proposes the Quality-Diversity Instruction Tuning algorithms (**QDIT**) for sampling instruction datasets with targeted levels of quality and diversty from larger instruction datasets. They find quality/diversity are traded off and and data diversity significantly improves worst case instruction performance, suggesting improved generalization.

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms


- QDIT: Assigns initial QD score to each sample and greedily takes the best. QD traded off by $\alpha$ parameter. Diversity scores are recomputed after each insertion.


## Benchmarks

Tasks evaluated.

- Ultrachat 10K
- LMSYS 10K
- Alpaca 3K
- Mixed 10K
- Dolly 1K

## Metric Results

- Quality is measured with anthropic helpfulness RM.
- Diversity of a set $A$ is measured with respect to a set $V$ via $d(A) = \sum_{v \in V}\max_{a \in A}sim(a,v)$ where $sim(a,v)$ is computed using cosine similarity via sentence transformers. (Facility location function)
- Fine-tuned models are evaluated via LLM as a judge and HH RM score.

## Comments

We can use this to construct arfitificial QD datasets in our experiments. Also reminds me of the MRMR (maximum relevance minimum redundancy) algorithm for feature selection.

Emerging theme that diveristy helps robustness/OOD generalization.

## Questions

Any investigation into scaling laws?
