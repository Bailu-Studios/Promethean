from abc import ABC

from promethean.api.vila.abc_member import ABCMember


class ABCMessage(ABC):
    async def reply(self):
        """
        :return: 回复消息
        """

    async def get_sender(self) -> ABCMember:
        """
        :return: 消息发送者
        """


class ABCTextMessage(ABCMessage):
    async def get_text(self) -> str:
        """
        :return: 消息文本
        """


class ABCImageMessage(ABCMessage):
    async def get_url(self) -> str:
        """
        :return: 图片链接
        """
