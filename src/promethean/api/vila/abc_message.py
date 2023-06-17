from abc import ABC, abstractmethod

from promethean.api.vila.abc_member import ABCMember


class ABCMessage(ABC):
    @abstractmethod
    def get_id(self) -> str:
        """
        :return: 消息 ID
        """

    @abstractmethod
    def get_room_id(self) -> int:
        """
        :return: 房间 ID
        """

    @abstractmethod
    def get_villa_id(self) -> int:
        """
        :return: 别野 ID
        """

    @abstractmethod
    def get_send_time(self) -> int:
        """
        :return: 消息发送时间
        """

    @abstractmethod
    async def reply(self, msg: 'ABCMessage'):
        """
        回复消息
        """

    @abstractmethod
    async def get_sender(self) -> ABCMember:
        """
        :return: 消息发送者
        """

    @abstractmethod
    async def serialize(self) -> dict:
        """
        :return: 序列化的消息
        """

    def get_quote(self) -> 'ABCMessage':
        """
        :return: 引用的消息
        """

    def set_quote(self, msg: 'ABCMessage'):
        """
        引用消息
        """

    @classmethod
    @abstractmethod
    def get_type(cls) -> str:
        """
        :return: 消息类型
        """


class ABCTextMessage(ABC):
    @abstractmethod
    def get_text(self) -> str:
        """
        :return: 消息文本
        """


class ABCImageMessage(ABC):
    @abstractmethod
    def get_url(self) -> str:
        """
        :return: 图片链接
        """
