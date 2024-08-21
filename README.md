# gnn_bay_net

## Overview

This project is designed to construct and analyze Bayesian networks using both continuous and discrete gene expression data. The goal is to model complex relationships between different genes and to understand the underlying structure of these relationships. The project is structured into several Python scripts, each handling specific tasks in the data processing and network analysis pipeline.

## Pipeline Summary

### 1.	Initial Node Setup
	•	Script: Bayesian_initial_nodes.py
	•	Input Files:
	•	i2g_df.csv
	•	ppionly_uc_newresults.csv
	•	edge_uc_3.txt
	•	Output: Annotated and visualized initial Bayesian network graph.
	•	Description: This script constructs a Bayesian network by mapping nodes to genes and annotating them with probability values. The network is visualized, displaying the relationships between nodes. This serves as the foundational setup for the network, establishing the initial nodes and their connections.
###	2.	Continuous Data Cleaning and Overview
	•	Script: bayesian_continous_data_overview.py
	•	Input Files:
	•	combined_hc_data.csv
	•	combined_uc_data.csv
	•	Output: Cleaned and batch-split continuous data.
	•	Description: This script combines, cleans, and splits continuous data into batches. The cleaned data is then prepared for clustering, dimensionality reduction, or further modeling. This step ensures that the continuous data is properly prepared for integration into the Bayesian network.
###	3.	Comparative Data Analysis
	•	Script: bayesian_comparative_data_overview.py
	•	Input Files:
	•	combined_hc_data.csv
	•	combined_uc_data.csv
	•	i2g_df_gene_ppion.csv
	•	edge_uc_3.txt
	•	Output: Filtered and merged data focusing on specific genes of interest.
	•	Description: This script filters the data based on specific gene criteria and merges the filtered data with additional datasets. The resulting data is used for further analysis and comparison, helping to refine the relationships in the Bayesian network.
###	4.	Discrete Data Cleaning and Overview
	•	Script: bayesian_discrete_data_overview.py
	•	Input Files:
	•	data.csv
	•	TPM data files (e.g., GSE109142/*.txt)
	•	Output: Grouped and aggregated TPM data for discrete samples.
	•	Description: This script processes discrete data by grouping samples based on diagnosis and sex, reading corresponding TPM files, and aggregating the data. The prepared data can then be used in discrete Bayesian network modeling.
###	5.	Model Training
	•	Script: train_lbn_081.py
	•	Input Files:
	•	continous_hc.csv
	•	discretized_hc.csv
	•	discretized_uc.csv
	•	i2g_df_gene_ppion.csv
	•	Output: Trained Bayesian network model.
	•	Description: This script loads the cleaned and processed data, standardizes the gene names, and uses the processed data to train a Bayesian network model. The model is then ready for inference or further analysis.

### 1. Bayesian_initial_nodes.py
	•	Input: i2g_df.csv, ppionly_uc_newresults.csv, edge_uc_3.txt
	•	Output: Annotated Bayesian network graph.
### 2. bayesian_continous_data_overview.py
	•	Input: combined_hc_data.csv, combined_uc_data.csv
	•	Output: Cleaned and batch-split continuous data.
### 3. bayesian_comparative_data_overview.py
	•	Input: combined_hc_data.csv, combined_uc_data.csv, i2g_df_gene_ppion.csv, edge_uc_3.txt
	•	Output: Filtered and merged data for specific gene analysis.
### 4. bayesian_discrete_data_overview.py
	•	Input: data.csv, TPM data files
	•	Output: Grouped and aggregated TPM data for discrete samples.
### 5. train_lbn_081.py
	•	Input: continous_hc.csv, discretized_hc.csv, discretized_uc.csv, i2g_df_gene_ppion.csv
	•	Output: Trained Bayesian network model.

## Methodology

### Data Loading and Preprocessing

Data is loaded from CSV files and processed to ensure consistency and accuracy. This includes standardizing gene names, filtering based on specific criteria, and handling missing data. The preprocessing steps ensure that the data is ready for further analysis and network construction.

### Network Construction and Analysis

Bayesian networks are constructed using processed data, with nodes representing variables (e.g., genes) and edges representing relationships between these variables. The networks are annotated with relevant data, such as probability values, to provide insight into the relationships being modeled.

### Visualization

The constructed networks are visualized to aid in understanding the structure and relationships within the data. Visualization tools such as networkx and matplotlib are used to create clear and informative network graphs.

