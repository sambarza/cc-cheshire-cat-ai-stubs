from _typeshed import Incomplete
from pydantic import BaseModel

class EmbedderSettings(BaseModel):
    model_config: Incomplete
    @classmethod
    def get_embedder_from_config(cls, config): ...

class EmbedderFakeConfig(EmbedderSettings):
    size: int
    model_config: Incomplete

class EmbedderDumbConfig(EmbedderSettings):
    model_config: Incomplete

class EmbedderOpenAICompatibleConfig(EmbedderSettings):
    url: str
    model_config: Incomplete

class EmbedderOpenAIConfig(EmbedderSettings):
    openai_api_key: str
    model: str
    model_config: Incomplete

class EmbedderAzureOpenAIConfig(EmbedderSettings):
    openai_api_key: str
    model: str
    azure_endpoint: str
    openai_api_type: str
    openai_api_version: str
    deployment: str
    model_config: Incomplete

class EmbedderCohereConfig(EmbedderSettings):
    cohere_api_key: str
    model: str
    model_config: Incomplete

FastEmbedModels: Incomplete

class EmbedderQdrantFastEmbedConfig(EmbedderSettings):
    model_name: FastEmbedModels
    max_length: int
    doc_embed_type: str
    cache_dir: str
    model_config: Incomplete

class EmbedderGeminiChatConfig(EmbedderSettings):
    """Configuration for Gemini Chat Embedder.

    This class contains the configuration for the Gemini Embedder.
    """
    google_api_key: str
    model: str
    model_config: Incomplete

def get_allowed_embedder_models(): ...
def get_embedder_from_name(name_embedder: str):
    """Find the llm adapter class by name"""
def get_embedders_schemas(): ...
