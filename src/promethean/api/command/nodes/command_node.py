from typing import Generic, List, TypeVar
from promethean.api.command.command_source import S
from promethean.api.command.command import Command
from promethean.api.command.command_context import CommandContext
from promethean.api.command.exceptions import IllegalCommandException

T = TypeVar('T', bound='CommandNode')


class CommandNode(Generic[S, T]):
    _children: List['CommandNode[S]'] = []
    _executes: Command[S] = None

    def then(self, child: 'CommandNode[S]') -> T:
        self._children.append(child)
        return self

    def executes(self, command: Command[S]) -> T:
        self._executes = command
        return self

    async def execute(self, command: List[str], context: CommandContext[S]):
        flag: bool = True
        for node in self._children:
            if node.instanceof(command[0], context):
                flag = False
                sub_command = command[1:]
                if len(sub_command) == 0:
                    if node._executes is not None:
                        await node._executes(context)
                    else:
                        raise IllegalCommandException('Illegal or incomplete commands')
                else:
                    await node.execute(sub_command, context)
                break
        if flag:
            raise IllegalCommandException('Illegal or incomplete commands')

    def get_children(self) -> List['CommandNode[S]']:
        return self._children

    def instanceof(self, node: str, context: CommandContext[S]) -> bool:
        return False
