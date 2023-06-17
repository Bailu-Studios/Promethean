from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_room import ABCRoom, RoomType, DefaultNotifyType, SendMsgAuthRange
from promethean.utils.requestable import Requestable


class Room(ABCRoom, Requestable[ABCRoom]):
    _bot: ABCBot
    _room_id: int
    _room_name: str
    _room_type: RoomType
    _group_id: int
    _room_default_notify_type: DefaultNotifyType
    _send_msg_auth_range: SendMsgAuthRange
    _link: str = '/vila/api/bot/platform/getRoom'

    def __init__(self, bot: ABCBot,
                 room_id: int,
                 room_name: str,
                 room_type: RoomType,
                 group_id: int,
                 room_default_notify_type: DefaultNotifyType,
                 send_msg_auth_range: SendMsgAuthRange):
        self._bot = bot
        self._room_id = room_id
        self._room_name = room_name
        self._room_type = room_type
        self._group_id = group_id
        self._room_default_notify_type = room_default_notify_type
        self._send_msg_auth_range = send_msg_auth_range

    def get_id(self) -> int:
        """
        :return: 房间 id
        """
        return self._group_id

    def get_name(self) -> str:
        """
        :return: 房间名称
        """
        return self._room_name

    def get_type(self) -> RoomType:
        """
        :return: 房间类型
        """
        return self._room_type

    def get_group(self) -> int:
        """
        :return: 分组 id
        """
        return self._group_id

    def get_default_notify_type(self) -> DefaultNotifyType:
        """
        :return: 房间默认通知类型
        """
        return self._room_default_notify_type

    def get_send_msg_auth_range(self) -> SendMsgAuthRange:
        """
        :return: 房间消息发送权限范围设置
        """
        return self._send_msg_auth_range

    @classmethod
    def get_link(cls) -> str:
        return cls._link

    @classmethod
    def resolve(cls, bot: ABCBot, data: dict) -> ABCRoom:
        return Room(
            bot=bot,
            room_id=data['room_id'],
            room_name=data['room_name'],
            room_type=RoomType.resolve(data['room_type']),
            group_id=data['group_id'],
            room_default_notify_type=DefaultNotifyType.resolve(data['room_default_notify_type']),
            send_msg_auth_range=SendMsgAuthRange.resolve(data['send_msg_auth_range']),
        )
