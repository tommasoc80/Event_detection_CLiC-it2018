# Italian Event Detection and Classification @ CLiC-it 2018

This repository contains pre-trained models (and system outputs) for event detection and classification in Italian, following the [EVENTI](https://sites.google.com/site/eventievalita2014/) evaluation exercise presented at [EVALITA 2014](http://www.evalita.it/2014).

The pre-trained models have been obtained by using a state-of-the-art Bi-LSTM-CRF system [Reimers and Gurevych, 2017](http://aclweb.org/anthology/D17-1035). The original repository is available [here](), a forked version (updated at Oct. 3rd 2018) is available [here](https://github.com/tommasoc80/emnlp2017-bilstm-cnn-crf). To facilitate the reproducibility of the experiments and run the trained models on new data (either from raw sentences or from CoNLL format), you should use the forked version of the repository.

The repository is structured as follows:
- folder /Train: contains the adapted python scripts to run the Bi-LSTM-CRF with the EVENTI datasets and different word embeddings for Italian;

