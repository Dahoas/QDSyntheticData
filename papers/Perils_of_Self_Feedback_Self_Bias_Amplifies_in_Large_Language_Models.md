# [Perils of Self-Feedback: Self-Bias Amplifies in Large Language Models](https://arxiv.org/abs/2402.11436)

ID: Number of paper in list of papers (ordered by date of accepted pr)

## Summary

Investigates how self-feedback affects LM, revealing that self-bias — models favouring their own outputs — is prevalent across various task (machine translation, text generation and maths reasoning).

This bias, which amplifies during iterative refinements, leads to overestimated performance improvements. 

Using larger models or integrating external feedback can mitigate some of this self-bias.

Self bias is defined as the average difference between the predicted quality and the expected quality score, where the expected quality is optimally measured by human preference but here they mainly use a proxy (BLEURT)

To mitigate uneven skewness they also use distance skewness estimation (one tail could be long and
thin, while the other is short and fat, yet they balance out overall):
    dSkew _(n)(X)=1-(sum_(i,j)||x_(i)-x_(j)||)/(sum_(i,j)||x_(i)+x_(j)-2gamma||),

where xi is a random variable drawn from θi − E(ˆθi) and xj is a random variable drawn from θi − E(ˆθi) − xi

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- Algorithm 1
- Algorithm 2
- Algorithm 3

## Benchmarks

Tasks evaluated.

- Flores-200
- CommonGen Hard
- MATH

## Metric Results

- How is quality measured?
    Bias and distance skewness: 
    1. Bias is calculated as the average difference between the LLM’s predicted quality scores and the expected quality (measured by human preference or predefined criteria).
    2. Distance skewness measures the asymmetry in the distribution of these differences
- How is diversity measured?
    UniEval (learned metric) for fluency and understandability.

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. Self-Feedback

## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

Anything else you found interesting/noteworthy.

## Questions

Questions you had about the paper
