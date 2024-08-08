# [Data Selection for Language Models via Importance Resampling](https://arxiv.org/abs/2302.03169)

## Summary

This work proposes Data Selection with Importance Resampling, an efficient and scalable framework that selects data using importance resampling.

## Relevance to survey topic (1-5)

Relevance: 2

## Algorithms

This algorithm finds data similar to a target distribution (measured with a bag of hashed n-gram model).

## Benchmarks

Task evaluated.

- Classification (ACL-ARC, Sci-ERC, ChemProt, RCT, HyperPartisan, AGNews, Helpfulness, IMDB)
- RoBERTa Pretraining (GLUE) 

## Metric Results

- This is only a measure of "quality". Where "quality" represents whether a given data point follows a similar distribution to some target distribution.
- This does not measure diversity.

## Other comments

This method is quite efficient compared to other embedding-based representations.
The authors have implemented the method as a [python package](https://github.com/p-lambda/dsir), meaning it may be straightforward to use this method as a measure for quality.
