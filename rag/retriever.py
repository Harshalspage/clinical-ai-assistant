import faiss
import numpy as np


def create_vector_index(embeddings):
    """
    Create a FAISS vector index from document embeddings.
    """

    embeddings = np.asarray(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def search_index(index, query_embedding, documents, top_k=3):
    """
    Retrieve the most relevant documents for a query.
    """

    query_embedding = np.asarray(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_position in zip(
        distances[0],
        indices[0]
    ):
        if index_position < len(documents):
            results.append({
                "document": documents[index_position],
                "distance": float(distance)
            })

    return results