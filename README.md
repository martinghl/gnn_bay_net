# gnn_bay_net

## Overview

This project is designed to construct and analyze Bayesian networks using both continuous and discrete gene expression data. The goal is to model complex relationships between different genes and to understand the underlying structure of these relationships. The project is structured into several Python scripts, each handling specific tasks in the data processing and network analysis pipeline.

## Pipeline Summary

###     1.	Initial Node Setup
	•	Script: Bayesian_initial_nodes.py
	•	Input Files:
	•	i2g_df.csv
	•	ppionly_uc_newresults.csv
	•	edge_uc_3.txt
	•	Output: Annotated and visualized initial Bayesian network graph.
	•	Description: This script constructs an undirected structure by mapping nodes to genes. The network is visualized, displaying the relationships between nodes. This serves as the foundational setup for the network, preparing for future inference. 

###	2.	Continuous Data Cleaning and Overview (Insignificant)
	•	Script: bayesian_continous_data_overview.py
	•	Input Files:
	•	combined_hc_data.csv
	•	combined_uc_data.csv
	•	Output: Cleaned and batch-split continuous data.
	•	Description: This script combines, cleans, and splits continuous data into batches. The cleaned data is then prepared for clustering, dimensionality reduction, or further modeling. This step ensures that the continuous data is properly prepared for integration into the Bayesian network. (Can be ignored, the bayesian_discrete_data_overview file also contained the same processes. This file is reserved in case we want to directly ultilize continous data without Discretization.)
 
###	3.	Comparative Data Analysis
	•	Script: bayesian_comparative_data_overview.py
	•	Input Files:
	•	combined_hc_data.csv
	•	combined_uc_data.csv
	•	i2g_df_gene_ppion.csv
	•	edge_uc_3.txt
	•	Output: Filtered and merged data focusing on specific genes of interest.
	•	Description: Compare and analyze the expression data of HC and UC patients. Determine whether the gene expression shows significant difference. 
 
###	4.	Discrete Data Cleaning and Overview
	•	Script: bayesian_discrete_data_overview.py
	•	Input Files:
	•	data.csv
	•	TPM data files (e.g., GSE109142/*.txt)
	•	Output: Grouped and aggregated TPM data for discrete samples.
	•	Description: This script processes gene expression data, conducts batch effect removal and k-means clustering discretization. 

###	5.	Model Training
	•	Script: train_lbn_081.py
	•	Input Files:
	•	continous_hc.csv
	•	discretized_hc.csv
	•	discretized_uc.csv
	•	i2g_df_gene_ppion.csv
	•	Output: Trained Bayesian network model.
	•	Description: This script loads the cleaned and processed data, and uses the processed data to train a Bayesian network model. The initial structure ( undirected network) was divided into local structures using knn method, and conducts HillClimb searching algorism (BIC) on each local network. Afterwards, the many local neworks were assembled into a global network. The first step of structure learning is complete, needs more iterations (change k value when creating local undirected structures) untill the structure of the final, global network becomes stablized. Parameter learning is uncomplete. Code contains bugs that need to be fixed. 

## Dependencies

### 1. Bayesian_initial_nodes.py
	•	Input: i2g_df.csv, ppionly_uc_newresults.csv, edge_uc_3.txt
	•	Output: Annotated Bayesian network graph.
 
 	Dependencies:
	•	pandas
	•	networkx
	•	matplotlib
	•	biopython (for Bio.Entrez)
 
### 2. bayesian_continous_data_overview.py
	•	Input: combined_hc_data.csv, combined_uc_data.csv
	•	Output: Cleaned and batch-split continuous data.
 
	Dependencies:
	•	pandas
	•	numpy
	•	scikit-learn
	•	matplotlib
	•	seaborn
	•	scipy
 
### 3. bayesian_comparative_data_overview.py
	•	Input: combined_hc_data.csv, combined_uc_data.csv, i2g_df_gene_ppion.csv, edge_uc_3.txt
	•	Output: Filtered and merged data for specific gene analysis.
 
 	Dependencies:
	•	pandas
	•	numpy
	•	scikit-learn
	•	matplotlib
	•	seaborn
	•	scipy
### 4. bayesian_discrete_data_overview.py
	•	Input: data.csv, TPM data files
	•	Output: Grouped and aggregated TPM data for discrete samples.
 
 	Dependencies:
	•	pandas
	•	numpy
	•	glob
	•	os
	•	scikit-learn
	•	matplotlib
	•	seaborn
	•	scipy
### 5. train_lbn_081.py
	•	Input: continous_hc.csv, discretized_hc.csv, discretized_uc.csv, i2g_df_gene_ppion.csv
	•	Output: Trained Bayesian network model.
 
	Dependencies:
	•	pandas
	•	numpy
	•	torch
	•	pgmpy
	•	scikit-learn
	•	networkx
	•	matplotlib
