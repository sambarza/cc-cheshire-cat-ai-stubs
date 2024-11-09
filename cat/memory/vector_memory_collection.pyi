from _typeshed import Incomplete
from typing import Any, Iterable

class VectorMemoryCollection:
    client: Incomplete
    collection_name: Incomplete
    embedder_name: Incomplete
    embedder_size: Incomplete
    def __init__(self, client: Any, collection_name: str, embedder_name: str, embedder_size: int) -> None: ...
    def check_embedding_size(self) -> None: ...
    def create_db_collection_if_not_exists(self) -> None: ...
    def create_collection(self) -> None: ...
    def add_point(self, content: str, vector: Iterable, metadata: dict = None, id: str | None = None, **kwargs: Any) -> list[str]:
        """Add a point (and its metadata) to the vectorstore.

        Args:
            content: original text.
            vector: Embedding vector.
            metadata: Optional metadata dict associated with the text.
            id:
                Optional id to associate with the point. Id has to be a uuid-like string.

        Returns:
            Point id as saved into the vectorstore.
        """
    def delete_points_by_metadata_filter(self, metadata: Incomplete | None = None): ...
    def delete_points(self, points_ids):
        """Delete point in collection"""
    def recall_memories_from_embedding(self, embedding, metadata: Incomplete | None = None, k: int = 5, threshold: Incomplete | None = None):
        """Retrieve similar memories from embedding"""
    def get_points(self, ids: list[str]):
        """Get points by their ids."""
    def get_all_points(self, limit: int = 10000, offset: str | None = None):
        """Retrieve all the points in the collection with an optional offset and limit."""
    def db_is_remote(self): ...
    snapshot_info: Incomplete
    def save_dump(self, folder: str = 'dormouse/') -> None: ...
