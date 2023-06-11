from inspect import getmembers, signature
from typing import Type as Class

import promethean
from promethean.api.event import Event, EventHandler
from promethean.bot import Bot


class SubscribeEvent:
    bot: Bot

    def __init__(self, bot: Bot = promethean.mainBot):
        self.bot = bot
        pass

    def __call__(self, handler: EventHandler):
        parameters = list(signature(handler).parameters.values())
        if len(parameters) != 1:
            return
        if parameters[0].annotation != Class[Event]:
            return
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
            if len(parameters) != 1:
                continue
            if parameters[0].annotation != Class[Event]:
                continue
            self.bot.events.subscribe(func)
