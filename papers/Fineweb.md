# [FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)

## Summary

FineWeb is a large-scale pretraining text dataset. They start out with a large unstructured web-scraped dataset from Common Crawl and seek to filter it down to improve its quality and diversity to make it more efficient to train on.

They follow a typical pipeline:
- Extract text from WARC files using trafilatura
- Filter for language using fastText
- Filter out bad urls
- Apply quality and repetition filters from MassiveText
- Minhash deduplication
- Apply C4 filters
- Custom filters
- Remove PII

They perform a number of experiments to show that
- WET data (raw text) is worse than WARC data (text extracted from html files)
- Global minhash deduplication is worse than deduplicating each dump individually. They hypothesise that the benefit of deduplication is the removal of very large document clusters that occur in every dump and that data that is not duplicated across dumps is generally of lower quality, i.e. quality and diversity aren't completely uncorrelated
- URL deduplication and line deduplication result in lower quality data
- C4 filters improve the quality and the ones with the most significant impact are fraction of lines ending in punctuation, fraction of characters in duplicated lines and fraction of lines shorter than 30 characters

They also find a subset that contains a lot of educational texts, which strongly outperforms the other datasets on the knowledge benchmarks ARC, MMLU and OpenbookQA.

## Relevance to survey topic (1-5)

Relevance: 3

## Algorithms

- Language classification
- Minhash

## Benchmarks

- CommonSense QA
- HellaSwag
- OpenBook QA
- PIQA
- SIQA
- WinoGrande
- ARC
- MMLU

## Metric Results

FineWeb is better than RefinedWeb, C4, Dolma, SlimPajama, RedPajama2 and The Pile on the above benchmarks

## Paper Tags

1. Pretraining
2. Deduplication

## Other comments

This blogpost is a helpful resource for anyone looking to create their own dataset and contains a lot of interesting information. Some of these ideas could also be applied to instruction tuning datasets. I think especially minhash could be a potential candidate to deduplicate large-scale finetuning datasets.

## other papers of interest

NA
