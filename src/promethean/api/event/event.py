from abc import ABC


class Event(ABC):
    _is_cancelable: bool
    _is_canceled: bool

    def __init__(self, is_cancelable: bool = False, is_canceled: bool = False):
        self._is_cancelable = is_cancelable
        self._is_canceled = is_canceled

    def is_cancelable(self):
        """
        :return: 该事件是否可取消
        """
        return self._is_cancelable

    def is_canceled(self):
        """
        :return: 该事件是否被取消
        """
        return self._is_canceled

    def cancel(self):
        """
        取消该事件
        """
        if self._is_cancelable:
            self._is_canceled = True
