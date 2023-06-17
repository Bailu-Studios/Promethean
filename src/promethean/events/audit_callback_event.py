from promethean.api.event.event import Event


class AuditCallbackEvent(Event):
    villa_id: int
    room_id: int
    uid: int
    emoticon_id: int
    emoticon: str
    msg_uid: str
    bot_msg_id: str
    is_cancel: bool

    def __init__(self, villa_id: int, room_id: int, uid: int, emoticon_id: int, emoticon: str, msg_uid: str,
                 bot_msg_id: str, is_cancel: bool):
        super().__init__()
        self.villa_id = villa_id
        self.room_id = room_id
        self.uid = uid
        self.emoticon_id = emoticon_id
        self.emoticon = emoticon
        self.msg_uid = msg_uid
        self.bot_msg_id = bot_msg_id
        self.is_cancel = is_cancel
