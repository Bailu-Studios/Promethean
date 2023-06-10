from promethean.api.command.arguments.argument_type import ArgumentType


class StringArgumentType(ArgumentType[str]):
    def parse(self, reader: str) -> str:
        return reader
