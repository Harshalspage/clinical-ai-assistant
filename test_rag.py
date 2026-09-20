from rag.document_loader import load_knowledge_base
from rag.embeddings import load_embedding_model, create_embeddings
from rag.retriever import create_vector_index, search_index




knowledge_base = load_knowledge_base(
    "knowledge_base/medical_knowledge.txt"
)

print("Knowledge base loaded successfully.")



documents = [
    section.strip()
    for section in knowledge_base.split("==================================================")
    if section.strip()
]

print(f"Number of knowledge sections: {len(documents)}")



model = load_embedding_model()

print("Embedding model loaded successfully.")




embeddings = create_embeddings(
    model,
    documents
)

print("Embeddings created successfully.")


# ---------------------------------
# 5. Create FAISS index
# ---------------------------------

index = create_vector_index(embeddings)

print("FAISS index created successfully.")


# ---------------------------------
# 6. Test clinical query
# ---------------------------------

query = "Patient has fever, chest pain and difficulty breathing."

query_embedding = create_embeddings(
    model,
    [query]
)


# ---------------------------------
# 7. Retrieve relevant knowledge
# ---------------------------------

results = search_index(
    index,
    query_embedding,
    documents,
    top_k=3
)


# ---------------------------------
# 8. Display results
# ---------------------------------

print("\n==============================")
print("RAG RETRIEVAL RESULTS")
print("==============================")

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("------------------------------")
    print(result["document"])
    print(f"Distance: {result['distance']:.4f}")