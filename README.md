
![rag](https://github.com/user-attachments/assets/530d822a-f48b-487c-b97a-9845462fcd08)
#
![app](https://github.com/user-attachments/assets/38ac1d64-2eaf-436a-8c9d-e7c3eec72fae)

## 🧬 Project Overview 
This project, Phenotype RAG, was developed as the final assignment for the LLM Zoomcamp. It implements a Retrieval-Augmented Generation (RAG) system that intelligently answers questions related to phenotypes by utilizing both a knowledge base and large language models (LLMs). The system is designed to assist with queries about phenotypes in fields such as genetics, evolutionary biology, and medical diagnostics. By integrating retrieval and generation capabilities, the project provides precise and contextually accurate information, making it a powerful tool for phenotype-related research and clinical applications.

## 🧬 Problem Description
Phenotyping plays a crucial role in various domains like genetics, evolutionary biology, and medical diagnostics, helping researchers and clinicians understand the observable traits influenced by genetic and environmental factors. However, the complexity and vastness of phenotype data make it challenging to access and retrieve relevant information efficiently. This project addresses the challenge by developing an intelligent assistant capable of answering complex phenotype-related queries. By leveraging RAG techniques, the system combines the reasoning ability of LLMs with the precision of a curated knowledge base, making the retrieval of phenotype information more accessible and accurate for researchers, healthcare professionals, and educators.

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
- **Pytest**: Ensures code reliability through unit and integration tests.
- **Git**: Version control for tracking changes and collaboration.
- **Visual Studio Code**: Integrated development environment (IDE) for writing and debugging code.
- **Jupyter Notebook**: Facilitates exploratory data analysis and preprocessing through interactive notebooks.
- **PostgreSQL**: Relational database used for storing and querying structured data.

## 🧬 Project Structure
The project is organized into the following directories and files:

```py
phenotype-rag/
├── bio-phenotype/                        # Root folder for the main application logic
│   ├── data/                             # Directory to hold project-specific datasets 
│   │   └── bio-phenotype.csv             # Main dataset: includes phenotype-related questions and answers
│   ├── sql/                              # Directory for database management and schema scripts
│   │   ├── .env                          # Environment file storing sensitive credentials database connection strings
│   │   └── create_table.py               # Python script to automate the creation of tables in PostgreSQL
│   ├── tests/                            # Directory for unit tests to ensure code quality and correctness
│   │   └── test.py                       # Python script containing test cases for core functionalities of the project
│   ├── __init__.py                       # Initializes the `bio-phenotype` package, making its modules importable across the project
│   ├── main.py                           # Streamlit application entry point; defines the UI and handles user interaction
│   ├── prefect_ingest.py                 # Prefect workflow script that automates data ingestion and processing tasks
│   ├── requirements.txt                  # Lists Python dependencies needed to run the project (for pip-based installations)
│   └── utils.py                          # Contains utility functions for data processing, I/O operations, and common tasks
├── data/                                 # Contains raw data files that can be accessed across different components
│   └── bio-phenotype.csv                 # Same dataset as in `bio-phenotype/data`, accessible for testing and backup
├── grafana/                              # Directory for Grafana monitoring setup
│   └── monitoring/
│       ├── docker-compose.yaml           # Docker Compose configuration for setting up Grafana
│       └── grafana_datasources.yaml      # Configuration file that defines the data sources Grafana will connect to PostgreSQL
├── images/                               # Directory for storing project-related images and screenshots
│   ├── app.png                           # Screenshot of the Streamlit app's interface
│   └── grafana.png                       # Screenshot of the Grafana monitoring dashboard, displaying key metrics
├── notebook/                             # Directory containing Jupyter notebooks for exploratory data analysis (EDA) and model experimentation
│   ├── .env                              # Environment file specifically for notebook-related configurations (API keys, credentials)
│   └── vector_Indexing_.ipynb            # Notebook for vectorizing data and indexing it into the semantic search system (Pinecone)
├── docker-compose.yaml                   # Primary Docker Compose file to orchestrate multi-container setups, including app, database, and Grafana
├── prefect_ingest.py                     # Duplicate of the workflow orchestration script (kept in the root for easier access during testing)
├── README.md                             # Project documentation with detailed instructions on usage, setup, and project purpose
├── requirements.txt                      # Python dependencies for the entire project (ensuring the environment is consistent across machines)
└── test.py                               # Standalone test script covering various components, including ingestion, database interactions, and the API
```

## 🧬 Dataset
The dataset used for this project contains questions and answers about phenotypes, with a focus on genetic research, evolutionary biology, and medical diagnostics. It explores how phenotypic traits relate to cognitive function, disease susceptibility, and treatment outcomes, highlighting the role of phenotyping in personalized medicine. The dataset also covers the impact of traits on aging, chronic diseases, and mental health disorders. Phenotypic trait analysis is crucial in understanding genetic predispositions, environmental adaptations, and evolutionary processes. This resource supports the development of diagnostic tools, therapeutic strategies, and health interventions by linking observable traits to genetic and environmental factors. Additionally, it is valuable for research in agricultural phenotypes, such as plant growth and disease resistance.

**Some Questions and Answers:**

![image](https://github.com/user-attachments/assets/9340d71a-9c3f-4013-9931-f8c904f0ed7a)

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
- Start the `vector_Indexing_.ipynb` notebook with **Jupyter**:
  
```py
jupyter notebook
```

## 🧬 Running the Application
To run the application, you will need access keys (API Key) for both **GroqCloud** and **Pinecone**. You will create and substitute them, as well as create an Index in **Pinecone**. You will need accounts on both platforms.

### Step 1: Create API Key on GroqCloud

![gloq](https://github.com/user-attachments/assets/474b3dbc-54d9-4965-ad54-6d505e77ddb2)

- Create or log into your GroqCloud account and navigate to **API Keys > Create API Key**.
- Copy and save the **Key** in a text editor for later use.

### Step 2: Create an Index on Pinecone

![pinecone](https://github.com/user-attachments/assets/68ccc4a9-0e0e-4209-a96e-f76448cc98ba)

- On the **Pinecone** website, go to **Indexes > Create Index**.
- Configure the index as follows:
   - Default / bio
   - **Dimensions**: 384
   - **Metric**: Cosine
   - **Capacity mode**: Serverless
   - **Cloud provider**: AWS
   - **Region**: Virginia | us-east-1
- Complete the setup by clicking on **Create Index**.

**Note**: The region can be changed without significantly affecting the code. However, altering other configurations would require significant code adjustments.

### Step 3: Add the API Keys to Environment Files
After completing the previous steps, add your API keys to the `.env` files in the `notebook` and `lang-bio-groq` folders, as shown below:

![image](https://github.com/user-attachments/assets/0acae8c7-6f60-4c20-bc5e-b987074e9d85)

Make sure to replace `your-pinecone-api-key` and `your-groqcloud-api-key` with the actual keys you generated earlier.

### Step 4: Running the Application Locally
To run the application locally, you may need to adjust the configurations in the .env file to match your environment. This also applies to the Grafana setup parameters shown below.

- In the **Anaconda Prompt**, ensure you are in the `lang-bio-groq` folder and run the following command:

```py
streamlit run main.py
```

## 🧬 Monitoring
![grafana](https://github.com/user-attachments/assets/8027f204-6112-4cb5-99f0-f2cf07a039a1)

**Grafana** is used to monitor performance. The image shows the dashboard configuration with the integrated charts for key performance metrics.

## More Information
This project was developed as the final assignment for the **LLM Zoomcamp** course.



