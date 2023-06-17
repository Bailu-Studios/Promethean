from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_role import ABCRole, Permission, RoleType
from promethean.utils.requestable import Requestable


class Role(ABCRole, Requestable[ABCRole]):
    _bot: ABCBot
    _role_id: int
    _name: str
    _villa_id: int
    _color: str
    _permissions: list[Permission]
    _role_type: RoleType
    _link = '/vila/api/bot/platform/getMemberRoleInfo'

    def __init__(self,
                 bot: ABCBot,
                 role_id: int,
                 name: str,
                 villa_id: int,
                 color: str,
                 permissions: list[Permission],
                 role_type: RoleType
                 ):
        self._bot = bot
        self._role_id = role_id
        self._name = name
        self._villa_id = villa_id
        self._color = color
        self._permissions = permissions
        self._role_type = role_type

    def get_id(self) -> int:
        """
        :return: 身份组 id
        """
        return self._role_id

    def get_name(self) -> str:
        """
        :return: 身份组名称
        """
        return self._name

    def get_villa_id(self) -> int:
        """
        :return: 大别野 id
        """
        return self._villa_id

    def get_color(self) -> str:
        """
        :return: 身份组颜色，可选项见颜色
        """
        return self._color

    def get_permissions(self) -> list[Permission]:
        """
        :return: 权限列表，可选项见权限
        """
        return self._permissions

    def get_role_type(self) -> RoleType:
        """
        :return: 身份组类型
        """
        return self._role_type

    @classmethod
    def get_link(cls) -> str:
        return cls._link

    @classmethod
    def resolve(cls, bot: ABCBot, data: dict) -> ABCRole:
        return Role(
            bot=bot,
            role_id=data['id'],
            name=data['name'],
            villa_id=data['villa_id'],
            color=data['color'],
            permissions=Permission.resolve(data['role_id_list']),
            role_type=RoleType.resolve(data['role_type']),
        )
