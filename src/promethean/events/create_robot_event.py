from promethean.api.event.event import Event


class CreateRobotEvent(Event):
    villa_id: int

    def __init__(self, villa_id: int):
        super().__init__()
        self.villa_id = villa_id

    def get_villa_id(self) -> int:
        return self.villa_id
