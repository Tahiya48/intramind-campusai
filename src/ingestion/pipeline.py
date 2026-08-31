from pathlib import Path

from src.ingestion.document_schema import Document
from src.processing.chunker import chunk_document
from src.processing.embeddings import create_embeddings
from src.processing.vector_store import add_chunks
from src.ingestion.pdf_loader import extract_text_from_pdf
from src.ingestion.web_loader import extract_text_from_webpage

def ingest_documents(
    docs_path: str = "docs",
) -> None:
    """
    Load documents from the docs folder, split them into chunks,
    create embeddings, and store them in ChromaDB.
    """

    folder = Path(docs_path)

    if not folder.exists():
        raise FileNotFoundError(
            f"Documents folder not found: {docs_path}"
        )

    # Clear the existing knowledge base before rebuilding it.
    from src.processing.vector_store import collection

    existing_data = collection.get()

    if existing_data["ids"]:
        collection.delete(
            ids=existing_data["ids"]
        )

    documents = []

    # Load Markdown documents
    for file_path in folder.glob("*.md"):

        text = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if text:

            documents.append(
                Document(
                    text=text,
                    source=file_path.name,
                    document_type="markdown",
                    title=file_path.stem,
                )
            )

    # Load PDF documents
    for file_path in folder.glob("*.pdf"):

        pdf_documents = extract_text_from_pdf(
            str(file_path)
        )

        documents.extend(pdf_documents)



    if not documents:
            print("No documents found to ingest.")
            return

    all_chunks = [] 

    for document in documents:

            chunks = chunk_document(document)

            all_chunks.extend(chunks)

    if not all_chunks:
            print("No chunks were created.")
            return

    chunk_texts = [
            chunk.text
            for chunk in all_chunks
    ]

    embeddings = create_embeddings(chunk_texts)    

    add_chunks(
            chunks=all_chunks,
            embeddings=embeddings,
    )

    print(
        f"Successfully ingested {len(documents)} documents "
        f"and {len(all_chunks)} chunks."
    ) 