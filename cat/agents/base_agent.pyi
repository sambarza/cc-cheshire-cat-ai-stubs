import abc
from abc import ABC, abstractmethod
from cat.utils import BaseModelDict

class AgentOutput(BaseModelDict):
    output: str | None
    intermediate_steps: list
    return_direct: bool

class BaseAgent(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def execute(*args, **kwargs) -> AgentOutput: ...
