from abc import ABC, abstractmethod
from enum import Enum


class RoleType(Enum):
    ALL_MEMBER = 'MEMBER_ROLE_TYPE_ALL_MEMBER'  # 所有人身份组
    ADMIN = 'MEMBER_ROLE_TYPE_ADMIN'  # 管理员身份组
    OWNER = 'MEMBER_ROLE_TYPE_OWNER'  # 大别野房主身份组
    CUSTOM = 'MEMBER_ROLE_TYPE_CUSTOM'  # 其他自定义身份组
    UNKNOWN = 'MEMBER_ROLE_TYPE_UNKNOWN'  # 未知

    @classmethod
    def resolve(cls, data: str) -> 'RoleType':
        for i in RoleType:
            if i.value == data:
                return i
        return RoleType.UNKNOWN


class Permission(Enum):
    MENTION_ALL = 'mention_all'  # 允许成员能够 @全体成员
    RECALL_MESSAGE = 'recall_message'  # 允许成员能够在聊天房间中撤回任何人的消息
    PIN_MESSAGE = 'pin_message'  # 允许成员能够在聊天房间中置顶消息
    MANAGE_MEMBER_ROLE = 'manage_member_role'  # 允许成员添加、删除身份组，管理身份组成员，修改身份组的权限
    EDIT_VILLA_INFO = 'edit_villa_info'  # 允许成员编辑大别野的简介、标签、设置大别野加入条件等
    MANAGE_GROUP_AND_ROOM = 'manage_group_and_room'  # 允许成员新建房间，新建/删除房间分组，调整房间及房间分组的排序
    VILLA_SILENCE = 'villa_silence'  # 允许成员能够在房间里禁言其他人
    BLACK_OUT = 'black_out'  # 允许成员能够拉黑和将其他人移出大别野
    HANDLE_APPLY = 'handle_apply'  # 允许成员审核大别野的加入申请
    MANAGE_CHAT_ROOM = 'manage_chat_room'  # 允许成员编辑房间信息及设置可见、发言权限
    VIEW_DATA_BOARD = 'view_data_board'  # 允许成员查看大别野数据看板
    MANAGE_CUSTOM_EVENT = 'manage_custom_event'  # 允许成员创建活动，编辑活动信息
    LIVE_ROOM_ORDER = 'live_room_order'  # 允许成员在直播房间中点播节目及控制节目播放
    MANAGE_SPOTLIGHT_COLLECTION = 'manage_spotlight_collection'  # 允许成员设置、移除精选消息

    @classmethod
    def resolve(cls, data: list[dict]) -> list['Permission']:
        out = []
        perms = []
        for perm in data:
            perms.append(perm['key'])
        for i in Permission:
            if i.value in perms:
                out.append(i)
        return out


class ABCRole(ABC):
    @abstractmethod
    def get_id(self) -> int:
        """
        :return: 身份组 id
        """

    @abstractmethod
    def get_name(self) -> str:
        """
        :return: 身份组名称
        """

    @abstractmethod
    def get_villa_id(self) -> int:
        """
        :return: 大别野 id
        """

    @abstractmethod
    def get_color(self) -> str:
        """
        :return: 身份组颜色，可选项见颜色
        """

    @abstractmethod
    def get_permissions(self) -> list[Permission]:
        """
        :return: 权限列表，可选项见权限
        """

    @abstractmethod
    def get_role_type(self) -> RoleType:
        """
        :return: 身份组类型
        """
