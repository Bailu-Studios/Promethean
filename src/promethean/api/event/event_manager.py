import asyncio
from typing import List, Dict, Callable, Coroutine, Any
from typing import Type as Class
from inspect import signature, Signature, Parameter
from .event import Event

EventHandler = Callable[[Event], Coroutine[Any, Any, Any]]


class EventManager:
    map: Dict[Class[Event], List[EventHandler]]

    def __init__(self):
        self.map = {}

    async def post(self, context: Event, callback: Callable[[], Coroutine[Any, Any, Any]] = None):
        func_list: List[EventHandler] = self.map.get(context.__class__, [])
        for i in func_list:
            await i(context)
        if context.is_cancelable and not context.is_canceled:
            await callback()

    def subscribe(self, handler: EventHandler):
        sign: Signature = signature(handler)
        params: List[Parameter] = list(sign.parameters.values())
        if len(params) != 1:
            raise UnsupportedFunctionException('Params lens not match.')
        event_type: Class[Event] = params[0].annotation
        func_list: List[EventHandler] = self.map.get(event_type, [])
        if not issubclass(event_type, Event):
            raise IllegalEventException()
        if not asyncio.iscoroutinefunction(handler):
            raise UnsupportedFunctionException('Is not coroutine function.')
        else:
            func_list.append(handler)
        self.map[event_type] = func_list


class UnsupportedFunctionException(Exception):
    msg: str

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return self.msg


class IllegalEventException(Exception):
    def __str__(self):
        return 'Event handle type not match.'
