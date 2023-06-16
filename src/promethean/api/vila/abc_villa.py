from abc import ABC


class ABCVilla(ABC):

    def get_villa_id(self) -> int:
        """
        :return: 别野 id
        """

    def get_name(self) -> str:
        """
        :return: 别野名称
        """

    def get_villa_avatar_url(self) -> str:
        """
        :return: 别野头像链接
        """

    def get_owner_uid(self) -> int:
        """
        :return: 别野主人 id
        """

    def get_is_official(self) -> bool:
        """
        :return: 是否是官方别野
        """

    def get_introduce(self) -> str:
        """
        :return: 介绍
        """

    def get_category_id(self) -> int:
        """
        :return:
        """

    def get_tags(self) -> list[str]:
        """
        :return: 标签
        """
