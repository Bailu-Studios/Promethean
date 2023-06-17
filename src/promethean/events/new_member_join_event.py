from promethean.api.event.event import Event


class NewMemberJoinEvent(Event):
    join_uid: int  # 用户 id
    join_user_nickname: int  # 用户昵称
    join_at: int  # 用户加入时间的时间戳
    villa_id: int  # 大别野 id

    def __init__(self, join_uid: int, join_user_nickname: int, join_at: int, villa_id: int):
        super().__init__()
        self._join_uid = join_uid
        self._join_user_nickname = join_user_nickname
        self._join_at = join_at
        self._villa_id = villa_id
