from abc import ABC, abstractmethod

from promethean.api.vila.abc_room import ABCRoom


class ABCGroup(ABC):
    @abstractmethod
    def get_group_id(self) -> int:
        """
        :return: 分组 id
        """

    @abstractmethod
    def get_group_name(self) -> str:
        """
        :return: 分组名称
        """

    @abstractmethod
    async def get_room_list(self) -> list[ABCRoom]:
        """
        :return: 房间信息
        """
