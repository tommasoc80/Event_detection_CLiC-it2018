
Here the links to the pre-trained models for the EVENTI task. All of these models can be executed by running the scripts in the Test folder:

```
python3 RunModel_CoNLL_Format_eventit.py model.h5 inputfile-conll-format.txt

python3 RunModel.py model.h5 inputfile-raw-text-format.txt
```

| Model | F1 Extent (Strict) - Test | F1-Class (Strict) - Test |
|----------|:-----------:|:------------:|
|[Berardi_w2v](https://drive.google.com/file/d/1P_KhGQHigt2Da2DZyI1uxM4RfM4-O4ef/view?usp=sharing) | 0.868 | 0.705 |
|[Berardi_GloVe](https://drive.google.com/file/d/1Gt2dYJA3_8Xh1ik1RePicbZUzU6lb2b8/view?usp=sharing) | 0.860 | 0.697 | 
|[Fastext-It](https://drive.google.com/open?id=1vf_n_M38v5m4KOBxdi2KykZRPDxqFLb4) | 0.880 | 0.736 | 
|[ILC-ItWack](https://drive.google.com/open?id=1AmADSdKLrOlLFE1mju1MXDStwN6kRBdf) | 0.856 | 0.702 | 
|[DH-FBK_100](https://drive.google.com/file/d/1IY4xTLi_ijJBuP2vNQ3LsFaT95gr0ovC/view?usp=sharing) | 0.857 | 0.685 | 


Below a plotted chart of the performaces of each pre-trained models against an SVM system (HLT-FBK) that participated to the EVENTI exercise (see paper for more details).

<a href="https://drive.google.com/uc?export=view&id="folders/1VloOVa7loaljFVFtjhaNjhXNmFUyGXzw?ogsrc=32"><img src="https://drive.google.com/uc?export=view&id="folders/1VloOVa7loaljFVFtjhaNjhXNmFUyGXzw?ogsrc=32" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

