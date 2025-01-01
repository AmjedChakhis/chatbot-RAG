# Hospital System Chatbot

A chatbot solution leveraging Neo4j, FastAPI, and Streamlit to provide natural language processing-based querying of hospital data.

## Chatbot Interface

### Prerequisites
- Python 3.8 or higher
- Docker
- OpenAI API Key

### Setup Instructions

#### 1. Initial Configuration
Begin by cloning the repository and navigating to its root directory. Create a `.env` file with the following details:

```env
OPENAI_API_KEY="Your OpenAI API Key"

# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password

# Data Source URLs
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

Update this file with your OpenAI API Key and adjust the Neo4j credentials to align with the docker command used in the next steps.

#### 2. Setting Up the Python Environment
Create and activate a virtual environment:

```bash
python -m venv venv
# For Windows:
./venv/Scripts/activate
# For Linux/Mac:
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

#### 3. Configuring Neo4j
Launch the Neo4j container with the APOC plugin:

```bash
docker run --name neo4j-apoc \
    -e NEO4J_AUTH=neo4j/password \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS='["apoc"]' \
    -e NEO4J_dbms_security_procedures_unrestricted=apoc.* \
    -e NEO4J_dbms_security_procedures_allowlist=apoc.* \
    neo4j:latest
```

Install the APOC plugin manually:

```bash
docker exec neo4j-apoc cp /var/lib/neo4j/labs/apoc-5.26.0-core.jar /var/lib/neo4j/plugins/
```

#### 4. Loading Data
Move to the ETL directory and execute the data-loading script:

```bash
cd hospital_neo4j_etl/src
python hospital_bulk_csv_write.py
```

#### 5. Starting the Services
Launch the backend API:

```bash
cd chatbot_api/src
uvicorn main:app --host 0.0.0.0 --port 8000
```

Start the frontend application:

```bash
cd chatbot_frontend/src
streamlit run main.py
```

#### 6. Accessing the Application
- Backend API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- Frontend chatbot interface: [http://localhost:8501/](http://localhost:8501/)

### Sample Questions
Test the chatbot with these queries:
- "What hospitals are available in the system?"
- "What was the billing amount for patient 789's stay?"
