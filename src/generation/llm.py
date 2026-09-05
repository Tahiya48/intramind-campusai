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

Your task is to answer the user's question using ONLY the retrieved
context provided below.

STRICT RULES:

1. Use only information explicitly stated in the context.
2. Do not use your own knowledge.
3. Do not invent facts, document names, systems, policies, sections,
   websites, or resources.
4. Do not infer that something exists unless the context explicitly
   supports it.
5. Do not combine unrelated information from different documents.
6. If the question contains multiple topics, answer each topic
   separately using only the information available for that topic.
7. If information for one topic is missing, clearly say that the
   available documents do not provide enough information for that topic.
8. Never claim that a document contains information unless that
   information actually appears in the context.
9. Keep the answer concise and directly answer the user's question.
10. If none of the retrieved context answers the question, respond
    exactly with:

"{FALLBACK_ANSWER}"

11. Never refer to retrieved chunks as "sections of the context",
    "chunks", "documents 1, 2, 3", or similar internal retrieval details.
12. When the user asks where information can be found, name the
    relevant university resource or document only if that name is
    explicitly supported by the context.

Retrieved Context:
{context}

User Question:
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