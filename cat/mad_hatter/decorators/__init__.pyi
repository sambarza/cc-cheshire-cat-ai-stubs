from cat.mad_hatter.decorators.endpoint import CustomEndpoint as CustomEndpoint, endpoint as endpoint
from cat.mad_hatter.decorators.hook import CatHook as CatHook, hook as hook
from cat.mad_hatter.decorators.plugin_decorator import CatPluginDecorator as CatPluginDecorator, plugin as plugin
from cat.mad_hatter.decorators.tool import CatTool as CatTool, tool as tool

__all__ = ['CatTool', 'tool', 'CatHook', 'hook', 'CustomEndpoint', 'endpoint', 'CatPluginDecorator', 'plugin']
