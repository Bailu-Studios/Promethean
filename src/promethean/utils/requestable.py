from datetime import datetime
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from promethean.api.vila.abc_bot import ABCBot

T = TypeVar('T')


class Requestable(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def get_link(cls) -> str:
        ...

    @classmethod
    @abstractmethod
    def resolve(cls, bot: ABCBot, data: dict) -> T:
        ...

    @classmethod
    def resolve_time(cls, data: int) -> datetime:
        return datetime.fromtimestamp(data)
