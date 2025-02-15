from _typeshed import Incomplete
from pydantic import BaseModel

class PluginSettingsModel(BaseModel): ...

class Plugin:
    py_files: Incomplete
    def __init__(self, plugin_path: str) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def settings_schema(self): ...
    def settings_model(self): ...
    def load_settings(self): ...
    def save_settings(self, settings: dict): ...
    def plugin_specific_error_message(self): ...
    @property
    def path(self): ...
    @property
    def id(self): ...
    @property
    def manifest(self): ...
    @property
    def active(self): ...
    @property
    def hooks(self): ...
    @property
    def tools(self): ...
    @property
    def forms(self): ...
    @property
    def endpoints(self): ...
