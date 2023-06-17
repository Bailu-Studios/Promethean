from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_member import ABCMember
from promethean.api.vila.abc_role import ABCRole
from datetime import datetime

from promethean.utils.requestable import Requestable


class Member(ABCMember, Requestable[ABCMember]):
    _bot: ABCBot
    _uid: int
    _name: str
    _introduce: str
    _avatar_url: str
    _role_id_list: list[int]
    _joined_at: datetime
    _link = '/vila/api/bot/platform/getMember'

    def __init__(self,
                 bot: ABCBot,
                 uid: int,
                 name: str,
                 introduce: str,
                 avatar_url: str,
                 role_id_list: list[int],
                 joined_at: datetime
                 ):
        self._bot = bot
        self._uid = uid
        self._name = name
        self._introduce = introduce
        self._avatar_url = avatar_url
        self._role_id_list = role_id_list
        self._joined_at = joined_at

    def get_uid(self) -> int:
        """
        :return: 用户 uid
        """
        return self._uid

    def get_name(self) -> str:
        """
        :return: 昵称
        """
        return self._name

    def get_introduce(self) -> str:
        """
        :return: 个性签名
        """
        return self._introduce

    def get_avatar_url(self) -> str:
        """
        :return: 头像链接
        """
        return self._avatar_url

    async def get_roles(self) -> list[ABCRole]:
        """
        :return: 用户加入的身份组列表
        """

    def get_joined_at(self) -> datetime:
        """
        :return: 用户加入时间
        """
        return self._joined_at

    @classmethod
    def get_link(cls) -> str:
        return cls._link

    @classmethod
    def resolve(cls, bot: ABCBot, data: dict) -> ABCMember:
        return Member(
            bot=bot,
            uid=data['basic']['uid'],
            name=data['basic']['name'],
            introduce=data['basic']['introduce'],
            avatar_url=data['basic']['avatar_url'],
            role_id_list=data['role_id_list'],
            joined_at=cls.resolve_time(data['joined_at'])
        )
