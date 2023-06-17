from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_group import ABCGroup
from promethean.api.vila.abc_room import ABCRoom
from promethean.utils.requestable import Requestable


class Group(ABCGroup, Requestable[ABCGroup]):
    _bot: ABCBot
    _group_id: int
    _group_name: str
    _room_id_list: list[int]
    _link: str = '/vila/api/bot/platform/getVillaGroupRoomList'

    def __init__(self, bot: ABCBot, group_id: int, group_name: str, room_id_list: list[int]):
        self._bot = bot
        self._group_id = group_id
        self._group_name = group_name
        self._room_id_list = room_id_list

    def get_group_id(self) -> int:
        """
        :return: 分组 id
        """
        return self._group_id

    def get_group_name(self) -> str:
        """
        :return: 分组名称
        """
        return self._group_name

    async def get_room_list(self) -> list[ABCRoom]:
        """
        :return: 房间信息
        """
        out = []
        for room_id in self._room_id_list:
            out.append(await self._bot.get_room(room_id))
        return out

    @classmethod
    def get_link(cls) -> str:
        return cls._link

    @classmethod
    def resolve(cls, bot: ABCBot, data: dict) -> ABCGroup:
        return Group(
            bot=bot,
            group_id=data['group_id'],
            group_name=data['group_name'],
            room_id_list=data['room_id_list']
        )
