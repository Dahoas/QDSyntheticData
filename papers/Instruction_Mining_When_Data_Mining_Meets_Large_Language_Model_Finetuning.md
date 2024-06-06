# [Instruction Mining: When Data Mining Meets Large Language Model Finetuning](https://arxiv.org/abs/2307.06290)

ID: 34

## Summary

This paper seeks to find an optimal subset to instruction-tune an LLM with. They do this by considering a bunch of quality and diversity metrics:
- Input length
- Output length
- Reward score from a 1.4B Pythia model trained on open assistant data
- Perplexity
- MTLD: Measure of Textual Lexical Diversity [1]
- KNN-i: Distance to i-th nearest neighbours in SentenceBERT embedding space
- Unieval-naturalness: Whether a response is like something a person would naturally say [2]
- Unieval-coherence: Whether a response is a valid continuation of the previous conversation [2]
- Unieval-understandability: Whether a response is understandable [2]
and then gather a dataset by training a bunch of Llama-2-7Bs on different data mixes, and recording the QD metrics and eval losses. With this they find a formula to predict eval loss from these metrics and use BlendSearch [3] to find optimal subsets.

Based on their analysis the only relevant metrics are the quality metrics reward score and the Unieval scores, so diversity as measured by MTLD or KNN-i doesn't play a role.

They find that the optimal size is rather small, around 2k samples. They call this double descent, but this has nothing to do with how that term is used normally in the literature.

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms

- BlendSearch [3]

## Benchmarks

- MT-bench loss
- OpenLLM benchmarks
- GPT-as-a-judge (not sure what dataset they used for this)

## Metric Results

There is a significant improvement over random subset selection at a relatively small cost. They show

## Other comments

They select the best regressors based on how well they fit the training data and their p-values, rather than eval R^2 and AIC/BIC.
They also don't consider multicollinearity so there's still room for improvement in their OLS analysis.

## Relevant related work

[1] "Mtld, vocd-d, and hd-d: A validation study of sophisticated approaches to lexical diversity assessment", Philip M McCarthy and Scott Jarvis. https://link.springer.com/article/10.3758/BRM.42.2.381

[2] "Towards a unified multi-dimensional evaluator for text generation", Ming Zhong et al. https://arxiv.org/abs/2210.07197

[3] "Economical hyperparameter optimization with blended search strategy", Chi Wang et al. https://openreview.net/forum?id=VbLH04pRA3