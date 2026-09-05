import chromadb

from src.ingestion.document_schema import Document


# Create a local persistent ChromaDB client.
client = chromadb.PersistentClient(
    path="data/chroma"
)


# Get the collection, or create it if it does not exist.
collection = client.get_or_create_collection(
    name="campus_documents"
)


def add_chunks(
    chunks: list[Document],
    embeddings: list[list[float]],
) -> None:
    """
    Store document chunks, embeddings, and metadata in ChromaDB.

    Args:
        chunks: List of chunked Document objects.
        embeddings: Corresponding embedding vectors.
    """

    if len(chunks) != len(embeddings):
        raise ValueError(
            "The number of chunks must match the number of embeddings."
        )

    ids = []
    documents = []
    metadatas = []

    for index, chunk in enumerate(chunks):

        ids.append(
            f"{chunk.source}_{chunk.page}_{chunk.chunk_index}"
        )

        documents.append(
            chunk.text
        )

        metadata = {
            "source": chunk.source,
            "document_type": chunk.document_type,
            "chunk_index": chunk.chunk_index,
        }

        if chunk.title is not None:
            metadata["title"] = chunk.title

        if chunk.page is not None:
            metadata["page"] = chunk.page

        if chunk.domain is not None:
            metadata["domain"] = chunk.domain

        metadatas.append(metadata)

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search_chunks(
    query_embedding: list[float],
    n_results: int = 3,
) -> dict:
    """
    Search for the most semantically similar document chunks.

    Args:
        query_embedding: Embedding vector representing the user's query.
        n_results: Number of relevant chunks to retrieve.

    Returns:
        Search results from ChromaDB.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    return results