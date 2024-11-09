from _typeshed import Incomplete

from cat.memory.vector_memory import VectorMemory

class LongTermMemory:
    """Cat's non-volatile memory.

    This is an abstract class to interface with the Cat's vector memory collections.

    Attributes
    ----------
    vectors : VectorMemory
        Vector Memory collection.
    """
    vectors: VectorMemory
    def __init__(self, vector_memory_config={}) -> None: ...
