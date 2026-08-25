from oauthlib.uri_validate import query
import ollama


def generate_answer(prompt: str) -> str:
    """
    Send a prompt to the local Ollama model and return its response.

    Args:
        prompt: The text prompt to send to the model.

    Returns:
        The generated response from the model.
    """

    response = ollama.generate(
        model="llama3.2:3b",
        prompt=prompt,
    )

    return response["response"]


from src.retrieval.retriever import retrieve_relevant_chunks


def generate_rag_answer(
    query: str,
    n_results: int = 3,
) -> str:
    """
    Generate an answer using relevant document chunks as context.

    Args:
        query: The user's question.
        n_results: Number of relevant chunks to retrieve.

    Returns:
        An answer generated from the retrieved context.
    """
    #handle empty retrieval results
    results = retrieve_relevant_chunks(
        query=query,
        n_results=n_results,
    )

    documents = results["documents"][0]

    if not documents:
        return "I could not find the answer in the available documents."

    context = "\n\n".join(documents)

    prompt = f"""
You are IntraMind CampusAI, a university information assistant.

Answer the user's question using ONLY the information provided
in the context below.

Do not use outside knowledge.
Do not make up information.
Do not add information that is not supported by the context.

If the answer cannot be found in the context, respond exactly with:

"I could not find the answer in the available documents."

Context:
{context}

Question:
{query}

Answer:
"""

    return generate_answer(prompt)