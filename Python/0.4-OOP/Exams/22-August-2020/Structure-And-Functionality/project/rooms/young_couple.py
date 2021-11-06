from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    __DEFAULT_ROOM_MEMBERS_COUNT = 2
    __DEFAULT_ROOM_COST = 20
    __DEFAULT_APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float) -> None:
        super().__init__(family_name, salary_one + salary_two, YoungCouple.__DEFAULT_ROOM_MEMBERS_COUNT)
        self.room_cost = YoungCouple.__DEFAULT_ROOM_COST
        self.appliances = YoungCouple.__DEFAULT_APPLIANCES * 2
        self.calculate_expenses(self.appliances)
