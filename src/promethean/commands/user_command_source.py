from promethean.api.command.command_source import CommandSource
from promethean.api.vila.abc_member import ABCMember
from promethean.api.vila.abc_message import ABCMessage
from promethean.log import logger


class UserCommandSource(CommandSource):
    _member: ABCMember
    _msg: ABCMessage

    def __init__(self, member: ABCMember, msg: ABCMessage):
        self._member = member
        self._msg = msg

    def get_name(self) -> str:
        return self._member.get_name()

    def send_msg(self, msg: ABCMessage):
        self._msg.reply(msg)

    def send_success(self, msg: ABCMessage, log: bool = False):
        self._msg.reply(msg)
        if log:
            logger.info(str(msg))

    def send_failure(self, msg: ABCMessage, log: bool = True):
        self._msg.reply(msg)
        if log:
            logger.warning(str(msg))
