from typing import Callable, Coroutine, Any

from promethean.api.command.command_source import S
from promethean.api.command.command_context import CommandContext

Command = Callable[[CommandContext[S]], Coroutine[Any, Any, Any]]
