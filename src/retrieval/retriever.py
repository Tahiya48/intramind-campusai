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
        Search results containing documents, metadata, and distances.
    """

    query_embedding = create_embedding(query)

    results = search_chunks(
        query_embedding=query_embedding,
        n_results=n_results,
    )

    return results