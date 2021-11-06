from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    __DEFAULT_ROOM_MEMBERS_COUNT = 2
    __DEFAULT_ROOM_COST = 15
    __DEFAULT_APPLIANCES = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float) -> None:
        super().__init__(family_name, pension_one + pension_two, OldCouple.__DEFAULT_ROOM_MEMBERS_COUNT)
        self.room_cost = OldCouple.__DEFAULT_ROOM_COST
        self.appliances = OldCouple.__DEFAULT_APPLIANCES * 2
        self.calculate_expenses(self.appliances)
