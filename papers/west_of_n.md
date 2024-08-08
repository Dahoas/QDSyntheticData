# [West-of-N: Synthetic Preference Generation for Improved Reward Modeling](https://arxiv.org/abs/2401.12086)

## Summary

This paper generates synthetic data for use in reward model training via augmenting their training datasets. This is a self-training, semi-supervised learning, or data augmentation approach: first, a base RM is trained on a labeled preference dataset, then, given a set of prompts without labeled completions, policy model generations are compared and pseudolabeled by the RM, and this pseudolabeled dataset is added to the original to retrain a better RM. The key addition is the use of N policy outputs, and selecting the best-of-N and worst-of-N as a preference pair, which makes the pseudo-labeled dataset far higher-quality. This performs as well or better than collecting RLAIF preference labels or extra human labels for RM training.  

## Algorithms

- 

## Benchmarks

Tasks evaluated.

- Anthropic HH, Learning To Summarize - test set classification accuracy
- Pairwise winrates, measured by GPT-4, of Best-of-N using the RMs

## Metric Results

- Quality: Measured solely based on downstream utility or performance of resulting policy model using the RMs.
- Diversity: best and worst-of-N generations used as synthetic labeled data are filtered by loglikelihood (e.g. shouldn't be too high or low probability under the generator model)--this implicitly filters out samples which are too non-diverse, most likely
- Fine-tuning results: see Benchmarks above--RM accuracy and Best-of-N winrate are measured

Overall, quality and diversity are not explicitly defined here.

## Other comments

In general this seems like a useful one-size-fits all trick to apply to get more RM data, any time you have enough trust in your initial (human- or AI-) labeled preference dataset and resulting RM.

## Questions

West-of-N might have benefitted more from hyperparameter tuning than the RLAIF and RLCD baselines--they have a hyperparameter for thresholding response likelihoods, and for filtering by RM confidence?
