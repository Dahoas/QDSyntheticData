# [StarCoder2-Instruct: Fully Transparent and Permissive Self-Alignment for Code Generation](https://arxiv.org/abs/2402.19173)

Language Models
## Summary

Uses self-refinement in the process of finetuning with instruct dataset to improve the correctness of the code through various heruristics like reasoning, execution feedback and generating test cases given an instruction. The seed functions are taken from the stackv1 python split.

## Relevance to survey topic (1-5)

Relevance: 3
The idea of generating seed prompts and the consequent generation of the completions are interesting to measure diversity and quality. Measuring the quality of the generated code ids also a good metric to evaluate through the process of the dataset generation via self-refinement. 

## Algorithms

List of algorithm categories the proposed method falls under. This will take some time to formalize. Example categories include i.i.d sampling, few-shot i.i.d sampling, MAP Elites, 

- self-refinement
- instruct-tuning

## Benchmarks

Tasks evaluated.

- HumanEval
- HumanEval-Plus
- MBPP
- MBPP-Plus

## Metric Results

- How is quality measured?
By pass@1 based on the test cases for each problem.
