from typing import TypeVar

from promethean.api.command.nodes.command_node import CommandNode
from promethean.api.command.command_context import CommandContext
from promethean.api.command.arguments.argument_type import ArgumentType
from promethean.api.command.exceptions import ArgumentException
from promethean.api.command.command_source import S

T = TypeVar('T')


class ArgumentCommandNode(CommandNode[S, 'ArgumentCommandNode']):
    name: str
    arg_type: ArgumentType[T]

    def __init__(self, name: str, arg_type: ArgumentType[T]):
        self.name = name
        self.arg_type = arg_type

    def instanceof(self, node: str, context: CommandContext[S]) -> bool:
        try:
            arg = self.arg_type.parse(node)
            context.arguments[self.name] = arg
        except ArgumentException:
            return False
        return True
