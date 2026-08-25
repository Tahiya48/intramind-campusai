from src.ingestion.document_schema import Document
from src.processing.chunker import chunk_document


text = """
IntraMind CampusAI is an intelligent university assistant.

It uses a Retrieval-Augmented Generation system to answer
questions based on university documents.

Students can ask questions about module registration,
academic deadlines, university policies, and other information.

The system retrieves relevant document chunks before generating
an answer. This helps the AI provide answers based on the available
knowledge base instead of relying only on general knowledge.

Chunking is an important part of the RAG pipeline because large
documents are divided into smaller pieces. These pieces can later
be converted into embeddings and stored in a vector database.

When a user asks a question, the system can retrieve the most
relevant chunks and provide them to the language model as context.
"""


document = Document(
    text=text,
    source="test_document.md",
    document_type="markdown",
    title="IntraMind Test Document",
)


chunks = chunk_document(
    document,
    chunk_size=200,
    chunk_overlap=50,
)


print(f"\nTotal chunks created: {len(chunks)}\n")


for chunk in chunks:

    print("=" * 60)
    print(f"Chunk index: {chunk.chunk_index}")
    print(f"Source: {chunk.source}")
    print(f"Document type: {chunk.document_type}")
    print(f"Title: {chunk.title}")

    print("\nChunk text:")
    print(chunk.text)
    print()