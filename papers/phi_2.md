# [Phi-2: The surprising power of small language models](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)

[HuggingFace](https://huggingface.co/microsoft/phi-2)

ID: 139

## Summary

It's a 2.7 billion-parameter LM trained on 1.4T tokens from multiple passes on a mixture of Synthetic and Web datasets for NLP and coding. 
It again demonstrates impressive reasoning and language understanding capabilities improving on phi-1.5.
Differences are it's a slightly bigger model, trained on more tokens and some new training techniques used for knowledge transfer... 

MSR say it showcases state-of-the-art performance among base language models with less than 13 billion parameters. 
On complex benchmarks Phi-2 matches or outperforms models up to 25x larger.

## Relevance to survey topic (1-5)

Relevance: 3 (not much new from Phi-1/1.5)

## Benchmarks

Many benchmarks in common sense reasoning, language understanding, mathematics and coding. 
Benchmarks span several categories, namely, Big Bench Hard (BBH) (3 shot with CoT), commonsense reasoning (PIQA, WinoGrande, ARC easy and challenge, SIQA), 
language understanding (HellaSwag, OpenBookQA, MMLU (5-shot), SQuADv2 (2-shot), BoolQ), math (GSM8k (8 shot)), and coding (HumanEval, MBPP (3-shot)).

Shows improvements across all compared to phi-1.5. 

With only 2.7 billion parameters, Phi-2 surpasses the performance of Mistral and Llama-2 models at 7B and 13B parameters on various aggregated benchmarks. 
It achieves better performance compared to 25x larger Llama-2-70B model on muti-step reasoning tasks, i.e., coding and math. 
Furthermore, Phi-2 matches or outperforms the recently-announced Google Gemini Nano 2, despite being smaller in size.

Due to benchmark contamination concerns they also evaluated Phi-2 using several Microsoft internal proprietary datasets and tasks, comparing it again to Mistral and Llama-2. We observed similar trends, i.e. on average, Phi-2 outperforms Mistral-7B, and the latter outperforms the Llama-2 models (7B, 13B, and 70B).

Toxicity results also improvement on phi-1.5 and llama2-7B. 


## Metric Results

- How is quality measured?
- How is diversity measured?
- Fine-tuning results?

## Paper Tags

1. SYNTH

## Relevant related work

Phi series, especially Phi-1.5. 

## Other comments

### Training details
The training for Phi-2 took 14 days on 96 A100 GPUs. 
Again no alignment or RLHF, but like Phi-1.5 it shows better behavior with respect to toxicity and bias compared to existing open-source models that went through alignment. 
They use innovative techniques to scale up, starting from the 1.3 billion parameter phi-1.5 model, and embed its knowledge within the 2.7 billion parameter Phi-2. 
This scaled knowledge transfer accelerates training convergence and shows a boost in Phi-2 benchmark scores.

### Training data details
The training data is the same as phi-1.5 but they further add "augmented with a new data source that consists of various NLP synthetic texts and filtered websites (for safety and educational value)."
This extra data was carefully selected web data that was filtered based on educational value and content quality. 


