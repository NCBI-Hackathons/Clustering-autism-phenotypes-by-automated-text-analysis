# Classifying Diseases by Clustering Phenotypes using Automated Text Analysis

### A versatile tool to classify diseases using cluster analysis of published phenotypic data

## What does PubClass do?
PubClass is a pipeline that will take your PubMed query and output clusters of phenotypes and/or genes based on their co-occurrence in the published literature.


## Why should you use PubClass?
The ability to subclassify a disease can directly affect diagnosis and treatment options for a patient. PubClass allows you to determine if a disease of interest can be further classified based on phenotypic data from the entire corpus of published data.


## Background
Autism is a brain-based disorder that affects how information is processed. Its cause is not known. Genetic factors are thought to be responsible for 70-90% of cases. There are also related environmental factors.

Autism is a spectrum disorder, which means that patients with it can have a wide range of conditions.

Right now, there is a split in the field. There are some researchers who believe that there is a single common cause among all of the types of autism. Another camp hypothesizes that there could be many completely different types of problems that can result in a patient getting diagnosed with autism.


## Goal
Cluster analysis has been used by a number of researchers to try to determine if there are distinct subtypes of autism, or just one with varying conditions.

We are taking the approach of doing a literature-wise analysis by processing all abstracts from autism-related publications. We will try cluster analysis using diseases, genes, or topics mentioned in the abstracts. Scientific analysis of the resulting clusters from all related literature may help shed light on the etiology of autism.


## Workflow

![Workflow](assets/phenoclass_workflow.jpg "Phenoclass Workflow")

1.	INPUT: Collect user-supplied query e.g. "autism" and additional clustering parameters.

2a.	Extract abstracts and keywords from the result of NCBI's PubMed query.

2b.	Load dictionary to tokenize abstracts for clustering and cluster-metadata analysis.

3.	Perform text-processing (maybe just stemming and tokenization) to extract segments/tokens.

4.	OUTPUT: Output disease-specific clusters based on co-occurrence of topics/tokens/segments.

5.	Analysis of output clusters.

## Autism Clustering Results
![Cluster1](word_cloud/clu1.png "Phenoclass Cluster1")

![Cluster2](word_cloud/clu2.png "Phenoclass Cluster2")

![Cluster3](word_cloud/clu3.png "Phenoclass Cluster3")


## Papers that have used cluster analysis
[Kienle X, Freiberger V, Greulich H, Blank R. Autism Spectrum disorder and DSM-5: Spectrum or cluster? Prax Kinderpsychol Kinderpsychiatr. 2015;64(6):412–28.](https://www.ncbi.nlm.nih.gov/pubmed/26289149)

[Hrdlicka M, Dudova I, Beranova I, Lisy J, Belsan T, Neuwirth J, Komarek V, Faladova L, Havlovicova M, Sedlacek Z, et al. Subtypes of autism by cluster analysis based on structural MRI data. Eur Child Adolesc Psychiatry. 2005;14(3):138–44.](https://www.ncbi.nlm.nih.gov/pubmed/15959659)

[Bitsika V, Sharpley CF, Orapeleng S. An exploratory analysis of the use of cognitive, adaptive and behavioural indices for cluster analysis of ASD subgroups. J Intellect Disabil Res. 2008;52(11):973–85.](https://www.ncbi.nlm.nih.gov/pubmed/19017167)

[Ji NY, Capone GT, Kaufmann WE. Autism spectrum disorder in Down syndrome: cluster analysis of aberrant behaviour checklist data supports diagnosis. J Intellect Disabil Res. 2011;55(11):1064–77.](https://www.ncbi.nlm.nih.gov/pubmed/21883598)

[Cuccaro ML, Tuchman RF, Hamilton KL, Wright HH, Abramson RK, Haines JL, Gilbert JR, Pericak-Vance M. Exploring the relationship between autism spectrum disorder and epilepsy using latent class cluster analysis. J Autism Dev Disord. 2012;42(8):1630–41.](https://www.ncbi.nlm.nih.gov/pubmed/22105141)

[Palmer CJ, Paton B, Enticott PG, Hohwy J. ‘Subtypes’ in the presentation of autistic traits in the general adult population. J Autism Dev Disord. 2015;45(5):1291–301.](https://www.ncbi.nlm.nih.gov/pubmed/25337855)

[Kitazoe N, Fujita N, Izumoto Y, Terada SI, Hatakenaka Y. Whether the autism Spectrum quotient consists of two different subgroups? Cluster analysis of the autism Spectrum quotient in general population. Autism. 2017;21(3):323–32.](https://www.ncbi.nlm.nih.gov/pubmed/27132011)

[Tanaka S, Oi M, Fujino H, Kikuchi M, Yoshimura Y, Miura Y, Tsujii M, Ohoka H. Characteristics of communication among Japanese children with autism spectrum disorder: a cluster analysis using the Children's communication Checklist-2. Clin Linguist Phon. 2017;31(3):234–49.](https://www.ncbi.nlm.nih.gov/pubmed/27739870)


## People / Team
Wayne Sebastian Pereanu

Syed Hussain Ather

Jifan Gao

Kyle Lemoi

Jack Sklar

Olaitan I. Awe


## Presentation
[Overview](https://docs.google.com/presentation/d/1FBevl6DZ992tMjkpXs78eWMgZaK5nbDodG5yecXeyb4/)
