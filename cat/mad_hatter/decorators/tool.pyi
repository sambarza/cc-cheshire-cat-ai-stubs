from _typeshed import Incomplete
from typing import Callable

class CatTool:
    func: Incomplete
    procedure_type: str
    name: Incomplete
    description: Incomplete
    return_direct: Incomplete
    triggers_map: Incomplete
    signature: Incomplete
    def __init__(self, name: str, func: Callable, return_direct: bool = False, examples: list[str] = []) -> None: ...
    @property
    def start_examples(self): ...
    def run(self, input_by_llm: str, stray) -> str: ...
    class Config:
        extra: str

def tool(*args: str | Callable, return_direct: bool = False, examples: list[str] = []) -> Callable:
    '''
    Make tools out of functions, can be used with or without arguments.
    Requires:
        - Function must be of type (str, cat) -> str
        - Function must have a docstring
    Examples:
        .. code-block:: python
            @tool
            def search_api(query: str, cat) -> str:
                # Searches the API for the query.
                return "https://api.com/search?q=" + query
            @tool("search", return_direct=True)
            def search_api(query: str, cat) -> str:
                # Searches the API for the query.
                return "https://api.com/search?q=" + query
    '''
