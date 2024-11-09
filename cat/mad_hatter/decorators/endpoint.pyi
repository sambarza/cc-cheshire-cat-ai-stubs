from _typeshed import Incomplete
from typing import Callable

class CustomEndpoint:
    prefix: Incomplete
    path: Incomplete
    function: Incomplete
    tags: Incomplete
    methods: Incomplete
    kwargs: Incomplete
    name: Incomplete
    def __init__(self, prefix: str, path: str, function: Callable, methods, tags, **kwargs) -> None: ...
    api_route: Incomplete
    def set_api_route(self, api_route) -> None: ...
    cheshire_cat_api: Incomplete
    def activate(self, cheshire_cat_api) -> None: ...
    def deactivate(self) -> None: ...

class Endpoint:
    cheshire_cat_api: Incomplete
    default_prefix: str
    default_tags: Incomplete
    def endpoint(cls, path, methods, prefix=..., tags=..., **kwargs) -> Callable:
        '''
        Define a custom API endpoint, parameters are the same as FastAPI path operation.
        Examples:
            .. code-block:: python
                from cat.mad_hatter.decorators import endpoint

                @endpoint.endpoint(path="/hello", methods=["GET"])
                def my_endpoint():
                    return {"Hello":"Alice"}
        '''
    def get(cls, path, prefix=..., response_model: Incomplete | None = None, tags=..., **kwargs) -> Callable:
        '''
        Define a custom API endpoint for GET operation, parameters are the same as FastAPI path operation.
        Examples:
            .. code-block:: python
                from cat.mad_hatter.decorators import endpoint

                @endpoint.get(path="/hello")
                def my_get_endpoint():
                    return {"Hello":"Alice"}
        '''
    def post(cls, path, prefix=..., response_model: Incomplete | None = None, tags=..., **kwargs) -> Callable:
        '''
        Define a custom API endpoint for POST operation, parameters are the same as FastAPI path operation.
        Examples:
            .. code-block:: python

                from cat.mad_hatter.decorators import endpoint
                from pydantic import BaseModel

                class Item(BaseModel):
                    name: str
                    description: str

                @endpoint.post(path="/hello")
                def my_post_endpoint(item: Item):
                    return {"Hello": item.name, "Description": item.description}
        '''

endpoint: Endpoint
