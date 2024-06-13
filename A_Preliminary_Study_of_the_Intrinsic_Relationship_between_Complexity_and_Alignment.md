# [A Preliminary Study of the Intrinsic Relationship between Complexity and Alignment](https://arxiv.org/abs/2308.05696)

## Summary

This paper studies how the complexity of instructions affects performance, measured by the number of nodes in the instructions' semantic trees. They introduce a method called Tree-instruct to increase the instruction complexity, which is relatively straight-forward. First they parse an instruction into a semantic tree, then they expand the number of nodes, and finally they turn this tree back into natural language.

At least, that's what they claim. In reality what they do is they ask GPT-4 to do all of these steps at the same time. You can argue whether the internal representation of GPT4 actually uses such a tree structure or whether this is just a prompting technique. In any case, it is shown that the more complex the data, the better the performance, even when controlling for the number of tokens.

They also experiment with curriculum learning, i.e. increasing or decreasing the complexity throughout training, but this doesn't work better than just straight-up training on complex data.

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

- Tree-Instruct

## Benchmarks

- AlpacaEval vs text-davinci003
- MT-Bench vs text-davinci003

## Metric Results

- We add 3, 6, and 10 nodes to the semantic tree of each sample, resulting in performance gains of 13%, 20%, and 26%, respectively, across eight sub-skills such as commonsense, writing, and coding, showing consistent improvements.

## Relevant related work

[1] "WizardLM: Empowering Large Language Models to Follow Complex Instructions", Can Xu et al., https://arxiv.org/abs/2304.12244

## Other comments

NA
