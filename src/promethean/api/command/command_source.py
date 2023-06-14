from abc import ABC
from typing import TypeVar

S = TypeVar('S', bound='CommandSource')


class CommandSource(ABC):
    def get_name(self) -> str:
        ...

    def send_msg(self, msg: str):
        ...

    def send_success(self, msg: str, log: bool = False):
        ...

    def send_failure(self, msg: str, log: bool = True):
        ...
