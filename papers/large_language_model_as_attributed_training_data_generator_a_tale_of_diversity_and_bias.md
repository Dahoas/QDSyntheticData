# [Large Language Model as Attributed Training Data Generator: A Tale of Diversity and Bias](https://arxiv.org/abs/2306.15895)

## Summary

This paper investigates synthetic datasets with *diversely attributed* prompts which specify additional attributes like length and style. They use a semi-automated form of attribute discovery and selection with ChatGPT. This method (AttrPrompt) improves downstream model performance, decreases bias, and increases efficiency by decreasing querying cost significantly as compared to the baseline (SimPrompt). 

## Relevance to survey topic (1-5)

Relevance: 5

## Algorithms

- Semi-supervised attribute discovery and generation with ChatGPT
- Attribute diversity ablation

## Benchmarks

Text classification for:
- NYT
- Amazon
- Reddit
- StackExchange

## Metric Results

- diversity (AttrPrompt mostly improves upon SimPrompt in diversity, but worse than Gold/real data)
  - lexical diversity: vocabulary size of generated dataset
  - cosine similarity of Sentence-BERT embedding of same-class text pairs
  - APS (average pairwise sample similarity)
      - AttrPrompt improves intra-class APS diversity compared to basic SimPrompt, worse than Gold standard
  - INGF (inter-sample N-gram Frequency)
- bias
  - attribute classifier to visualize
- performance
  - best performance downstream
  - improves performance most when combined with Gold data
- efficiency
  - AttrPrompt requires 5% of the query-cost of SimPrompt to achieve similar performance. 

## Other comments

Extensive details on prompts and generated attributes in Appendix

Appendix also mentions experiments and improved performance on significantly underrepresented classes because the AttrPrompt method creates samples for these classes. Makes sense, but I wonder if the improved diversity in AttrPrompt could improve performance on classes undetected (perhaps could measure by being more restrictive during attribute discovery/selection). The method evidently improves robustness, but what about adaptability?

## Questions

Perhaps worth nothing dataset bias in the context of quality-diversity, as it definitely affects downstream model performance. Would bias fit in as a subtopic of dataset quality? 
