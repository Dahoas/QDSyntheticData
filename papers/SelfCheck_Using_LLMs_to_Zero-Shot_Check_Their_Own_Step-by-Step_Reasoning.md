# [SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning](https://arxiv.org/abs/2308.00436)

ID: 66

## Summary

Explores if LLMs are able to recognize errors in their own step-by-step reasoning, without resorting to external resources.
They propose SelfCheck, a zero-shot schema for self-identifying errors in LLM CoT reasoning. 
Specifically, using separate calls to the LLM they first extract the target and relevant context for the step, then regenerate an independent alternative step from these, and then compare the two. 
They use the results of these checks to improve question-answering performance by conducting weighted voting (given multiple solutions to a question, it uses confidence scores as weights to vote among the answer) on multiple solutions to the question.  

## Relevance to survey topic (1-5)

Relevance: 1 (reasoning paper)

## Algorithms

- Zero-shot checking

## Benchmarks

They find SeftCheckGPT recognises errors, and so improves accuracies on math-reasoning datasets:

GSM8K, MathQA, and MATH. 

## Metric Results

- How is quality measured?
- How is diversity measured?
- Fine-tuning results?
SelfCheck increases final answer accuracies with both GPT-3.5 and GPT-4 on all 3 benchmarks, except on GSM8K with GPT-4 and GPT-4 self checker (see table 1). 

## Paper Tags

1. REASONING

<!--
## Relevant related work

Add them to the spreadsheet. No need to link them in the report.

## Other comments

Anything else you found interesting/noteworthy.

## Questions

Questions you had about the paper
-->
