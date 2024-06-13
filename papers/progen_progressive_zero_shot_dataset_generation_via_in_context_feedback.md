# [ProGen: Progressive Zero-shot Dataset Generation via In-context Feedback](https://arxiv.org/abs/2210.12329)

## Summary

Proposes zero-shot data generation ProGen to leverage feedback from the task-specific model to guide data generation and improve quality issues (low informativeness and redundancy). Progen achieves comparable or better performance with 1% of the dataset size compared to baseline methods. 

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

ProGen:

1. Generate a dataset using a LM by prompting
2. Use dataset to train task model
3. Use noise-resistant "Influence Function" to choose most influential examples to update the prompt as in-context examples (few-shot)
4. Repeat

Influence function: change in model's Reverse Cross-Entropy loss on test data-point if up-weight loss of training data-point z

In practice, uses synthetic validation set, as no actual validation set is available. This is generated at the beginning with LM. 

## Benchmarks

- Text classification
  - IMDb
  - SST-2
  - Rotten Tomatoes
  - Elec
  - Yelp

## Metric Results

- Improves upon fine-tuning performance across the board
- Quality of dataset = performance of task model on test set
- Measures diversity with Self-BLEU
  - Progen degrades diversity relative to ZeroGen
- MAUVE (similarity between prediction distribution and ground-truth)
  - Progen creates higher score, indicating it well-shifts the generation distribution toward grount-truth distribution

## Paper Tags

1. SYNTH
2. QUALITY

## Other comments

- Attributes improved performance to improved dataset quality

