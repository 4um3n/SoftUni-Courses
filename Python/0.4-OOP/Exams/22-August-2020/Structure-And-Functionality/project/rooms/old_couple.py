from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    __ROOM_COST = 15
    __MEMBERS_COUNT = 2
    __ROOM_APPLIANCES = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float) -> None:
        budget = pension_one + pension_two
        super().__init__(family_name, budget, self.__MEMBERS_COUNT)
        self.room_cost = self.__ROOM_COST
        self.appliances = self.__ROOM_APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances)
