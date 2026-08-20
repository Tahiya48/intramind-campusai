from sentence_transformers import SentenceTransformer


# Load the embedding model once when this module is imported.
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str) -> list[float]:
    """
    Convert a piece of text into a semantic embedding vector.

    Args:
        text: Text to convert into an embedding.

    Returns:
        A list of floating-point values representing the text.
    """

    embedding = model.encode(text)

    return embedding.tolist()

def create_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Convert multiple pieces of text into embedding vectors.

    Args:
        texts: A list of text strings to convert.

    Returns:
        A list of embedding vectors.
    """

    embeddings = model.encode(texts)

    return embeddings.tolist()