class ArgumentException(Exception):
    msg: str

    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self) -> str:
        return f'ArgumentException: {self.msg}'


class IllegalArgumentException(Exception):
    def __init__(self, msg):
        self.msg = msg


class IllegalCommandException(Exception):
    def __init__(self, msg):
        self.msg = msg
