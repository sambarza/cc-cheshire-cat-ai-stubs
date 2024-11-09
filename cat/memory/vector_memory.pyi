from _typeshed import Incomplete

from cat.memory.vector_memory_collection import VectorMemoryCollection

class VectorMemory:
    def delete_collection(self, collection_name: str):
        """Delete specific vector collection"""
    def get_collection(self, collection_name: str):
        """Get collection info"""

    @property
    def episodic(self) -> VectorMemoryCollection: ...

    @property
    def declarative(self) -> VectorMemoryCollection: ...

    @property
    def procedural(self) -> VectorMemoryCollection: ...