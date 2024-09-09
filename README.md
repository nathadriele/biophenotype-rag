
![rag](https://github.com/user-attachments/assets/530d822a-f48b-487c-b97a-9845462fcd08)
#
![app](https://github.com/user-attachments/assets/38ac1d64-2eaf-436a-8c9d-e7c3eec72fae)

## 🧬 Project Overview 
This project, Phenotype RAG, was developed as the final assignment for the LLM Zoomcamp. It implements a Retrieval-Augmented Generation (RAG) system that intelligently answers questions related to phenotypes by utilizing both a knowledge base and large language models (LLMs). The system is designed to assist with queries about phenotypes in fields such as genetics, evolutionary biology and medical diagnostics. 

## 🧬 Problem Description
Phenotyping plays a crucial role in various domains like genetics and medical diagnostics, helping researchers and clinicians understand the observable traits influenced by genetic and environmental factors. However, accessing and retrieving this knowledge can be challenging due to the vast amounts of data involved. This project aims to bridge this gap by building an intelligent assistant capable of answering complex phenotype-related queries using RAG techniques, combining the power of LLMs and a knowledge base.

## 🧬 Technologies and Tools Used
### ⚗️ Key Technologies

- **Anaconda**: Used for managing dependencies and environment configurations.
- **Docker**: Containerizes the application for easy deployment and consistent execution across different platforms.
- **Grafana**: Provides monitoring and visualization dashboards to track application performance and usage metrics.
- **Streamlit**: Offers a user-friendly interface for interacting with the Phenotype RAG system.
- **Prefect**: Orchestrates data ingestion workflows to ensure smooth and automated processes.

## 🧬 LLMs Used

- **gemma2-9b-it**: Utilized for question reformulation, optimizing queries for better understanding.
- **mixtral-8x7b-32768**: Powers the retrieval-augmented generation by processing large volumes of text and delivering more contextually accurate answers.
- **all-MiniLM-L6-v2**: Handles embedding generation and semantic search, allowing for precise query-to-answer matching.
- **Groq**: Integrates with the system for efficient vector processing during the search phase.
- **Pinecone**: Manages vector indexing and provides fast, scalable retrieval of information using semantic search.

### ⚗️ Other Tools Used for Development

- **Pytest**: For unit testing.
- **Git**: Version control.
- **Visual Studio Code**: Development environment.
- **Jupyter Notebook**: For data exploration and vector indexing.
- **PostgreSQL**: Database management for storing and retrieving structured data.

## 🧬 Dataset
The dataset used for this project contains questions and answers about phenotypes, focusing on topics such as genetic research, evolutionary biology and medical diagnostics.

**Sample Questions:**

- "What is the definition of a phenotype?"
- "How do phenotypes relate to genetic research?"
- "What is the significance of phenotyping in evolutionary biology?"

## 🧬 Project Execution Locally
### ⚗️ Pre-requisites
Ensure the following are installed on your machine:

- Anaconda (latest version)
- Python (version 3.10 or later)
- PostgreSQL (latest version)
- Grafana (latest version)

### ⚗️ Environment Setup
1. Clone the repository:
   
```py
git clone https://github.com/nathadriele/biophenotype-rag.git
cd bio-phenotype
```

2. Create and activate the virtual environment:
   
```py
conda create -n bio-phenotype python=3.10
conda activate bio-phenotype
```

3. Install dependencies:
   
```py
pip install -r requirements.txt
```

## 🧬 Data Exploration and Preprocessing
- Start the vector_Indexing_.ipynb notebook with Jupyter:
  
```py
jupyter notebook
```

## 🧬 Running the Application
To run the application, you'll need access keys for GroqCloud and Pinecone, as well as a Pinecone Index setup. Follow the instructions below:

1. Obtain API keys from GroqCloud and Pinecone.
2. Set up an index in Pinecone with the following configuration:

- Dimensions: 384
- Metric: Cosine
- Capacity Mode: Serverless
- Cloud Provider: AWS (Region: us-east-1)
3. Add your API keys to the .env files in the notebook and lang-bio-groq folders.
4. To launch the app locally:
  
```py
streamlit run main.py
```

## 🧬 Monitoring
Grafana is used to monitor the performance of the system. The grafana.png image shows the dashboard setup with at least five charts for key performance metrics.

## More Information
Final Consideration: This project was developed as the final assignment for the LLM Zoomcamp course.



