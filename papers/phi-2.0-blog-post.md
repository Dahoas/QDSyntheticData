[Phi-2: The surprising power of small language models](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)

phi-2:
- 2.7B 
- 1.4T tokens
- 2k context
- 51200 vocab size
- 32 layers
- 32 heads

## Comments

The training for Phi-2 took 14 days on 96 A100 GPUs.

## Datasets

Did not expands on what has changed beyond the size to 1.4T

## Evaluations
- Big Bench Hard (BBH) (3 shot with CoT)

commonsense reasoning: 
- PIQA
- WinoGrande
- ARC easy 
- ARC challenge
- SIQA

language understanding:
- HellaSwag
- OpenBookQA
- MMLU (5-shot)
- SQuADv2 (2-shot)
- BoolQ

math:
- GSM8k (8 shot)

coding:
- HumanEval
- MBPP (3-shot)