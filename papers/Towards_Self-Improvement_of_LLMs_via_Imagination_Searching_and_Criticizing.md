# [Towards Self-Improvement of LLMs via Imagination, Searching, and Criticizing](https://arxiv.org/abs/2404.12253)

## Summary

Generates data to solve math problems via MCTS, and then collects the best traces and uses them to construct a finetuning dataset to improve the base policy - this is then applied iteratively. Called "AlphaLLM" and is trying to apply AlphaZero approach for LLMs.

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms

- MCTS 
- PRMs
- ORMs

## Benchmarks

Tasks evaluated.

- GSM8k 
- MATH 

## Metric Results

- How is quality measured?
  - Train a value function, PRM and ORM to evaluate intermediate completions as well as total completions, to guide MCTS.
    - Start with GSM8k training dataset, and for each problem do multiple rollouts, and then label the final answer and intermediate steps with values.
  - They use an importance factor 
     I(s_t) = \max_{o_t} |v^\pi([s_t, o_t]) - v^\pi(s_t)|
    which is the difference between a sequence [s_t, o_t] compared to the base prefix s_t. This is used to determine how many children to expand a node, i.e. importance-weighted expansion.
- How is diversity measured?
  - When expanding leaf nodes, they use similarity to other candidates via some distance to determine if a proposed candidate completion is too similar to the existing set. They say either a LLM-based distance or a traditional edit distance can be used, though they don't say what they use. They call this method state merging.
- Fine-tuning results?
  - Accuracy improves over two iterations of generating and finetuning on generated results when greedily choosing the paths.
  - Synthetic data is filtered using threshold on ORMs evaluation for each trace.

## Other comments

The action space for MCTS is not at the sentence-level or token-level but rather something in-between they call options.
A smaller LLM is used for the rollout phase, but they don't rollout to estimate the value at every node, and instead only rollout at greater depths.

## Questions

What distance function do they use for state merging?
How do they terminate generation for option-level completions?
The PRMs and ORMs are text based rewards, so how do they incorporate that into the actual value function computation?

