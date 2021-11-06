from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    __DEFAULT_ROOM_COST: int = 10
    __DEFAULT_ROOM_MEMBERS_COUNT: int = 1
    __DEFAULT_APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float) -> None:
        super().__init__(family_name, salary, AloneYoung.__DEFAULT_ROOM_MEMBERS_COUNT)
        self.room_cost = self.__DEFAULT_ROOM_COST
        self.appliances = self.__DEFAULT_APPLIANCES
        self.calculate_expenses(self.appliances)
