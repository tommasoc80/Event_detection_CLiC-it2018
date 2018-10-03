# Italian Event Detection and Classification @ CLiC-it 2018

This repository contains pre-trained models (and system outputs) for event detection and classification in Italian, following the [EVENTI](https://sites.google.com/site/eventievalita2014/) evaluation exercise presented at [EVALITA 2014](http://www.evalita.it/2014).

The pre-trained models have been obtained by using a state-of-the-art Bi-LSTM-CRF system [Reimers and Gurevych, 2017](http://aclweb.org/anthology/D17-1035). The original repository is available [here](), a forked version (updated at Oct. 3rd 2018) is available [here](https://github.com/tommasoc80/emnlp2017-bilstm-cnn-crf). To facilitate the reproducibility of the experiments and run the trained models on new data (either from raw sentences or from CoNLL format), you should use the forked version of the repository.

The repository is structured as follows:
- Train: it contains the adapted scripts to train the Bi-LSTM-CRF with the EVENTI datasets and different word embeddings for Italian;
- Test: it contains the adapted scripts to run the trained models either against CoNLL format datatset or against plain text documents (raw sentences);
- Models: it contains pointers to the trained models;
- Convert2CAT: it contains scripts to convert the Bi-LSTM-CRF output in the EVENTI CAT XML format for the evaluation and comparison with other systems.

# Citation
If you find any of these pre-trained models useful, please cite the following paper: [Italian Event Detection Goes Deep Learning]()

```
@InProceedings{Caselli-Clicit2018,
  author    = {Caselli Tommaso},
  title     = {{Italian Event Detection Goes Deep Learning}},
  booktitle = {Proceedings of the 5th Italian Conference on Computational Linguistics (CLiC-it 2018)},
  year      = {to appear},
  address   = {Turin, Italy},
}
``` 


