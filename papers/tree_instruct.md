# [Tree-Instruct: A Preliminary Study of the Intrinsic Relationship between Complexity and Alignment](https://arxiv.org/pdf/2308.05696)

ID: #305

## Summary

This paper proposes a method called Tree-Instruct to systematically enhance the complexity of instruction data. This method involves constructing semantic trees from natural language instructions by adding nodes, thereby deepening and widening the tree structure. This approach aims to improve the intricacy of sentence structures without deviating from the core thematic focus. 

## Relevance to survey topic (1-5)

Relevance: 4

## Benchmarks

Tasks evaluated.

- Alpaca-Eval
- MT-Bench

## Metric Results

- How is quality measured? NA
- How is diversity measured? NA
- Fine-tuning results? 
With increasing complexity of the instruction data, eval scores are increasing, the rise in complexity is due to increase in tokens, yet less more complex instructions outperform a bigger number of simpler instructions. In curriculum based instruction tuning easy to hard approach enhances model performance. 


## Relevant related work

- Can Xu, Qingfeng Sun, Kai Zheng, Xiubo Geng, Pu Zhao, Jiazhan Feng, Chongyang Tao, and Daxin Jiang. 2023. Wizardlm: Empowering large language models to follow complex instructions.  https://arxiv.org/abs/2304.12244
- Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. 2023. Wizardcoder: Empowering code large lan- guage models with evol-instruct. arXiv preprint https://arxiv.org/abs/2306.08568
- Subhabrata Mukherjee, Arindam Mitra, Ganesh Jawahar, Sahaj Agarwal, Hamid Palangi, and Ahmed Awadallah. 2023. Orca: Progressive learning from complex explanation traces of gpt- 4. arXiv preprint https://arxiv.org/abs/2306.02707. 



