# IntraMind CampusAI

> An AI-powered institutional knowledge assistant for university communities.

## Overview

IntraMind CampusAI is an AI-driven university information assistant that lets students ask questions about university information using natural language.

The system pulls relevant information from the university knowledge base and gives it as context to a local Large Language Model (LLM) using Retrieval-Augmented Generation (RAG).

IntraMind does not just use the general knowledge of the model, it actually generates answers from the information within its knowledge base.

The project uses a synthetic university knowledge base generated for the purpose of reproducible development, testing and demonstration of the RAG pipeline.

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