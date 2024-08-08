# [Shepherd: A Critic for Language Model Generation](https://arxiv.org/abs/2308.04592)

ID: 68

## Summary

They introduce Shepherd, an LLM finetuned to provide criticism to model responses and suggest refinements. They create their own dataset from StackExchange and Reddit and finetune a Llama-7B model with this. This model outperforms ChatGPT, SelFee and Alpaca as judged by GPT4 and by humans.

## Relevance to survey topic (1-5)

Relevance: 2

## Benchmarks

Tasks evaluated:

- Winrates on AlpacaFarm, FairEval, CosmosQA, OBQA, PIQA, TruthfulQA and CritiqueEval

## Metric Results

It outperforms Alpaca, SelFee and ChatGPT


## Other comments

Most of the research value of this paper is in the construction of the dataset and the final model. It could be used as part of a pipeline to create synthetic data, but on it's own I don't think it's super relevant.

## Relevant related work

NA