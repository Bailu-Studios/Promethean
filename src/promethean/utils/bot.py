import asyncio

from command_dispatcher.command_manager import CommandManager
from promethean.api.vila.abc_bot import ABCBot
from promethean.api.vila.abc_group import ABCGroup
from promethean.api.vila.abc_member import ABCMember
from promethean.api.vila.abc_message import ABCMessage
from promethean.api.vila.abc_role import ABCRole
from promethean.api.vila.abc_room import ABCRoom
from promethean.api.vila.abc_villa import ABCVilla
from promethean.commands.console_command_source import ConsoleCommandSource
from promethean.commands.user_command_source import UserCommandSource
from promethean.constants import VILA_API_URL
from promethean.events.handle_event import handle_event
from promethean.events.command_register_event import CommandRegisterEvent, ConsoleCommandRegisterEvent
from promethean.events.member_send_message_event import MemberSendMessageEvent
from promethean.log import log_patcher, logger
from promethean.requests.http_client import HTTPClient
from promethean.requests.http_server import HTTPServer
from promethean.utils.group import Group
from promethean.utils.member import Member
from promethean.utils.role import Role
from promethean.utils.room import Room
from promethean.utils.villa import Villa


class Bot(ABCBot):
    _console_commands: CommandManager[ConsoleCommandSource] = CommandManager[ConsoleCommandSource]()
    _commands: CommandManager[UserCommandSource] = CommandManager[UserCommandSource]()
    _http_client: HTTPClient
    _http_server: HTTPServer
    _headers: dict
    _bot_id: str
    _bot_uid: int
    _bot_secret: str
    _callback_url: str
    _command_prefix: str
    _running: bool

    def __init__(self, bot_id: str, bot_secret: str, callback_url: str, command_prefix='/'):
        super().__init__()
        self._bot_id = bot_id
        self._bot_secret = bot_secret
        self._callback_url = callback_url
        self._command_prefix = command_prefix
        self._console_commands = CommandManager[ConsoleCommandSource](self._command_prefix)
        self._register_console_commands()
        self._commands = CommandManager[UserCommandSource](self._command_prefix)
        self._register_commands()
        self._register_event_handlers()
        self._headers = {
            'x-rpc-bot_id': self._bot_id,
            'x-rpc-bot_secret': self._bot_secret
        }
        self._http_client = HTTPClient(base_url=VILA_API_URL, headers=self._headers)
        # asyncio.run(self._check_access())
        self._running = False

    def run(self, host='127.0.0.1', port='23333', log_level='INFO'):
        logger.configure(extra={"promethean_log_level": log_level}, patcher=log_patcher)
        logger.success("Starting Promethean...")
        self._http_server = HTTPServer(host, port)
        self._http_server.app.post(self._callback_url, status_code=200)(lambda data: handle_event(self, data))
        self._running = True
        while self._running:
            continue

    def close(self):
        logger.success("Stopping Promethean...")
        self._http_client.session.close()
        self._running = False

    async def get_villa(self, villa_id: int = None) -> ABCVilla:
        """
        :return: 别野
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.get(Villa.get_link(), headers=self._headers) as context:
            return Villa.resolve(self, await context['villa'])

    async def get_member(self, member_id: int, villa_id: int = None) -> ABCMember:
        """
        :param villa_id: 别野 ID
        :param member_id: 用户 ID
        :return: 用户
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.get(Member.get_link(), {'uid': member_id}, headers=self._headers) as context:
            return Member.resolve(self, await context['member'])

    async def get_role(self, role_id: int, villa_id: int = None) -> ABCRole:
        """
        :param villa_id: 别野 ID
        :param role_id: 身份组 ID
        :return: 身份组
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.get(Role.get_link(), {'role_id': role_id}, headers=self._headers) as context:
            return Role.resolve(self, await context['role'])

    async def get_groups(self, villa_id: int = None) -> list[ABCGroup]:
        """
        :param villa_id: 别野 ID
        :return: 分组列表
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.get(Group.get_link(), headers=self._headers) as context:
            out = []
            for data in (await context['list']):
                data['villa_id'] = villa_id
                out.append(Group.resolve(self, data))
            return out

    async def get_room(self, room_id: int, villa_id: int = None) -> ABCRoom:
        """
        :param villa_id: 别野 ID
        :param room_id: 房间 ID
        :return: 房间
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.get(Room.get_link(), {'room_id': room_id}, headers=self._headers) as context:
            return Room.resolve(self, await context['room'])

    async def send_msg(self, room_id: int, msg: ABCMessage, villa_id: int = None) -> str:
        """
        :param villa_id: 别野 ID
        :param room_id: 房间 ID
        :param msg: 消息内容
        :return: 消息 ID
        """
        if villa_id is not None:
            self._headers['x-rpc-bot_villa_id'] = villa_id
        async with self._http_client.post('/vila/api/bot/platform/sendMessage', {
            'room_id': room_id,
            'object_name': msg.get_type(),
            'msg_content': await msg.serialize()
        }, headers=self._headers) as context:
            return await context['bot_msg_id']

    def get_bot_uid(self):
        return self._bot_uid

    async def _check_access(self):
        async with self._http_client.post('/vila/api/bot/platform/checkMemberBotAccessToken') as context:
            data = await context
            self._bot_uid = data['member']['basic']['uid']

    def _register_commands(self):
        asyncio.run(self._events.post(CommandRegisterEvent(self._commands)))

    def _register_console_commands(self):
        asyncio.run(self._events.post(ConsoleCommandRegisterEvent(self._console_commands)))

    def _register_event_handlers(self):
        @self.subscribe_event()
        async def on_member_send_message(event: MemberSendMessageEvent):
            text = str(event.msg)
            logger.info(text)
            if text.startswith(self._command_prefix):
                await self._commands.execute(text, UserCommandSource(event.msg.get_sender(), event.msg))
