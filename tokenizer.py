#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:12:22 2019

@author: jacksklar
"""


import pandas as pd 
import numpy as np
import re
import time


phenotype_df = pd.read_csv("./Clustering-autism-phenotypes-by-automated-text-analysis/dictionaries/HPO_synonym_map.txt", header = None, sep = "\t")
gene_df = pd.read_csv("./Clustering-autism-phenotypes-by-automated-text-analysis/dictionaries/gene_name_map.txt", header = None, sep = "\t")
pubmed_df = pd.read_csv("./Clustering-autism-phenotypes-by-automated-text-analysis/pubmed_bulk/total.csv", sep = "\t")
pubmed_df.dropna(subset=[ 'Abstracts'], inplace = True)

gene_list = gene_df[1]
phenotype_list = phenotype_df[0]

clust_features = phenotype_list
clust_dict = dict(zip(phenotype_df[0], phenotype_df.index))
synonym_dict = dict(zip(phenotype_list[0], phenotype_list[1]))


#%%



def replaceSynonym(line):
    line_no_special = re.sub(r"[^a-zA-Z0-9]+", ' ', line)
    for syn in synonym_dict:
        syn_no_special = re.sub(r"[^a-zA-Z0-9]+", ' ', syn)
        if re.match(syn_no_special, line_no_special):
            print syn
            new_line = re.sub(syn, synonym_dict[syn], line.rstrip())
            print(new_line)
    return new_line

def OneHot(text):
    gene_to_vec = np.zeros(len(clust_dict))
    text_no_special = re.sub(r"[^a-zA-Z0-9]+", ' ', text)
    for key in clust_dict:
            key_no_special = re.sub(r"[^a-zA-Z0-9]+", ' ', key)
            if re.match(key_no_special, text_no_special):
                print key
                gene_to_vec[clust_dict[key]] = 1.0
    return gene_to_vec
    
start = time.time()
pubmed_temp = pubmed_df.iloc[:1,:]
pubmed_temp.loc[0,"Abstracts"] = "Abnormality of body height"
pubmed_temp["present_genes"] = pubmed_temp["Abstracts"].apply(OneHot)
end = time.time()
print(end - start)

 

#%%














    
    