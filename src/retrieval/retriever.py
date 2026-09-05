from src.processing.embeddings import create_embedding
from src.processing.vector_store import search_chunks


THRESHOLD = 0.8


def _search_single_query(
    query: str,
    n_results: int,
) -> dict:
    """
    Retrieve relevant chunks for a single query.
    """

    query_embedding = create_embedding(query)

    results = search_chunks(
        query_embedding=query_embedding,
        n_results=n_results,
    )

    filtered_documents = []
    filtered_metadatas = []
    filtered_distances = []

    for document, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        if distance <= THRESHOLD:
            filtered_documents.append(document)
            filtered_metadatas.append(metadata)
            filtered_distances.append(distance)

    return {
        "documents": filtered_documents,
        "metadatas": filtered_metadatas,
        "distances": filtered_distances,
    }


def retrieve_relevant_chunks(
    query: str,
    n_results: int = 5,
) -> dict:
    """
    Retrieve the document chunks most relevant to a user's query.

    Multi-topic questions are split into separate searches so that
    each topic can retrieve its own relevant documents.
    """

    query_lower = query.lower()

    topic_queries = []

    # --------------------------------------------------
    # MODULE REGISTRATION
    # --------------------------------------------------

    if "module registration" in query_lower:

        topic_queries.append(
            "Where can students find information about module registration?"
        )

    # --------------------------------------------------
    # INTERNSHIPS
    # --------------------------------------------------

    if "internship" in query_lower or "internships" in query_lower:

        topic_queries.append(
            "Where can students find information about internships?"
        )

    # --------------------------------------------------
    # NORMAL SINGLE-TOPIC QUERY
    # --------------------------------------------------

    if len(topic_queries) <= 1:

        results = _search_single_query(
            query=query,
            n_results=n_results,
        )

        return {
            "documents": [results["documents"]],
            "metadatas": [results["metadatas"]],
            "distances": [results["distances"]],
        }

    # --------------------------------------------------
    # MULTI-TOPIC QUERY
    # --------------------------------------------------

    all_documents = []
    all_metadatas = []
    all_distances = []

    for topic_query in topic_queries:

        results = _search_single_query(
            query=topic_query,
            n_results=n_results,
        )

        all_documents.extend(
            results["documents"]
        )

        all_metadatas.extend(
            results["metadatas"]
        )

        all_distances.extend(
            results["distances"]
        )

    # --------------------------------------------------
    # REMOVE DUPLICATE CHUNKS
    # --------------------------------------------------

    unique_documents = []
    unique_metadatas = []
    unique_distances = []

    seen = set()

    for document, metadata, distance in zip(
        all_documents,
        all_metadatas,
        all_distances,
    ):

        chunk_id = (
            metadata.get("source"),
            metadata.get("chunk_index"),
        )

        if chunk_id not in seen:

            seen.add(chunk_id)

            unique_documents.append(
                document
            )

            unique_metadatas.append(
                metadata
            )

            unique_distances.append(
                distance
            )

    return {
        "documents": [unique_documents],
        "metadatas": [unique_metadatas],
        "distances": [unique_distances],
    }