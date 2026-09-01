# IntraMind CampusAI

> An institutional knowledge and intelligence platform for university communities driven by AI.

## Overview

IntraMind CampusAI is an AI-based university information assistant that allows students to ask questions in natural language and receive institutional information.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a university knowledge base for generation of an answer by a local Large Language Model (LLM).

Rather than answering based on the knowledge the model is trained with, IntraMind answers based on the documents in its knowledge base.

## Key Features

- University information assistant in natural language
- Retrieval-Enhanced Generation (REG)
- Semantic-based document retrieval
- Olama for local LLM generation
- ChromaDB vector database (chroma)
- Embeddings of Sentence transformer
- Markdown document processing
- PDF document ingestion
- Web page ingestion (synthetic)
- Attribution of sources for generated answers
- Protection from unsupported answers
- Streamlit interactive interface- Overview of Knowledge Base
- Document library with enhanced document contents
- Enhance knowledge base functionality

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