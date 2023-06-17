from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_villa import ABCVilla
from promethean.utils.requestable import Requestable


class Villa(ABCVilla, Requestable[ABCVilla]):
    _bot: ABCBot
    _villa_id: int
    _name: str
    _villa_avatar_url: str
    _owner_uid: int
    _is_official: bool
    _introduce: str
    _category_id: int
    _tags: list[str]
    _link: str = '/vila/api/bot/platform/getVilla'

    def __init__(self,
                 bot: ABCBot,
                 villa_id: int = '',
                 name: str = '',
                 villa_avatar_url: str = '',
                 owner_uid: int = 0,
                 is_official: bool = False,
                 introduce: str = '',
                 category_id: int = 0,
                 tags: list[str] = None):
        if tags is None:
            tags = []
        self._bot = bot
        self._villa_id = villa_id
        self._name = name
        self._villa_avatar_url = villa_avatar_url
        self._owner_uid = owner_uid
        self._is_official = is_official
        self._introduce = introduce
        self._category_id = category_id
        self._tags = tags

    def get_villa_id(self) -> int:
        """
        :return: 别野 id
        """
        return self._villa_id

    def get_name(self) -> str:
        """
        :return: 别野名称
        """
        return self._name

    def get_villa_avatar_url(self) -> str:
        """
        :return: 别野头像链接
        """
        return self._villa_avatar_url

    def get_owner_uid(self) -> int:
        """
        :return: 别野主人 id
        """
        return self._owner_uid

    def get_is_official(self) -> bool:
        """
        :return: 是否是官方别野
        """
        return self._is_official

    def get_introduce(self) -> str:
        """
        :return: 介绍
        """
        return self._introduce

    def get_category_id(self) -> int:
        """
        :return:
        """
        return self._category_id

    def get_tags(self) -> list[str]:
        """
        :return: 标签
        """
        return self._tags

    @classmethod
    def get_link(cls) -> str:
        return cls._link

    @classmethod
    def resolve(cls, bot: ABCBot, data: dict) -> ABCVilla:
        return Villa(
            bot=bot,
            villa_id=data['villa_id'],
            name=data['name'],
            villa_avatar_url=data['villa_avatar_url'],
            owner_uid=data['owner_uid'],
            is_official=data['is_official'],
            introduce=data['introduce'],
            category_id=data['category_id'],
            tags=data['tags']
        )
