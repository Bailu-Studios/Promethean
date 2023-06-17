from promethean.api.event.event import Event


class MemberAddQuickEmoticonEvent(Event):
    audit_id: int
    bot_tpl_id: str
    villa_id: int
    room_id: int
    user_id: int
    pass_through: str
    audit_result: int

    def __init__(self, audit_id: int, bot_tpl_id: str, villa_id: int, room_id: int, user_id: int, pass_through: str,
                 audit_result: int):
        super().__init__()
        self.audit_id = audit_id
        self.bot_tpl_id = bot_tpl_id
        self.villa_id = villa_id
        self.room_id = room_id
        self.user_id = user_id
        self.pass_through = pass_through
        self.audit_result = audit_result
