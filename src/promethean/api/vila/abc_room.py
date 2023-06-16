from abc import ABC
from enum import Enum

from promethean.api.vila.abc_role import ABCRole


class RoomType(Enum):
    CHAT_ROOM = 'BOT_PLATFORM_ROOM_TYPE_CHAT_ROOM'  # 聊天房间
    POST_ROOM = 'BOT_PLATFORM_ROOM_TYPE_POST_ROOM'  # 帖子房间
    SCENE_ROOM = 'BOT_PLATFORM_ROOM_TYPE_SCENE_ROOM'  # 场景房间
    INVALID = 'BOT_PLATFORM_ROOM_TYPE_INVALID'  # 无效


class DefaultNotifyType(Enum):
    NOTIFY = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_NOTIFY'  # 默认通知
    IGNORE = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_IGNORE'  # 默认免打扰
    INVALID = 'BOT_PLATFORM_DEFAULT_NOTIFY_TYPE_INVALID'  # 无效


class SendMsgAuthRange:
    def get_is_all_send_msg(self) -> bool:
        """
        :return: 是否全局可发送
        """
        ...

    async def get_roles(self) -> list[ABCRole]:
        """
        :return: 可发消息的身份组 id
        """
        ...


class ABCRoom(ABC):
    def get_id(self) -> int:
        """
        :return: 房间 id
        """

    def get_name(self) -> str:
        """
        :return: 房间名称
        """

    def get_type(self) -> RoomType:
        """
        :return: 房间类型
        """

    def get_group(self) -> int:
        """
        :return: 分组 id
        """

    def get_default_notify_type(self) -> DefaultNotifyType:
        """
        :return: 房间默认通知类型
        """

    def get_send_msg_auth_range(self) -> SendMsgAuthRange:
        """
        :return: 房间消息发送权限范围设置
        """
