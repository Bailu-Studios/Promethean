import logging

from promethean.api.command.command_source import CommandSource


class ConsoleCommandSource(CommandSource):
    def get_name(self) -> str:
        return 'Console'

    def send_msg(self, msg: str):
        logging.info(msg)

    def send_success(self, msg: str, log: bool = False):
        logging.info(msg)

    def send_failure(self, msg: str, log: bool = True):
        logging.warning(msg)
