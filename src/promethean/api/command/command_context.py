from typing import Generic, Dict, Any, Type as Class, TypeVar

from promethean.api.command.command import S
from promethean.api.command.exceptions import IllegalArgumentException

T = TypeVar('T')


class CommandContext(Generic[S]):
    source: S
    arguments: Dict[str, Any] = {}

    def __init__(self, source: S):
        self.source = source

    def get_argument(self, name: str, clazz: Class[T]) -> T:
        """
        获取参数
        :param name: 参数名
        :param clazz: 参数类型
        :return:
        """
        argument: clazz = self.arguments.get(name)
        if argument is None:
            raise IllegalArgumentException(f'No such argument "{name}" exists on this command')
        return T(argument)
