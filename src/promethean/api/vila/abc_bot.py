from abc import ABC
from inspect import signature, getmembers
from typing import Type as Class

from promethean.api.event.event import Event
from promethean.api.event.event_manager import EventHandler, EventManager


class ABCBot(ABC):
    _events: EventManager = EventManager()
    token: str

    def __init__(self, token: str):
        self.token = token

    def subscribe_event(self, handler: EventHandler):
        """
        :param handler: 事件处理器
        :return: None
        """
        parameters = list(signature(handler).parameters.values())
        if len(parameters) != 1:
            return
        if parameters[0].annotation != Class[Event]:
            return
        self._events.subscribe(handler)

    def subscribe_events(self, handlers: object):
        """
        :param handlers: 事件处理器工具对象
        :return: None
        """
        methods = getmembers(handlers)
        for method in methods:
            func = method[1]
            parameters = list(signature(func).parameters.values())
            if len(parameters) != 1:
                continue
            if parameters[0].annotation != Class[Event]:
                continue
            self._events.subscribe(func)
