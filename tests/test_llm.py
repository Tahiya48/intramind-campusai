from src.generation.llm import generate_rag_answer


query = "When do I need to complete module registration?"

answer = generate_rag_answer(
    query=query,
)

print("\nRAG PIPELINE TEST")
print("=" * 60)

print(f"\nQuestion:\n{query}")

print("\nAnswer:")
print(answer)

print("\n" + "=" * 60)