from typing import List, Dict, Callable, Coroutine, Any
from typing import Type as Class
from inspect import signature, Signature
from .event import Event


class EventManager:
    map: Dict[Class['Event'], List[Callable[['Event'], Coroutine[Any, Any, Any]]]]

    def __init__(self):
        self.map = {}

    async def post(self, context: 'Event'):
        func_list: List[Callable[['Event'], Coroutine[Any, Any, Any]]] = self.map.get(context.__class__, [])
        for i in func_list:
            await i(context)

    def subscribe(self, handler: Callable[['Event'], Coroutine[Any, Any, Any]]):
        sig: Signature = signature(handler)
        event_type: Class['Event'] = list(sig.parameters.values())[0].annotation
        func_list: List[Callable[['Event'], Coroutine[Any, Any, Any]]] = self.map.get(event_type, [])
        func_list.append(handler)
        self.map[event_type] = func_list
