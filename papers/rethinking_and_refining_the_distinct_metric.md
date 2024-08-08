# [Rethinking and Refining the Distinct Metric](https://arxiv.org/abs/2202.13587)

ID: #327

## Summary

The aim of the paper is to improve the so called "Distict" metric proposed few years ago in another paper. The Distinct
metric is also what is called token type ratio, which is the ratio of unique tokens over all the tokens present in the text. The paper presents the limitations of the distinct metric like the sensitivity to length, that is shorter texts can have higher distinct scores while longer can have lower ones due to the repetition of tokens. The new proposed refined metric called expectation-adjusted distinct (EAD) is the number of distinct tokens divided by the expectation of distinct/unique tokens.
Empirical evaluations show that this metric correlates more with human judgements. 

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

NA

## Benchmarks

- OpenSubtitles
- DailyDialog

## Metric Results

- How is quality measured? NA
- How is diversity measured? 
EAD score: N/(V[1-((V-1)/V)^C]), where N = #unique tokens, C = #all tokens, V = #tokens in the whole vocabulary
- Fine-tuning results? NA

## Paper Tags

1. SAMPLING


## Relevant related work

Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, and Bill Dolan. 2016. A diversity-promoting objec- tive function for neural conversation models. 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL HLT 2016 - Proceedings of the Conference, pages 110–119. https://aclanthology.org/N16-1014.pdf


