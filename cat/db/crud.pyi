from cat.db import models

def get_settings(search: str = '') -> list[dict]: ...
def get_settings_by_category(category: str) -> list[dict]: ...
def create_setting(payload: models.Setting) -> dict: ...
def get_setting_by_name(name: str) -> dict: ...
def get_setting_by_id(setting_id: str) -> dict: ...
def delete_setting_by_id(setting_id: str) -> None: ...
def delete_settings_by_category(category: str) -> None: ...
def update_setting_by_id(payload: models.Setting) -> dict: ...
def upsert_setting_by_name(payload: models.Setting) -> models.Setting: ...
def get_users() -> dict[str, dict]: ...
def update_users(users: dict[str, dict]) -> dict[str, dict]: ...
