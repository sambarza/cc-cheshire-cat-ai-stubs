from _typeshed import Incomplete
from cat.convo.messages import LLMModelInteraction
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.outputs.llm_result import LLMResult as LLMResult
from typing import Any

class NewTokenHandler(BaseCallbackHandler):
    stray: Incomplete
    def __init__(self, stray) -> None: ...
    def on_llm_new_token(self, token: str, **kwargs) -> None: ...

class ModelInteractionHandler(BaseCallbackHandler):
    """
    Langchain callback handler for tracking model interactions.
    """
    stray: Incomplete
    def __init__(self, stray, source: str) -> None: ...
    def on_llm_start(self, serialized: dict[str, Any], prompts: list[str], **kwargs) -> None: ...
    def on_llm_end(self, response: LLMResult, **kwargs) -> None: ...
    @property
    def last_interaction(self) -> LLMModelInteraction: ...
