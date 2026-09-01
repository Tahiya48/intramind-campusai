import ollama
from src.retrieval.retriever import retrieve_relevant_chunks


FALLBACK_ANSWER = (
    "I could not find the answer in the available documents."
)


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


def generate_rag_answer(
    query: str,
    n_results: int = 10,
) -> dict:
    """
    Generate an answer using relevant document chunks as context.

    Args:
        query: The user's question.
        n_results: Number of relevant chunks to retrieve.

    Returns:
        A dictionary containing the generated answer
        and the sources that support the answer.
    """

    # Retrieve relevant document chunks.
    results = retrieve_relevant_chunks(
        query=query,
        n_results=n_results,
    )

    documents = results["documents"][0]

    # If retrieval found no relevant documents,
    # return the fallback answer without any sources.
    if not documents:
        return {
            "answer": FALLBACK_ANSWER,
            "sources": [],
        }

    # Combine retrieved chunks into the context given to the LLM.
    context = "\n\n".join(documents)

    prompt = f"""
You are IntraMind CampusAI, a university information assistant.

Answer the user's question using ONLY the information provided
in the context below.

Rules:
- Do not use outside knowledge.
- Do not make up information.
- Do not add information that is not supported by the context.
- If the context does not contain enough information to answer
  the question, respond exactly with:

"{FALLBACK_ANSWER}"

Context:
{context}

Question:
{query}

Answer:
"""

    answer = generate_answer(prompt).strip()

    # If the LLM determines that the answer is not available
    # in the retrieved context, do not display the retrieved
    # documents as sources.
    if answer == FALLBACK_ANSWER:
        return {
            "answer": FALLBACK_ANSWER,
            "sources": [],
        }

    # Collect unique sources only when an actual answer was generated.
    sources = []

    for metadata in results["metadatas"][0]:

        source = metadata.get("source")

        if source and source not in sources:
            sources.append(source)

    return {
        "answer": answer,
        "sources": sources,
    }