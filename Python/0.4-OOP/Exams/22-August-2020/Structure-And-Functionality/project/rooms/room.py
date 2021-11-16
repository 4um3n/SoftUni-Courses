from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    __DEFAULT_CHILDREN: list = []
    __DEFAULT_APPLIANCES: list = []
    __DEFAULT_EXPENSES: float = 0.0

    def __init__(self, name: str, budget: float, members_count: int) -> None:
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = Room.__DEFAULT_CHILDREN
        self.appliances = Room.__DEFAULT_APPLIANCES
        self.expenses = Room.__DEFAULT_EXPENSES

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(f"Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args) -> None:
        for list_data in args:
            for obj in list_data:
                self.expenses += obj.get_monthly_expense()

    def __repr__(self) -> str:
        info = [
            f"{self.family_name} with {self.members_count} members. ",
            f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$",
        ]

        for i, child in enumerate(self.children):
            info.append(f"--- Child {i + 1} monthly cost: {child.get_monthly_expense():.2f}$")

        appliance_monthly_expenses = sum([appliance.get_monthly_expense() for appliance in self.appliances])
        info.append(f"--- Appliances monthly cost: {appliance_monthly_expenses:.2f}$")
        return '\n'.join(info)
