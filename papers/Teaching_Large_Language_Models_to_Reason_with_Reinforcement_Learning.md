# [Teaching Large Language Models to Reason with Reinforcement Learning](https://arxiv.org/abs/2403.04642)

ID: Number of paper in list of papers (ordered by date of accepted pr)

## Summary

Fine-tunes mid-sized LLMs (LLama2-7B,13B) on reasoning tasks using RL offline/online and off-policy/on-policy algorithms. Finds performance is pretty comparable across all tasks both in terms of accuracy and sample complexity. This is conjectured to be due to a limitation in model exploration (as measured by pass@96 on the test set). Also identifies RL as improving pass@96 more/for longer than SFT due to diversity of synthetically generated training set.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- Return conditioned RL
- Expert Iteration
- PPO

## Benchmarks

Tasks evaluated.

- GSM8K
- SVAMP

## Metric Results

- How is quality measured: fine-tuning performance
- How is diversity measured: two solutions are identified as the same if they have the same sequence of arithmetic operations

## Paper Tags

Tag paper with relevant categories. See [here](https://github.com/Dahoas/QDSyntheticData/blob/main/papers/categories.json) for list of all category tags.

1. SYNTH
2. DIVERSITY
3. REASONING

## Other comments

The authors seem like pretty cool people.

