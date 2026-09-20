from pathlib import Path


def load_knowledge_base(file_path):
    """
    Load the clinical knowledge base from a text file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Knowledge base not found: {file_path}"
        )

    return path.read_text(encoding="utf-8")