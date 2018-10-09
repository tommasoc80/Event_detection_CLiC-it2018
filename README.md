# Italian Event Detection and Classification @ CLiC-it 2018

This repository contains pre-trained models (and system outputs) for event detection and classification in Italian, following the [EVENTI](https://sites.google.com/site/eventievalita2014/) evaluation exercise presented at [EVALITA 2014](http://www.evalita.it/2014). The system performs the task in a single step (detection + classification) rather than in the standard two-step approach achieving new state of the art results (F1 0.880 for event extent and F1-class 0.736 for event classification).

The pre-trained models have been obtained by using a state-of-the-art Bi-LSTM-CRF system [Reimers and Gurevych, 2017](http://aclweb.org/anthology/D17-1035). The original repository is available [here](https://github.com/UKPLab/emnlp2017-bilstm-cnn-crf), a forked version (updated at Oct. 3rd 2018) is available [here](https://github.com/tommasoc80/emnlp2017-bilstm-cnn-crf). To facilitate the reproducibility of the experiments and run the trained models on new data (either from raw sentences or from CoNLL format), you should use the forked version of the repository: first, you clone the forked (or the original) repository, then you clone this repository to run the trained models. 

The repository is structured as follows:
- Train: it contains the adapted scripts to train the Bi-LSTM-CRF with the EVENTI datasets and different word embeddings for Italian;
- Test: it contains the adapted scripts to run the trained models either against CoNLL format datatset or against plain text documents (raw sentences);
- Models: it contains pointers to the trained models;
- Convert2CAT: it contains scripts to convert the Bi-LSTM-CRF output in the EVENTI CAT XML format for the evaluation and comparison with other systems.

A final remark (not so small): by re-training the models from scratch, you may obtain different results.


# Citation
If you find any of these pre-trained models useful, please cite the following papers: 
- [Italian Event Detection Goes Deep Learning](https://arxiv.org/abs/1810.02229)
```
@InProceedings{Caselli-Clicit2018,
  author    = {Caselli, Tommaso},
  title     = {{Italian Event Detection Goes Deep Learning}},
  booktitle = {Proceedings of the 5th Italian Conference on Computational Linguistics (CLiC-it 2018)},
  year      = {to appear},
  address   = {Turin, Italy},
}
``` 
- [Reporting Score Distributions Makes a Difference: Performance Study of LSTM-networks for Sequence Tagging](https://arxiv.org/abs/1707.09861)

```
@InProceedings{Reimers:2017:EMNLP,
  author    = {Reimers, Nils, and Gurevych, Iryna},
  title     = {{Reporting Score Distributions Makes a Difference: Performance Study of LSTM-networks for Sequence Tagging}},
  booktitle = {Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  month     = {09},
  year      = {2017},
  address   = {Copenhagen, Denmark},
  pages     = {338--348},
  url       = {http://aclweb.org/anthology/D17-1035}
}
``` 

