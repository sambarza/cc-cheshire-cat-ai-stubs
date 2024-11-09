from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.language_models.llms import LLM
from langchain_openai.chat_models import ChatOpenAI
from typing import Any

class LLMDefault(LLM): ...

class LLMCustom(LLM):
    url: str
    auth_key: str
    options: dict

class CustomOpenAI(ChatOpenAI):
    url: str
    def __init__(self, **kwargs) -> None: ...

class CustomOllama(ChatOllama):
    def __init__(self, **kwargs: Any) -> None: ...
