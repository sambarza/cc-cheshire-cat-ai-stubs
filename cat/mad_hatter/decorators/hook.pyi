from _typeshed import Incomplete
from typing import Callable

class CatHook:
    function: Incomplete
    name: Incomplete
    priority: Incomplete
    def __init__(self, name: str, func: Callable, priority: int) -> None: ...

def hook(*args: str | Callable, priority: int = 1) -> Callable:
    '''
    Make hooks out of functions, can be used with or without arguments.
    Examples:
        .. code-block:: python
            @hook
            def on_message(message: Message) -> str:
                return "Hello!"
            @hook("on_message", priority=2)
            def on_message(message: Message) -> str:
                return "Hello!"
    '''
