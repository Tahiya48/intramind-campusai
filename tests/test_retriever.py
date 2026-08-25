from src.retrieval.retriever import retrieve_relevant_chunks


query = "When do I need to register for my modules?"

results = retrieve_relevant_chunks(
    query=query,
    n_results=3,
)


print("\nRETRIEVAL RESULTS")
print("=" * 60)

documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]


if documents:

    for index, document in enumerate(documents):

        print(f"\nResult {index + 1}")

        print(f"Text: {document}")

        print(
            f"Source: "
            f"{metadatas[index]['source']}"
        )

        print(
            f"Distance: "
            f"{distances[index]}"
        )

        print("-" * 60)

else:

    print("No sufficiently relevant documents were found.")