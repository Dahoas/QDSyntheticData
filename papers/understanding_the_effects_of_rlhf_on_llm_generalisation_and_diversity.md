# [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://arxiv.org/abs/2310.06452)

## Summary

The paper analyzes how supervised fine-tuning, reward modelling, and RLHF affect OOD generalization and output diversity. RLHF improves in- and out-of-distribution performance (compared to SFT) but significantly reduces output diversity. Because of this, the paper asserts there is a tradeoff between generalization ability and diversity. 

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

- Supervised fine-tuning
- best-of-N sampling
- RLHF (SFT, reward modeling, PPO)

- Prompts GPT-4 as a human annotator simulation

## Benchmarks

Tasks evaluated:
- summarization
- instruction following tasks

Models evaluated:
- LLaMa-7b
- OPT models

## Metric Results

- How is quality measured?
  - GPT-4 is queried for whether it prefers the model output or the human annotated output - a "percentage win-rate of model against the reference"
  - ID test is the usual test set
  - OOD test is a separate dataset

- How is diversity measured? (chose one each of syntactic/semantic/logical diversity)
  - distinct N-grams (adjusted to remove bias toward short outputs)
  - Sentence-BERT cosine similarity
  - NLI diversity: Count number of entailments and contradictions between pairs of elements (higher if more contradiction)

NOTE: diversity is measured per-input (average diversity over inputs) and cross-input (diversity of all outputs)

- Results
  - RLHF > SFT performance-wise (both ID and OOD on all tasks)
  - Generalization gap
    - Summarization
      - BoN and SFT have similar generalization gaps, and they conclude BoN drop in performance is most explained by SFT drop in performance. 
      - RLHF has worse Generalization gap
    - Instruction-following
      - RLHF generalizes better on the further OOD

  - diversity (RLHF vs SFT) (both per-input and cross-input)
    - RLHF is less diverse semantically and syntactically
    - models comparable in logical diversity
  
## Paper Tags

1. DIVERSITY
2. JUDGE

## Other comments

The paper asserts that because RLHF improves generalization but decreases diversity, that there is a tradeoff between generalization and diversity. 

The paper mostly relies on instruction following performance results to assert RLHF is better at generalization, but then relise on the summarization diversity metrics to asser RLHF has lower semantic/syntactic diversity. One issue is in the summarisation task, actually RLHF was worse at generalization. I did not find the diversity metrics for the instruction-following task. 
