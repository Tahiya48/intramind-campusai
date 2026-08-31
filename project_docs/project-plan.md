# IntraMind CampusAI — Project Plan

## 1. Project Overview

IntraMind CampusAI is an AI based institutional knowledge and intelligence platform developed to assist university students and staff to retrieve information from institutional documents.

The platform is designed to be adaptable to different
universities, with the initial implementation demonstrated
using publicly available documentation from a selected
university.

The system will use Retrieval-Augmented Generation (RAG) to retrieve relevant information from institutional documents and generate grounded responses with references to the original sources.
---

## 2. Problem Statement

Universities contain an extensive amount of information in a variety of documents such as academic regulations, student handbooks, assessment policies, examination regulations, internship guidelines and other institutional procedures.

Locating the right information in these documents is time consuming. Users may also have difficulty in determining which document has the most relevant or up-to-date information.

IntraMind CampusAI is built to provide a single AI-powered interface where users can ask questions in natural language and receive answers that are grounded in institutional documentation.
---

## 3. Target Users

The target users are:
-Students
-Academic staffs
-Administrative staffs
---

## 4. Project Objectives

The main objectives are to:

1. Build a RAG-based system for institution-specific information retrieval.

2. Let users ask questions in natural language.

3. Extract relevant data from institutional documents.

4. Produce answers using the retrieved sources.

5. Get the original documents through citations.

6. Assess the quality of retrieval of documents and generated responses.

7. Discuss the use of machine learning and data analytics in improving the system.

8. Design the system so that its knowledge base can be adapted to different university environments.
---

## 5. Initial Features

The initial version is planned to include:

- Natural-language question answering
- Institutional document search
- Document retrieval
- Retrieval-Augmented Generation
- Source citations
- Document summarization
---

## 6. Planned Advanced Features

Potential advanced features include:

- Hybrid retrieval
- Reranking
- Question classification
- Policy conflict detection
- User feedback analysis
- Question clustering
- Knowledge analytics
- Retrieval evaluation
- Hallucination analysis
- Response quality monitoring
---

## 7. Planned Technology Stack

### Programming

- Python

### Data Processing

- Pandas
- NumPy
- PyMuPDF

### AI / NLP

- Large Language Model
- Embedding model
- RAG

### Vector Search

- Qdrant

### Machine Learning

- Scikit-learn

### Application

- Streamlit
- FastAPI

### Development

- Git
- GitHub
- Docker
---

## 8. Project Architecture

Initial conceptual architecture:

Documents
    ↓
Document Ingestion
    ↓
Document Processing
    ↓
Text Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
User Question
    ↓
Retrieval
    ↓
Relevant Context
    ↓
Large Language Model
    ↓
Grounded Answer + Sources

The architecture will be refined during development.
---

## 9. Evaluation Plan

The system will be evaluated by using a manually created question and answer dataset.

Evaluation metrics:

-Precision@K
-Recall@K
-Mean Reciprocal Rank (MRR)

Generation metrics:

-Relevance of answers
-Accuracy of citations
-Hallucination rate
-Faithfulness

System-level metrics:

-Response latency
-Retrieval efficiency 

## 10. Project Roadmap

- [x] Define initial project concept
- [x] Create project repository
- [x] Create documentation structure
- [ ] Select institutional scenario
- [ ] Collect initial document dataset
- [ ] Design document metadata
- [ ] Implement document processing
- [ ] Implement text chunking
- [ ] Generate embeddings
- [ ] Set up vector database
- [ ] Implement semantic retrieval
- [ ] Build baseline RAG pipeline
- [ ] Implement source citations
- [ ] Build user interface
- [ ] Create evaluation dataset
- [ ] Evaluate retrieval performance
- [ ] Improve retrieval
- [ ] Add machine learning component
- [ ] Add analytics
- [ ] Build API
- [ ] Containerise application
- [ ] Deploy application
