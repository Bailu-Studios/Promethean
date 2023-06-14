from typing import Any, Generic

from promethean.api.command import CommandContext
from promethean.api.command.arguments import ArgumentType
from promethean.api.command.nodes.command_node import CommandNode
from promethean.api.command.nodes.argument_command_node import ArgumentCommandNode
from promethean.api.command.nodes.literal_command_node import LiteralCommandNode
from promethean.api.command.command import S


class CommandManager(Generic[S]):
    start: str
    root_node: CommandNode[S, CommandNode] = CommandNode()

    def __init__(self, start: str = '/'):
        self.start = start

    def register(self, root: LiteralCommandNode[S]):
        self.root_node.then(root)

    def argument(self, name: str, arg_type: ArgumentType[Any]) -> ArgumentCommandNode[S]:
        return ArgumentCommandNode(name, arg_type)

    def literal(self, literal: str) -> LiteralCommandNode[S]:
        return LiteralCommandNode(literal)

    async def execute(self, input_: str, source: S):
        parse: list[str] = input_.split(" ")
        if len(parse) > 0:
            parse[0] = parse[0].replace(self.start, '')
        await self.root_node.execute(parse, CommandContext(source))
