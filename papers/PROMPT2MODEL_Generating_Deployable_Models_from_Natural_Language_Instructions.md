# [PROMPT2MODEL: Generating Deployable Models from Natural Language Instructions](https://arxiv.org/abs/2308.12261)

## Summary

Given a natural language prompt with a few examples, the system constructs a finetune dataset by retrieving a relevant dataset and also generating a synthetic finetune dataset. The system also retrieve the most relevant model for the task to finetune.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

- few-shot sampling 
    - add examples of previous generated examples to increase diversity.
    - temperature annealing: adjusting the temperature from low to high proportionally to the number of examples generated.
    - use self-consistency to get better labels for a given generated data.

## Benchmarks

Tasks evaluated.

- Machine Reading Question Answering: SQuAD
- Japanese NL-to-Code: MCoNaLa
- Temporal Expression Normalization

## Metric Results

- How is quality measured?
    - No direct measurement of quality - considering the downstream task results.
- How is diversity measured?
    - Consider how many duplicates are in the generated data
    - Manual data inspection e.g. identifying a lot of similar examples in generated examples for the Japanese-to-Python task.
- Fine-tuning results?
    - Shows better result compare to gpt-3.5 with small finetune models except for the Japanese-to-Python task.
