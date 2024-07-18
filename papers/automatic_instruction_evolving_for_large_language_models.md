# [Automatic Instruction Evolving for Large Language Models](https://arxiv.org/abs/2406.00770)


## Summary

Proposes automatic pipeline for evolving instruction datasets. The evolution strategy is developed custom for the dataset. An LLM optimizer is used to evolve the evolution method as well. The optimization stage happens in two phases: (1) trajectory analysis for identifying failure modes and (2) optimization for improving the evolution method. They claim complexity and diversity correlate with benchmark performance.

The appendix details a couple key evolutionary failures:
1. Stagnant complexity
2. Insufficient qualification
3. Loss of key information

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- EvolInstruct

## Benchmarks

Tasks evaluated. For chat they start evolution from ShareGPT (note: possibly unfair comparisons since they use newer LLMs to generate the data) and base models for fine-tuning.

- MT-Bench
- AlpaceEval
- GSM8K: notably they do beat MetaMath
- HumanEval

## Metric Results

- Quality measured via downstream model performance + LLM as a judge feedback.
- Diuversity is measured via Instag automatic tagging method and calculating number of tags
- Complexity measured via GPT-4 llm as a judge

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. SYNTH
2. QUALITY
3. DIVERSITY
4. JUDGE
5. EVO

## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

Interesting that's there's no refinement component for fixing incorrect samples

## Questions

Questions you had about the paper
