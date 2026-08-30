from src.processing.embeddings import create_embedding
from src.processing.vector_store import search_chunks


def retrieve_relevant_chunks(
    query: str,
    n_results: int = 3,
) -> dict:
    """
    Retrieve the document chunks most relevant to a user's query.

    Args:
        query: The user's question or search query.
        n_results: Number of relevant chunks to retrieve.

    Returns:
        Search results containing relevant documents,
        metadata, and distances.
    """

    # Convert the user's query into an embedding.
    query_embedding = create_embedding(query)

    # Search the vector database.
    results = search_chunks(
        query_embedding=query_embedding,
        n_results=n_results,
    )

    # Reject chunks that are too dissimilar.
    threshold = 1.3

    filtered_documents = []
    filtered_metadatas = []
    filtered_distances = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        if distance <= threshold:
            filtered_documents.append(document)
            filtered_metadatas.append(metadata)
            filtered_distances.append(distance)

    return {
        "documents": [filtered_documents],
        "metadatas": [filtered_metadatas],
        "distances": [filtered_distances],
    }