# Hospital System Chatbot

A chatbot solution leveraging Neo4j, FastAPI, and Streamlit to provide natural language processing-based querying of hospital data.

## Prerequisites
- Python 3.8 or higher
- Docker Desktop
- OpenAI API Key
- Git

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/TahirRida/RAG-Chatbot
cd RAG-Chatbot
```

### Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows:
./venv/Scripts/activate
# On Unix or MacOS:
source venv/bin/activate
```

### Install Required Packages
```bash
pip install -r requirements.txt
```

### Create an Environment Configuration File
Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY="Your OpenAI API Key"

# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password

# Data Source Paths
HOSPITALS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/hospitals.csv
PAYERS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/payers.csv
PHYSICIANS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/physicians.csv
PATIENTS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/patients.csv
VISITS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/visits.csv
REVIEWS_CSV_PATH=https://raw.githubusercontent.com/hfhoffman1144/langchain_neo4j_rag_app/main/data/reviews.csv

# Model Configuration
HOSPITAL_AGENT_MODEL=gpt-3.5-turbo-1106
HOSPITAL_CYPHER_MODEL=gpt-3.5-turbo-1106
HOSPITAL_QA_MODEL=gpt-3.5-turbo-0125

# Service URLs
CHATBOT_URL=http://host.docker.internal:8000/hospital-rag-agent
```

Update this file with your OpenAI API Key and adjust the Neo4j credentials to match the configuration used in subsequent steps.

## Setting Up Neo4j

### Start Neo4j Container with APOC Plugin
```bash
docker run --name neo4j-apoc \
  -e NEO4J_AUTH=neo4j/password \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_apoc_export_file_enabled=true \
  -e NEO4J_apoc_import_file_enabled=true \
  -e NEO4J_apoc_import_file_use_neo4j_config=true \
  -e NEO4J_PLUGINS='["apoc"]' \
  -e NEO4J_dbms_security_procedures_unrestricted=apoc.* \
  -e NEO4J_dbms_security_procedures_allowlist=apoc.* \
  neo4j:latest
```

### Install APOC Core in the Neo4j Container
- Open Docker Desktop.
- Locate the `neo4j-apoc` container.
- Open the container's terminal (Exec) and run the following command:

```bash
cp /var/lib/neo4j/labs/apoc-5.26.0-core.jar /var/lib/neo4j/plugins/
```

## Loading Data
Navigate to the ETL directory and execute the data-loading script:

```bash
cd hospital_neo4j_etl/src
python hospital_bulk_csv_write.py
```

## Starting the Application

### Start the FastAPI Backend
```bash
cd chatbot_api/src
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Start the Streamlit Frontend
In a new terminal:
```bash
cd chatbot_frontend/src
streamlit run main.py
```

## Accessing the Application
- Neo4j Browser: [http://localhost:7474](http://localhost:7474)
- FastAPI Backend: [http://localhost:8000](http://localhost:8000)
- Streamlit Frontend: [http://localhost:8501](http://localhost:8501)

## Project Structure
```
RAG-Chatbot/
├── chatbot_api/          # FastAPI backend
├── chatbot_frontend/     # Streamlit frontend
├── chroma_data/         # Vector store data
├── data/                # Raw data files
├── hospital_neo4j_etl/  # ETL scripts
├── langchain_intro/     # LangChain setup
├── tests/              # Test files
└── requirements.txt    # Project dependencies
```

## Sample Questions
Test the chatbot with the following queries:
- "What hospitals are available in the system?"
- "What was the billing amount for patient 789's stay?"
