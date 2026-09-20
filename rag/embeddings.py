from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():
    """
    Load the sentence-transformer embedding model.
    """

    return SentenceTransformer(MODEL_NAME)


def create_embeddings(model, documents):
    """
    Convert documents into vector embeddings.
    """

    return model.encode(
        documents,
        convert_to_numpy=True
    )