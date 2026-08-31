from pathlib import Path

from src.ingestion.document_schema import Document
from src.ingestion.pdf_loader import extract_text_from_pdf
from src.processing.chunker import chunk_document
from src.processing.embeddings import create_embeddings
from src.processing.vector_store import add_chunks


def ingest_documents(
    docs_path: str = "docs",
) -> None:
    """
    Load documents from the knowledge-base folders, split them into chunks,
    create embeddings, and store them in ChromaDB.
    """

    folder = Path(docs_path)

    if not folder.exists():
        raise FileNotFoundError(
            f"Documents folder not found: {docs_path}"
        )

    university_folder = folder / "university"
    web_folder = folder / "web"
    testing_folder = folder / "testing"

    # --------------------------------------------------
    # CLEAR EXISTING KNOWLEDGE BASE
    # --------------------------------------------------

    from src.processing.vector_store import collection

    existing_data = collection.get()

    if existing_data["ids"]:
        collection.delete(
            ids=existing_data["ids"]
        )

    documents = []

    # --------------------------------------------------
    # LOAD SYNTHETIC UNIVERSITY DOCUMENTS
    # --------------------------------------------------

    for file_path in university_folder.glob("*.md"):

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

    # --------------------------------------------------
    # LOAD SYNTHETIC WEBPAGE DOCUMENTS
    # --------------------------------------------------

    for file_path in web_folder.glob("*.md"):

        text = file_path.read_text(
            encoding="utf-8"
        ).strip()

        if text:

            documents.append(
                Document(
                    text=text,
                    source=file_path.name,
                    document_type="webpage",
                    title=file_path.stem,
                )
            )

    # --------------------------------------------------
    # LOAD TESTING PDF DOCUMENTS
    # --------------------------------------------------

    for file_path in testing_folder.glob("*.pdf"):

        pdf_documents = extract_text_from_pdf(
            str(file_path)
        )

        documents.extend(pdf_documents)

    # --------------------------------------------------
    # CHECK DOCUMENTS
    # --------------------------------------------------

    if not documents:

        print("No documents found to ingest.")

        return

    # --------------------------------------------------
    # CHUNK DOCUMENTS
    # --------------------------------------------------

    all_chunks = []

    for document in documents:

        chunks = chunk_document(
            document
        )

        all_chunks.extend(chunks)

    if not all_chunks:

        print("No chunks were created.")

        return

    # --------------------------------------------------
    # CREATE EMBEDDINGS
    # --------------------------------------------------

    chunk_texts = [
        chunk.text
        for chunk in all_chunks
    ]

    embeddings = create_embeddings(
        chunk_texts
    )

    # --------------------------------------------------
    # STORE CHUNKS
    # --------------------------------------------------

    add_chunks(
        chunks=all_chunks,
        embeddings=embeddings,
    )

    # --------------------------------------------------
    # REPORT RESULTS
    # --------------------------------------------------

    print(
        f"Successfully ingested {len(documents)} documents "
        f"and {len(all_chunks)} chunks."
    )