from abc import ABC, abstractmethod

from promethean.api.vila.abc_role import ABCRole
from datetime import datetime


class ABCMember(ABC):
    @abstractmethod
    def get_uid(self) -> int:
        """
        :return: 用户 uid
        """

    @abstractmethod
    def get_name(self) -> str:
        """
        :return: 昵称
        """

    @abstractmethod
    def get_introduce(self) -> str:
        """
        :return: 个性签名
        """

    @abstractmethod
    def get_avatar_url(self) -> str:
        """
        :return: 头像链接
        """

    @abstractmethod
    async def get_roles(self) -> list[ABCRole]:
        """
        :return: 用户加入的身份组列表
        """

    @abstractmethod
    def get_joined_at(self) -> datetime:
        """
        :return: 用户加入时间
        """
