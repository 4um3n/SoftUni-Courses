from project.rooms.room import Room


class AloneOld(Room):
    __ROOM_COST = 10
    __MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float) -> None:
        super().__init__(family_name, pension, self.__MEMBERS_COUNT)
        self.room_cost = self.__ROOM_COST
