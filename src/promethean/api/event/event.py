from abc import ABC


class Event(ABC):
    is_cancelable: False
    is_canceled: False

    def is_cancelable(self):
        return self.is_cancelable

    def is_canceled(self):
        return self.is_cancelable

    def __init__(self):
        ...
