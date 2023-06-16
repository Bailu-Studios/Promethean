from promethean.api.command.command_manager import CommandManager
from promethean.api.vila.abc_bot import ABCBot
from promethean.commands.console_command_source import ConsoleCommandSource
from promethean.commands.user_command_source import UserCommandSource
from promethean.constants import VILA_API_URL
from promethean.events.command_register_event import CommandRegisterEvent, ConsoleCommandRegisterEvent
from promethean.requests.http_client import HTTPClient


class Bot(ABCBot):
    _console_commands: CommandManager[ConsoleCommandSource] = CommandManager[ConsoleCommandSource]()
    _commands: CommandManager[UserCommandSource] = CommandManager[UserCommandSource]()
    _http_client: HTTPClient
    _headers: dict

    def __init__(self, token: str):
        super().__init__(token)
        self._register_console_commands()
        self._register_commands()
        self._http_client = HTTPClient(VILA_API_URL)

    async def _login(self):
        async with self._http_client.post('/vila/api/bot/platform/checkMemberBotAccessToken') as context:
            access_info: dict = context['access_info']
            self._headers = {
                'x-rpc-bot_id': await access_info['bot_tpl_id'],
                'x-rpc-bot_secret': await access_info['member_access_token'],
                'x-rpc-bot_villa_id': await access_info['villa_id']
            }

    def _register_commands(self):
        self._events.post(CommandRegisterEvent(self._commands))

    def _register_console_commands(self):
        self._events.post(ConsoleCommandRegisterEvent(self._console_commands))
