from abc import ABC, abstractmethod


class ABCVilla(ABC):
    @abstractmethod
    def get_villa_id(self) -> int:
        """
        :return: 别野 id
        """

    @abstractmethod
    def get_name(self) -> str:
        """
        :return: 别野名称
        """

    @abstractmethod
    def get_villa_avatar_url(self) -> str:
        """
        :return: 别野头像链接
        """

    @abstractmethod
    def get_owner_uid(self) -> int:
        """
        :return: 别野主人 id
        """

    @abstractmethod
    def get_is_official(self) -> bool:
        """
        :return: 是否是官方别野
        """

    @abstractmethod
    def get_introduce(self) -> str:
        """
        :return: 介绍
        """

    @abstractmethod
    def get_category_id(self) -> int:
        """
        :return:
        """

    @abstractmethod
    def get_tags(self) -> list[str]:
        """
        :return: 标签
        """
