import logging

from promethean.api.command.command_source import CommandSource


class UserCommandSource(CommandSource):
    def get_name(self) -> str:
        ...

    def send_msg(self, msg: str):
        ...

    def send_success(self, msg: str, log: bool = False):
        ...
        if log:
            logging.info(msg)

    def send_failure(self, msg: str, log: bool = True):
        ...
        if log:
            logging.warning(msg)
