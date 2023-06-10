from inspect import getmembers, signature
from typing import Callable, Type as Class, Coroutine, Any
import promethean
from promethean.bot import Bot
from promethean.api.event import Event


class SubscribeEvent:
    bot: Bot

    def __init__(self, bot: Bot = promethean.mainBot):
        self.bot = bot
        pass

    def __call__(self, handler: Callable[['Event'], Coroutine[Any, Any, Any]]):
        parameters = list(signature(handler).parameters.values())
        if len(parameters) != 1: return
        if parameters[0].annotation != Class[Event]: return
        self.bot.events.subscribe(handler)


class SubscribeEvents:
    bot: Bot

    def __init__(self, bot: Bot = promethean.mainBot):
        self.bot = bot
        pass

    def __call__(self, handlers: object):
        methods = getmembers(handlers)
        for method in methods:
            func = method[1]
            parameters = list(signature(func).parameters.values())
            if len(parameters) != 1: continue
            if parameters[0].annotation != Class[Event]: continue
            self.bot.events.subscribe(func)
