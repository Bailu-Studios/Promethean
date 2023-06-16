from promethean.api.event.event import Event
from promethean.api.command.command_manager import CommandManager
from promethean.api.command.nodes.literal_command_node import LiteralCommandNode
from promethean.commands.console_command_source import ConsoleCommandSource
from promethean.commands.user_command_source import UserCommandSource


class CommandRegisterEvent(Event):
    _manager: CommandManager[UserCommandSource]

    def __init__(self, manager: CommandManager[UserCommandSource]):
        super().__init__()
        self._manager = manager

    def register(self, root: LiteralCommandNode):
        self._manager.register(root)

    def get_manager(self):
        return self._manager


class ConsoleCommandRegisterEvent(Event):
    _manager: CommandManager[ConsoleCommandSource]

    def __init__(self, manager: CommandManager[ConsoleCommandSource]):
        super().__init__()
        self._manager = manager

    def register(self, root: LiteralCommandNode[ConsoleCommandSource]):
        self._manager.register(root)

    def get_manager(self):
        return self._manager
