from _typeshed import Incomplete
from langchain_core.embeddings import Embeddings

class DumbEmbedder(Embeddings):
    """Default Dumb Embedder.

    This is the default embedder used for testing purposes
    and to replace official embedders when they are not available.

    Notes
    -----
    This class relies on the `CountVectorizer`[1]_ offered by Scikit-learn.
    This embedder uses a naive approach to extract features from a text and build an embedding vector.
    Namely, it looks for pairs of characters in text starting form a vocabulary with all possible pairs of
    printable characters, digits excluded.
    """
    embedder: Incomplete
    def __init__(self) -> None: ...
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of text and returns the embedding vectors that are lists of floats."""
    def embed_query(self, text: str) -> list[float]:
        """Embed a string of text and returns the embedding vector as a list of floats."""

class CustomOpenAIEmbeddings(Embeddings):
    """Use LLAMA2 as embedder by calling a self-hosted lama-cpp-python instance."""
    url: Incomplete
    def __init__(self, url) -> None: ...
    def embed_documents(self, texts: list[str]) -> list[list[float]]: ...
    def embed_query(self, text: str) -> list[float]: ...
