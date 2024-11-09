from _typeshed import Incomplete
from pydantic import BaseModel

class LLMSettings(BaseModel):
    model_config: Incomplete
    @classmethod
    def get_llm_from_config(cls, config): ...

class LLMDefaultConfig(LLMSettings):
    model_config: Incomplete

class LLMCustomConfig(LLMSettings):
    url: str
    auth_key: str
    options: str
    @classmethod
    def get_llm_from_config(cls, config): ...
    model_config: Incomplete

class LLMOpenAICompatibleConfig(LLMSettings):
    url: str
    temperature: float
    model_name: str
    api_key: str
    streaming: bool
    model_config: Incomplete

class LLMOpenAIChatConfig(LLMSettings):
    openai_api_key: str
    model_name: str
    temperature: float
    streaming: bool
    model_config: Incomplete

class LLMOpenAIConfig(LLMSettings):
    openai_api_key: str
    model_name: str
    temperature: float
    streaming: bool
    model_config: Incomplete

class LLMAzureChatOpenAIConfig(LLMSettings):
    openai_api_key: str
    model_name: str
    azure_endpoint: str
    max_tokens: int
    openai_api_type: str
    openai_api_version: str
    azure_deployment: str
    streaming: bool
    model_config: Incomplete

class LLMAzureOpenAIConfig(LLMSettings):
    openai_api_key: str
    azure_endpoint: str
    max_tokens: int
    api_type: str
    api_version: str
    azure_deployment: str
    model_name: str
    streaming: bool
    model_config: Incomplete

class LLMCohereConfig(LLMSettings):
    cohere_api_key: str
    model: str
    temperature: float
    streaming: bool
    model_config: Incomplete

class LLMHuggingFaceTextGenInferenceConfig(LLMSettings):
    inference_server_url: str
    max_new_tokens: int
    top_k: int
    top_p: float
    typical_p: float
    temperature: float
    repetition_penalty: float
    model_config: Incomplete

class LLMHuggingFaceEndpointConfig(LLMSettings):
    endpoint_url: str
    huggingfacehub_api_token: str
    task: str
    max_new_tokens: int
    top_k: int
    top_p: float
    temperature: float
    return_full_text: bool
    model_config: Incomplete

class LLMOllamaConfig(LLMSettings):
    base_url: str
    model: str
    num_ctx: int
    repeat_last_n: int
    repeat_penalty: float
    temperature: float
    model_config: Incomplete

class LLMGeminiChatConfig(LLMSettings):
    '''Configuration for the Gemini large language model (LLM).

    This class inherits from the `LLMSettings` class and provides default values for the following attributes:

    * `google_api_key`: The Google API key used to access the Google Natural Language Processing (NLP) API.
    * `model`: The name of the LLM model to use. In this case, it is set to "gemini".
    * `temperature`: The temperature of the model, which controls the creativity and variety of the generated responses.
    * `top_p`: The top-p truncation value, which controls the probability of the generated words.
    * `top_k`: The top-k truncation value, which controls the number of candidate words to consider during generation.
    * `max_output_tokens`: The maximum number of tokens to generate in a single response.

    The `LLMGeminiChatConfig` class is used to create an instance of the Gemini LLM model, which can be used to generate text in natural language.
    '''
    google_api_key: str
    model: str
    temperature: float
    top_p: int
    top_k: int
    max_output_tokens: int
    model_config: Incomplete

class LLMAnthropicChatConfig(LLMSettings):
    api_key: str
    model: str
    temperature: float
    max_tokens: int
    max_retries: int
    model_config: Incomplete

def get_allowed_language_models(): ...
def get_llm_from_name(name_llm: str):
    """Find the llm adapter class by name"""
def get_llms_schemas(): ...
