from pydantic import BaseModel

def generate_uuid(): ...
def generate_timestamp(): ...

class SettingBody(BaseModel):
    name: str
    value: dict | list
    category: str | None

class Setting(SettingBody):
    setting_id: str
    updated_at: int
