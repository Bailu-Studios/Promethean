from abc import ABC

from promethean.api.vila.abc_room import ABCRoom


class ABCGroup(ABC):
    def get_group_id(self) -> int:
        """
        :return: 分组 id
        """

    def get_group_name(self) -> str:
        """
        :return: 分组名称
        """

    async def get_room_list(self) -> list[ABCRoom]:
        """
        :return: 房间信息
        """
