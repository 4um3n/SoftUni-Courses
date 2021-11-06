from project.rooms.room import Room


class AloneOld(Room):
    __DEFAULT_ROOM_COST = 10
    __DEFAULT_ROOM_MEMBERS_COUNT: int = 1

    def __init__(self, family_name: str, pension: float) -> None:
        super().__init__(family_name, pension, AloneOld.__DEFAULT_ROOM_MEMBERS_COUNT)
        self.room_cost = self.__DEFAULT_ROOM_COST

