from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):
    __ROOM_COST = 10
    __MEMBERS_COUNT = 1
    __ROOM_APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float) -> None:
        super().__init__(family_name, salary, self.__MEMBERS_COUNT)
        self.room_cost = self.__ROOM_COST
        self.appliances = self.__ROOM_APPLIANCES
        self.calculate_expenses(self.appliances)
