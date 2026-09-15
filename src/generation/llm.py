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
    # Include the source name so the LLM knows exactly where each
    # piece of information came from.

    context_parts = []

    for document, metadata in zip(
        documents,
        results["metadatas"][0],
    ):
        source = metadata.get("source", "Unknown source")

        context_parts.append(document)
        
    context = "\n\n".join(context_parts)

    prompt = f""""
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
12. When the user asks where information can be found, describe the relevant resource using only information explicitly supported by the 
    context. Do not include source filenames, URLs, Markdown links, or
    external websites in the answer. Source filenames are displayed separately by the application.
13. Do not turn general information into a specific resource.
    If the context explains a topic but does not specify where the
    information can be found, say that the available documents
    provide the information but do not specify a separate resource.
14. Do not state that documents can be accessed through a website,
    or that students should contact an office or service, unless
    the context explicitly states this for the topic being asked.

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