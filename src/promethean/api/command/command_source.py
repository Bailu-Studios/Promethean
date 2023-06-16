from abc import ABC
from typing import TypeVar

S = TypeVar('S', bound='CommandSource')


class CommandSource(ABC):
    def get_name(self) -> str:
        """
        :return: 命令源名称
        """
        ...

    def send_msg(self, msg: str):
        """
        向命令源发送的消息
        :param msg: 向命令源发送的消息
        """
        ...

    def send_success(self, msg: str, log: bool = False):
        """
        向命令源发送成功消息
        :param msg: 向命令源发送的消息
        :param log: 是否日志记录
        """
        ...

    def send_failure(self, msg: str, log: bool = True):
        """
        向命令源发送失败消息
        :param msg: 向命令源发送的消息
        :param log: 是否日志记录
        """
        ...
