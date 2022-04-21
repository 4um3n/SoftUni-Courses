from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    __ROOM_COST = 30
    __MEMBERS_COUNT = 2
    __ROOM_APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: tuple) -> None:
        budget = salary_one + salary_two
        self.__MEMBERS_COUNT += len(children)
        super().__init__(family_name, budget, self.__MEMBERS_COUNT)
        self.children.extend(children)
        self.room_cost = self.__ROOM_COST
        self.appliances = self.__ROOM_APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances, self.children)
