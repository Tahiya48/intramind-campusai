from src.ingestion.document_schema import Document
from src.processing.embeddings import create_embeddings
from src.processing.vector_store import (
    add_chunks,
    search_chunks,
    collection,
)

# --------------------------------------------------
# CLEAR PREVIOUS TEST DATA
# --------------------------------------------------

existing_data = collection.get()

if existing_data["ids"]:

    collection.delete(
        ids=existing_data["ids"]
    )

# --------------------------------------------------
# CREATE TEST DOCUMENT CHUNKS
# --------------------------------------------------

chunks = [
    Document(
        text="Students must complete module registration before the academic deadline.",
        source="registration.md",
        document_type="markdown",
        chunk_index=0,
    ),
    Document(
        text="The university academic calendar contains important dates and deadlines.",
        source="deadlines.md",
        document_type="markdown",
        chunk_index=0,
    ),
    Document(
        text="Students should follow the university academic policies and regulations.",
        source="policies.md",
        document_type="markdown",
        chunk_index=0,
    ),
]


# --------------------------------------------------
# CREATE EMBEDDINGS
# --------------------------------------------------

texts = [chunk.text for chunk in chunks]

embeddings = create_embeddings(texts)


# --------------------------------------------------
# STORE CHUNKS
# --------------------------------------------------

add_chunks(chunks, embeddings)

print("\nChunks successfully stored in ChromaDB.")


# --------------------------------------------------
# SEARCH FOR RELEVANT CHUNKS
# --------------------------------------------------

query = "When do I need to register for my modules?"

query_embedding = create_embeddings([query])[0]

results = search_chunks(
    query_embedding,
    n_results=3,
)


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

print("\nSEARCH RESULTS")
print("=" * 60)

for index, document in enumerate(results["documents"][0]):

    print(f"\nResult {index + 1}")

    print(f"Text: {document}")

    print(
        f"Source: "
        f"{results['metadatas'][0][index]['source']}"
    )

    print(
        f"Distance: "
        f"{results['distances'][0][index]}"
    )

    print("-" * 60)