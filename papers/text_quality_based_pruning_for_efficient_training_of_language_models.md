# [Text Quality-Based Pruning for Efficient Training of Language Models](https://arxiv.org/abs/2405.01582)

## Summary

Paper proposes model-agnostic numerical quality score for large unlabelled NLP datasets. This metric is used to remove low-quality text for “improved training efficiency.” It uses a weighted sum of 14 binary heuristics based on linguistic characteristic and reports comparable accuracy with less data, resulting in faster training. 

## Relevance to survey topic (1-5)

Relevance: 4

## Algorithms

Quality score calculation explained:
1. Apply each linguistic heuristic to the dataset and filter the best examples of the dataset to create a subset “validation dataset”
2. Calculate a weight for each heuristic: based on perplexity of the validation dataset. If applying this filter to a dataset causes lower perplexity in the subset, the weight is higher.
3. Each document line gets a line score, a weighted sum of indicator variables that a line passes a binary heuristic, weighted by previously calculated weights
4. Each document gets a document score, a weighted sum of line scores, weighted by line token length

Data pruning takes place by selecting a threshold. This work performs percentile-based pruning.

## Benchmarks

Models used include:
- GPT2
- GPT-Neo-125M
- Pythia-160M
- OPT-125M

Trains LM based on data subset against full dataset with English-only:
- Wikipedia
- OpenWebtext

Zeroshot accuracy on 14 downstream NLP tasks
- Arc Challenge
- ARC Easy
- HellaSwag
- OpenBookQA
- StoryCloze
- Winograd
- Winogrande
- SuperGLUE

## Metric Results

Qualitatively shows text mapping to various text quality scores.

Pruning 40% of OpenWebText sees an increase in performance for most models, and pruning 20% of Wikipedia sees comparable performance with less training time. They show graphs, but seems to me the model behavior varies. More significant changes in some downstream tasks' accuracy. 

When a small amount of data is removed, model perplexity only increases a little, which means likely meaningful data hasn’t been removed. When perplexity sharply increases, that is indicative of meaningful data being removed. 

## Paper Tags

QUALITY

## Other Comments

They use **lower perplexity as a sign of higher quality**, which is different from other papers that seem to just use model performance as a sign of quality.  
