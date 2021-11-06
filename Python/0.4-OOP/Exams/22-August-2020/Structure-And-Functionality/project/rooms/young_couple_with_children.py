from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    __DEFAULT_ROOM_MEMBERS_COUNT = 2
    __DEFAULT_ROOM_COST = 30
    __DEFAULT_APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children) -> None:
        room_members_count = YoungCoupleWithChildren.__DEFAULT_ROOM_MEMBERS_COUNT + len(children)
        super().__init__(family_name, salary_one + salary_two, room_members_count)
        self.room_cost = YoungCoupleWithChildren.__DEFAULT_ROOM_COST
        self.children.extend(children)
        self.appliances = YoungCoupleWithChildren.__DEFAULT_APPLIANCES * room_members_count
        self.calculate_expenses(self.appliances, self.children)
