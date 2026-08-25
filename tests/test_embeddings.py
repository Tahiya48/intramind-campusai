from src.processing.embeddings import (
    create_embedding,
    create_embeddings,
)


# --------------------------------------------------
# TEST SINGLE EMBEDDING
# --------------------------------------------------

text = "Students must complete module registration before the deadline."

embedding = create_embedding(text)

print("\nSINGLE EMBEDDING TEST")
print("=" * 50)

print(f"Text: {text}")
print(f"Embedding dimensions: {len(embedding)}")

print("\nFirst 10 values:")
print(embedding[:10])


# --------------------------------------------------
# TEST MULTIPLE EMBEDDINGS
# --------------------------------------------------

texts = [
    "Students must complete module registration.",
    "The university has several academic policies.",
    "Important academic deadlines are available in the handbook.",
]

embeddings = create_embeddings(texts)

print("\nMULTIPLE EMBEDDINGS TEST")
print("=" * 50)

print(f"Number of texts: {len(texts)}")
print(f"Number of embeddings: {len(embeddings)}")

print("\nEmbedding dimensions:")

for index, embedding in enumerate(embeddings):
    print(f"Text {index}: {len(embedding)} dimensions")