# [Scaling Laws of Synthetic Images for Model Training ... for Now](https://arxiv.org/abs/2312.04567)

## Summary

Synthetic image data is generated using several different models (Stable Diffusion, Imagen, Muse) with several prompting T2I prompting techniques and CFG (classifier free guidence) levels. Supervised classifiers are then trained on up to 64 million samples and power law exponents are derived. Real images do best at in-distribution generalization but synthetic data scales better when tested out-of-distribution.

Scaling law exponents as a function of dataset size are computed for each 

## Algorithms

Most of the data generation algorithms depend on the T2I prompting technique used

- Classname: use only classname
- Classname + description
- Classname + hypernym
- Word2Sen: uses pretrained LM to generated varied sentences for each class
- CLIP template: generate sentences with the text template CLIP used for zero-shot classification

## Benchmarks

Tasks evaluated.

- Imagenet classification
- CLIP model training

## Metric Results

- Quality: is measured via a metric they call *recognizability*. Computed via classification accuracy of pre-trained ImageNet classifier. F1 is computed for each class and then averaged across all classes.
- Diversity: Standard deviation on embedded pre-trained feature space for each class averged across all classes. FID and LPIPS are also used

As expected, an inverse correlation is found.


## Other comments

- Using a more diverse prompt set results in more diverse images and as a by produt lowers recognizability
- For fixed prompts, higer CFG improves recognizability, leading to initially better but later declining performance.
- All models performed similarly
- Conducted analysis examining correlation between quality and diversity separately on scalability. Quality of a class (easiness of generating accurate representaions for the generator) is highly correlated with scalability (amenability to improvement with more synthetic data). Influence of diversity on scalability less pronounced.
- Scalability tightly correlated with overall performance

## Questions

- Maybe diversity matters more for OOD performance?