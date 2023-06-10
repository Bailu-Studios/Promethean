from typing import Generic, TypeVar

T = TypeVar('T')


class ArgumentType(Generic[T]):
    def parse(self, reader: str) -> T:
        ...
