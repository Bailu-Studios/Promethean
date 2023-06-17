from abc import ABC, abstractmethod
from enum import Enum


class RoomType(Enum):
    CHAT_ROOM = 'BOT_PLATFORM_ROOM_TYPE_CHAT_ROOM'  # 聊天房间
    POST_ROOM = 'BOT_PLATFORM_ROOM_TYPE_POST_ROOM'  # 帖子房间
    SCENE_ROOM = 'BOT_PLATFORM_ROOM_TYPE_SCENE_ROOM'  # 场景房间
    INVALID = 'BOT_PLATFORM_ROOM_TYPE_INVALID'  # 无效

    @classmethod
    def resolve(cls, data: str) -> 'RoomType':
        for i in RoomType:
            if i.value == data:
                return i
        return RoomType.INVALID


class DefaultNotifyType(Enum):
    NOTIFY = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_NOTIFY'  # 默认通知
    IGNORE = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_IGNORE'  # 默认免打扰
    INVALID = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_INVALID'  # 无效

    @classmethod
    def resolve(cls, data: str) -> 'DefaultNotifyType':
        for i in DefaultNotifyType:
            if i.value == data:
                return i
        return DefaultNotifyType.INVALID


class SendMsgAuthRange:
    is_all_send_msg: bool
    roles: list[int]

    def __init__(self, is_all_send_msg: bool, roles: list[int]):
        self.is_all_send_msg = is_all_send_msg
        self.roles = roles

    def get_is_all_send_msg(self) -> bool:
        """
        :return: 是否全局可发送
        """
        return self.is_all_send_msg

    async def get_roles(self) -> list[int]:
        """
        :return: 可发消息的身份组 id
        """
        return self.roles

    @classmethod
    def resolve(cls, data: dict) -> 'SendMsgAuthRange':
        return SendMsgAuthRange(
            is_all_send_msg=data['is_all_send_msg'],
            roles=data['roles']
        )


class ABCRoom(ABC):
    @abstractmethod
    def get_id(self) -> int:
        """
        :return: 房间 id
        """

    @abstractmethod
    def get_name(self) -> str:
        """
        :return: 房间名称
        """

    @abstractmethod
    def get_type(self) -> RoomType:
        """
        :return: 房间类型
        """

    @abstractmethod
    def get_group(self) -> int:
        """
        :return: 分组 id
        """

    @abstractmethod
    def get_default_notify_type(self) -> DefaultNotifyType:
        """
        :return: 房间默认通知类型
        """

    @abstractmethod
    def get_send_msg_auth_range(self) -> SendMsgAuthRange:
        """
        :return: 房间消息发送权限范围设置
        """
