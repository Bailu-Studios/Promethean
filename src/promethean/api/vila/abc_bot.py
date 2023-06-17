from abc import ABC, abstractmethod
from inspect import signature, getmembers
from typing import Type as Class, Callable, Coroutine, Any

from promethean.api.event.event import Event
from promethean.api.event.event_manager import EventHandler, EventManager
from promethean.api.vila.abc_group import ABCGroup
from promethean.api.vila.abc_member import ABCMember
from promethean.api.vila.abc_message import ABCMessage
from promethean.api.vila.abc_role import ABCRole
from promethean.api.vila.abc_room import ABCRoom
from promethean.api.vila.abc_villa import ABCVilla


class ABCBot(ABC):
    _events: EventManager = EventManager()

    @abstractmethod
    def get_bot_uid(self):
        """
        :return: Bot 实例所对应的用户ID
        """

    @abstractmethod
    async def get_villa(self) -> ABCVilla:
        """
        :return: 别野
        """

    @abstractmethod
    async def get_member(self, member_id: int) -> ABCMember:
        """
        :param member_id: 用户 ID
        :return: 用户
        """

    @abstractmethod
    async def get_role(self, role_id: int) -> ABCRole:
        """
        :param role_id: 身份组 ID
        :return: 身份组
        """

    @abstractmethod
    async def get_groups(self) -> list[ABCGroup]:
        """
        :return: 分组列表
        """

    @abstractmethod
    async def get_room(self, room_id: int) -> ABCRoom:
        """
        :param room_id: 房间 ID
        :return: 房间
        """

    @abstractmethod
    async def send_msg(self, room_id: int, msg: ABCMessage) -> str:
        """
        :param room_id: 房间 ID
        :param msg: 消息内容
        :return: 消息 ID
        """

    def post_event(self, event: Event, callback: Callable[[], Coroutine[Any, Any, Any]] = None):
        self._events.post(event, callback)

    def subscribe_event(self):
        def subscribe(handler: EventHandler):
            """
            :param handler: 事件处理器
            """
            parameters = list(signature(handler).parameters.values())
            if len(parameters) != 1:
                return
            if parameters[0].annotation != Class[Event]:
                return
            self._events.subscribe(handler)

        return subscribe

    def subscribe_events(self):
        def subscribe(handlers: object):
            """
            :param handlers: 事件处理器工具对象
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

        return subscribe
