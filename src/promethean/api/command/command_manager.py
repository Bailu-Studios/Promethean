from typing import Any, Generic

from promethean.api.command.command_context import CommandContext
from promethean.api.command.arguments.argument_type import ArgumentType
from promethean.api.command.nodes.command_node import CommandNode
from promethean.api.command.nodes.argument_command_node import ArgumentCommandNode
from promethean.api.command.nodes.literal_command_node import LiteralCommandNode
from promethean.api.command.command import S


class CommandManager(Generic[S]):
    command_prefix: str
    root_node: CommandNode[S, CommandNode] = CommandNode()

    def __init__(self, command_prefix: str = '/'):
        self.command_prefix = command_prefix

    def register(self, root: LiteralCommandNode[S]):
        """
        注册命令
        :param root: 命令根节点
        """
        self.root_node.then(root)

    @classmethod
    def argument(cls, name: str, arg_type: ArgumentType[Any]) -> ArgumentCommandNode[S]:
        """
        :param name: 参数名称
        :param arg_type: 参数类型
        :return: 参数节点
        """
        return ArgumentCommandNode(name, arg_type)

    @classmethod
    def literal(cls, literal: str) -> LiteralCommandNode[S]:
        """
        :param literal: 字面量
        :return: 字面量节点
        """
        return LiteralCommandNode(literal)

    async def execute(self, input_: str, source: S):
        """
        执行命令
        :param input_: 命令输入
        :param source: 命令源
        """
        parse: list[str] = input_.split(' ')
        if len(parse) > 0:
            parse[0] = parse[0].replace(self.command_prefix, '')
        await self.root_node.execute(parse, CommandContext(source))
