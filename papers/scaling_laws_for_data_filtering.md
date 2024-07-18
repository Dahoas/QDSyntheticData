# [Scaling Laws for Data Filtering— Data Curation cannot be Compute Agnostic](https://arxiv.org/abs/2404.07177)

ID: #280

## Summary

This paper explores the intersection of data curation and computational constraints in the training of vision-language models (VLMs) like CLIP. The primary argument is that effective data filtering must consider the available computational resources to optimize model performance. 
It is also discussed and empirically analyzed how the utility of high-quality data decreases significantly when used repeatedly in training. After several epochs, even well-curated data can provide less benefit than new, lower-quality data that the model has not seen before. 
The authors propose new scaling laws that factor in the diminishing utility of repeated data points, providing a more nuanced approach to data curation.

## Relevance to survey topic (1-5)

Relevance: 3

## Benchmarks

- Datacomp
- LAION
- ImageNet
- CIFAR10

## Metric Results

- How is quality measured?
T-MARS score
CLIP score
- How is diversity measured?NA
- Fine-tuning results?NA

## Relevant related work

- Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. arXiv preprint arXiv:2203.15556, 2022
- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jef- frey Wu, and Dario Amodei. Scaling laws for neural language models, 2020
- Christoph Schuhmann, Richard Vencu, Romain Beaumont, Robert Kaczmarczyk, Clayton Mullis, Aarush Katta, Theo Coombes, Jenia Jitsev, and Aran Komatsuzaki. Laion-400m: Open dataset of clip-filtered 400 million image-text pairs. arXiv preprint arXiv:2111.02114, 2021
- Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, et al. Laion- 5b: An open large-scale dataset for training next generation image-text models. Advances in Neural Information Process- ing Systems, 35:25278–25294, 2022



## Questions

How can we transfer the scaling laws for data filtering to LLM models?



