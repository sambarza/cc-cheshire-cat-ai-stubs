from cat.utils import BaseModelDict
from enum import Enum

class AuthResource(str, Enum):
    STATUS = 'STATUS'
    MEMORY = 'MEMORY'
    CONVERSATION = 'CONVERSATION'
    SETTINGS = 'SETTINGS'
    LLM = 'LLM'
    EMBEDDER = 'EMBEDDER'
    AUTH_HANDLER = 'AUTH_HANDLER'
    USERS = 'USERS'
    UPLOAD = 'UPLOAD'
    PLUGINS = 'PLUGINS'
    STATIC = 'STATIC'

class AuthPermission(str, Enum):
    WRITE = 'WRITE'
    EDIT = 'EDIT'
    LIST = 'LIST'
    READ = 'READ'
    DELETE = 'DELETE'

def get_full_permissions() -> dict[AuthResource, list[AuthPermission]]:
    """
    Returns all available resources and permissions.
    """
def get_base_permissions() -> dict[AuthResource, list[AuthPermission]]:
    """
    Returns the default permissions for new users (chat only!).
    """

class AuthUserInfo(BaseModelDict):
    """
    Class to represent token content after the token has been decoded.
    Will be creted by AuthHandler(s) to standardize their output.
    Core will use this object to retrieve or create a StrayCat (session)
    """
    id: str
    name: str
    permissions: dict[AuthResource, list[AuthPermission]]
    extra: BaseModelDict
