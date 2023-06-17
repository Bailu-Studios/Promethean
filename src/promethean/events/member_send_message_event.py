from promethean.api.event.event import Event
from promethean.utils.message import TextMessage


class MemberSendMessageEvent(Event):
    msg = TextMessage

    def __init__(self, msg: TextMessage):
        super().__init__()
        self._msg = msg
