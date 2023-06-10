from typing import Generic, Dict, Any, Type as Class

from promethean.api.command.command import S
from promethean.api.command.exceptions import IllegalArgumentException


class CommandContext(Generic[S]):
    source: S
    arguments: Dict[str, Any] = {}

    def __init__(self, source: S):
        self.source = source

    def get_argument(self, name: str, clazz: Class[Any]) -> Any:
        argument: clazz = self.arguments.get(name)
        if argument is None:
            raise IllegalArgumentException(f'No such argument "{name}" exists on this command')
        return argument
