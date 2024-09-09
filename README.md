
![rag](https://github.com/user-attachments/assets/530d822a-f48b-487c-b97a-9845462fcd08)
#
![app](https://github.com/user-attachments/assets/38ac1d64-2eaf-436a-8c9d-e7c3eec72fae)

## Project Overview
This project, Phenotype RAG, was developed as the final assignment for the LLM Zoomcamp. It implements a Retrieval-Augmented Generation (RAG) system that intelligently answers questions related to phenotypes by utilizing both a knowledge base and large language models (LLMs). The system is designed to assist with queries about phenotypes in fields such as genetics, evolutionary biology and medical diagnostics.

## Problem Description
Phenotyping plays a crucial role in various domains like genetics and medical diagnostics, helping researchers and clinicians understand the observable traits influenced by genetic and environmental factors. However, accessing and retrieving this knowledge can be challenging due to the vast amounts of data involved. This project aims to bridge this gap by building an intelligent assistant capable of answering complex phenotype-related queries using RAG techniques, combining the power of LLMs and a knowledge base.

## Technologies and Tools Used
### Key Technologies

- **Anaconda**: For environment management and package handling.
- **Docker**: Containerization of the entire application, ensuring consistency across different systems.
- **Grafana**: Used for monitoring with a customized dashboard displaying performance metrics.
- **Streamlit**: Provides a user-friendly UI for interacting with the Phenotype RAG system.
- **Prefect**: Orchestration and automation of data ingestion processes.

## LLMs Used

- **gemma2-9b-it**: Used for question reformulation.
- **mixtral-8x7b-32768**: Powers the retrieval-augmented generation (RAG) process, handling large text volumes to provide deeper contextual answers.
- **all-MiniLM-L6-v2**: Employed for embedding generation and semantic search.
- **Groq**: Integrated for vector search efficiency.
- **Pinecone**: Handles vector storage and fast retrieval, supporting the system's search capabilities.

### Other Tools Used for Development

- **Pytest**: For unit testing.
- **Git**: Version control.
- **Visual Studio Code**: Development environment.
- **Jupyter Notebook**: For data exploration and vector indexing.
- **PostgreSQL**: Database management for storing and retrieving structured data.

## Dataset
The dataset used for this project contains questions and answers about phenotypes, focusing on topics such as genetic research, evolutionary biology and medical diagnostics.

**Sample Questions:**

- "What is the definition of a phenotype?"
- "How do phenotypes relate to genetic research?"
- "What is the significance of phenotyping in evolutionary biology?"

## Project Execution Locally

### Pre-requisites
Ensure the following are installed on your machine:

- Anaconda (latest version)
- Python (version 3.10 or later)
- PostgreSQL (latest version)
- Grafana (latest version)

### Environment Setup

