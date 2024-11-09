from _typeshed import Incomplete
from cat.utils import BaseModelDict
from enum import Enum
from langchain_core.messages import AIMessage, BaseMessage as BaseMessage
from pydantic import BaseModel
from typing import Literal

class Role(Enum):
    AI = 'AI'
    Human = 'Human'

class ModelInteraction(BaseModel):
    model_type: Literal['llm', 'embedder']
    source: str
    prompt: str
    input_tokens: int
    started_at: float
    model_config: Incomplete

class LLMModelInteraction(ModelInteraction):
    model_type: Literal['llm']
    reply: str
    output_tokens: int
    ended_at: float

class EmbedderModelInteraction(ModelInteraction):
    model_type: Literal['embedder']
    source: str
    reply: list[float]

class MessageWhy():
    """Class for wrapping message why

    Variables:
        input (str): input message
        intermediate_steps (List): intermediate steps
        memory (dict): memory
        model_interactions (List[LLMModelInteraction | EmbedderModelInteraction]): model interactions
    """
    input: str
    intermediate_steps: list
    memory: dict
    model_interactions: list[LLMModelInteraction | EmbedderModelInteraction]

class CatMessage():
    """Class for wrapping cat message

    Variables:
        content (str): cat message
        user_id (str): user id
    """
    content: str
    """_summary_
    """
    user_id: str
    type: str
    why: MessageWhy | None

class UserMessage():
    """Class for wrapping user message

    Variables:
        text (str): user message
        user_id (str): user id
    """
    text: str
    """Prompt sent by the user
    """
    user_id: str
    """ID of the user
    """