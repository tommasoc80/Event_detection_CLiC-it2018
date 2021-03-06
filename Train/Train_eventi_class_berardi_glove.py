# This script trains the BiLSTM-CNN-CRF architecture for event detection and classification in Italian
# using the EVENTI 2014 dataset (https://sites.google.com/site/eventievalita2014/).
# The code use the embeddings GloVe embeddings by Berardi et al 2015 (https://drive.google.com/open?id=1RY21bJP-lh9zvdWF5vBL4zeC8OCZ1sNg)
from __future__ import print_function
import os
import logging
import sys
from neuralnets.BiLSTM import BiLSTM
from util.preprocessing import perpareDataset, loadDatasetPickle

from keras import backend as K

# :: Change into the working dir of the script ::
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# :: Logging level ::
loggingLevel = logging.INFO
logger = logging.getLogger()
logger.setLevel(loggingLevel)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(loggingLevel)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


######################################################
#
# Data preprocessing
#
######################################################
datasets = {
#    'eventi_class_gold_berardi_glove':                                   #Name of the dataset
    'eventi_class_berardi_glove':                                   #Name of the dataset
        {'columns': {0:'tokens', 1:'POS', 2:'dependency', 3:'EVENT_CLASS'},    #CoNLL format for the input data. Column 1 contains tokens, column 2 contains NER information using BIO encoding
         'label': 'EVENT_CLASS',                      #Which column we like to predict
         'evaluate': True,                        #Should we evaluate on this task? Set true always for single task setups
         'commentSymbol': None}                   #Lines in the input data starting with this string will be skipped. Can be used to skip comments
}
# :: Path on your computer to the word embeddings. Embeddings by Reimers et al. will be downloaded automatically ::
embeddingsPath = 'glove_WIKI.txt'

# :: Prepares the dataset to be used with the LSTM-network. Creates and stores cPickle files in the pkl/ folder ::
pickleFile = perpareDataset(embeddingsPath, datasets)


######################################################
#
# The training of the network starts here
#
######################################################


#Load the embeddings and the dataset
embeddings, mappings, data = loadDatasetPickle(pickleFile)

# Some network hyperparameters
params = {'classifier': ['CRF'], 'LSTM-Size': [100, 100], 'dropout': (0.25, 0.25), 'charEmbeddings': 'CNN', 'maxCharLength': 50}


model = BiLSTM(params)
model.setMappings(mappings, embeddings)
model.setDataset(datasets, data)
model.modelSavePath = "models/[ModelName]_[DevScore]_[TestScore]_[Epoch].h5"
model.fit(epochs=25)



