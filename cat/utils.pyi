from _typeshed import Incomplete
from datetime import timedelta
from pydantic import BaseModel

def to_camel_case(text: str) -> str:
    """Format string to camel case.

    Takes a string of words separated by either hyphens or underscores and returns a string of words in camel case.

    Parameters
    ----------
    text : str
        String of hyphens or underscores separated words.

    Returns
    -------
    str
        Camel case formatted string.
    """
def verbal_timedelta(td: timedelta) -> str:
    """Convert a timedelta in human form.

    The function takes a timedelta and converts it to a human-readable string format.

    Parameters
    ----------
    td : timedelta
        Difference between two dates.

    Returns
    -------
    str
        Human-readable string of time difference.

    Notes
    -----
    This method is used to give the Language Model information time information about the memories retrieved from
    the vector database.

    Examples
    --------
    >>> print(verbal_timedelta(timedelta(days=2, weeks=1))
    'One week and two days ago'
    """
def get_base_url():
    """Allows exposing the base url."""
def get_base_path():
    """Allows exposing the base path."""
def get_plugins_path():
    """Allows exposing the plugins' path."""
def get_static_url():
    """Allows exposing the static server url."""
def get_static_path():
    """Allows exposing the static files' path."""
def is_https(url): ...
def extract_domain_from_url(url): ...
def explicit_error_message(e): ...
def levenshtein_distance(prediction: str, reference: str) -> int: ...
def parse_json(json_string: str, pydantic_model: BaseModel = None) -> dict: ...
def match_prompt_variables(prompt_variables: dict, prompt_template: str) -> tuple[dict, str]:
    """Ensure prompt variables and prompt placeholders map, so there are no issues on mismatches"""
def get_caller_info(): ...
def langchain_log_prompt(langchain_prompt, title): ...
def langchain_log_output(langchain_output, title): ...

class singleton:
    instances: Incomplete
    def __new__(cls, class_): ...

class BaseModelDict(BaseModel):
    model_config: Incomplete
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def get(self, key, default: Incomplete | None = None): ...
    def __delitem__(self, key) -> None: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def __contains__(self, key) -> bool: ...
