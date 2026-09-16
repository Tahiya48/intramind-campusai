# IntraMind CampusAI

> An AI-powered institutional knowledge assistant for university communities.

## Overview

IntraMind CampusAI is an AI-powered institutional knowledge assistant that uses Retrieval-Augmented Generation (RAG) to answer questions related to the university based on a controlled knowledge base.

System takes Markdown, PDF and webpage content, converts documents to semantic embeddings, stores them in ChromaDB, retrieves relevant information and passes the retrieved context to a local Llama 3.2 3B model running through Ollama.

This architecture helps to ensure that the responses are grounded on the indexed knowledge base rather than relying only on the general knowledge of the LLM.

The project uses a synthetic university knowledge base for reproducible development, testing and demonstration.

---

## Key Features

- Natural-language university information assistant
- Retrieval-Augmented Generation (RAG)
- Semantic document retrieval
- Local LLM generation using Ollama
- ChromaDB vector database
- Sentence Transformer embeddings
- Markdown document ingestion
- PDF document ingestion
- Webpage ingestion
- Source attribution for generated answers
- Grounded responses based on retrieved information
- Fallback responses for unsupported questions
- Streamlit interactive interface
- Knowledge Base overview
- University document library
- Automated retrieval and generation evaluation

---

## How It Works

The IntraMind pipeline follows these main steps:

```text
University Documents
        ↓
Document Ingestion
        ↓
Text Extraction
        ↓
Document Chunking
        ↓
Embeddings
        ↓
ChromaDB Vector Database
        ↓
Semantic Retrieval
        ↓
Relevant Context
        ↓
Local LLM (Ollama)
        ↓
Grounded Answer + Sources

```
---

## Technology Stack

- **Python** — Core programming language
- **Streamlit** — Interactive web interface
- **Ollama** — Local LLM inference
- **Llama 3.2 3B** — Local language model
- **Sentence Transformers** — Text embeddings
- **ChromaDB** — Persistent vector database
- **PyMuPDF** — PDF text extraction
- **BeautifulSoup** — Webpage text extraction
- **Requests** — Web content retrieval

---

## Knowledge Base

The system currently uses a synthetic university knowledge base designed for reproducible development, testing and demonstration.

The knowledge base contains information covering areas such as:

- Academic support
- Attendance
- Campus services
- Deadlines
- Examinations
- Fees and finance
- Internships
- University policies
- Module registration
- Student information

The project also includes PDF and webpage sources to demonstrate multiple document ingestion methods.

---

## Evaluation

The RAG pipeline was evaluated using predefined questions covering both supported and unsupported queries.

### Retrieval Evaluation

- **13/14** questions retrieved the expected information
- **Retrieval accuracy: 92.86%**

The evaluation also includes unsupported questions to verify that the system does not retrieve irrelevant university information.

### Generation Evaluation

- **5/5** test cases produced the expected results
- **Generation accuracy: 100%**

The generation tests evaluate whether the LLM produces answers grounded in the retrieved knowledge base and correctly falls back when information is unavailable.
---

## How to Run

1. Clone the repository

```bash 
git clone <repository-url>
cd intramind-campusai

```
2. Create and activate the virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate

```

3. Install dependencies

```bash
pip install -r requirements.txt

```
4. Start Ollama

Make sure Ollama is installed and the required model is available:

```bash
ollama pull llama3.2:3b

```
5. Run the application

```bash
streamlit run app.py

```
---

## Project Structure

```text
intramind-campusai/
│
├── app.py
├── docs/
│   ├── pdf/
│   ├── testing/
│   ├── university/
│   └── web/
│
├── project_docs/
│
├── src/
│   ├── generation/
│   ├── ingestion/
│   ├── processing/
│   └── retrieval/
│
├── synthetic_site/
│
├── tests/
│
├── requirements.txt
└── README.md
```
---

## Limitations
- The current knowledge base uses synthetic university information.
- The local LLM is relatively small and may produce less detailed responses than larger language models.
- Answers are limited to information available in the indexed knowledge base.
- The system is intended as a demonstration and prototype rather than a production university information system.

---

## Future Improvements

Potential future improvements include:

- Expanding the university knowledge base
- Improving retrieval and ranking
- Supporting additional document formats
- Adding conversation memory
- Improving evaluation coverage
- Deploying the system for real-world institutional use

---

## Project Purpose

IntraMind CampusAI demonstrates how Retrieval-Augmented Generation can be used to build a grounded institutional knowledge assistant that combines document retrieval, vector search and local LLM generation.



