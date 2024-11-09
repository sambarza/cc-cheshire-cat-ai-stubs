import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from cat.auth.permissions import AuthPermission as AuthPermission, AuthResource as AuthResource, AuthUserInfo as AuthUserInfo
from cat.looking_glass.stray_cat import StrayCat
from fastapi import Request as Request, WebSocket as WebSocket
from fastapi.requests import HTTPConnection as HTTPConnection

class ConnectionAuth(ABC, metaclass=abc.ABCMeta):
    resource: Incomplete
    permission: Incomplete
    def __init__(self, resource: AuthResource, permission: AuthPermission) -> None: ...
    async def __call__(self, connection: HTTPConnection) -> StrayCat: ...
    @abstractmethod
    async def extract_credentials(self, connection: Request | WebSocket) -> tuple[str] | None: ...
    @abstractmethod
    async def get_user_stray(self, user: AuthUserInfo, connection: Request | WebSocket) -> StrayCat: ...
    @abstractmethod
    def not_allowed(self, connection: Request | WebSocket): ...

class HTTPAuth(ConnectionAuth):
    async def extract_credentials(self, connection: Request) -> tuple[str, str] | None:
        """
        Extract user_id and token/key from headers
        """
    async def get_user_stray(self, user: AuthUserInfo, connection: Request) -> StrayCat: ...
    def not_allowed(self, connection: Request): ...

class WebSocketAuth(ConnectionAuth):
    async def extract_credentials(self, connection: WebSocket) -> tuple[str, str] | None:
        """
        Extract user_id from WebSocket path params
        Extract token from WebSocket query string
        """
    async def get_user_stray(self, user: AuthUserInfo, connection: WebSocket) -> StrayCat: ...
    def not_allowed(self, connection: WebSocket): ...

class CoreFrontendAuth(HTTPAuth):
    async def extract_credentials(self, connection: Request) -> tuple[str, str] | None:
        """
        Extract user_id from cookie
        """
    def not_allowed(self, connection: Request): ...
