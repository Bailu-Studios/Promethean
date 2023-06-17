from promethean.api.command.command_source import CommandSource
from promethean.api.vila.abc_message import ABCMessage
from promethean.log import logger


class ConsoleCommandSource(CommandSource):
    def get_name(self) -> str:
        return 'Console'

    def send_msg(self, msg: ABCMessage):
        logger.info(str(msg))

    def send_success(self, msg: ABCMessage, log: bool = False):
        logger.info(str(msg))

    def send_failure(self, msg: ABCMessage, log: bool = True):
        logger.warning(str(msg))
