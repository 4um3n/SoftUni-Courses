from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    __ROOM_COST = 20
    __MEMBERS_COUNT = 2
    __ROOM_APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float) -> None:
        budget = salary_one + salary_two
        super().__init__(family_name, budget, self.__MEMBERS_COUNT)
        self.room_cost = self.__ROOM_COST
        self.appliances = self.__ROOM_APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances)
