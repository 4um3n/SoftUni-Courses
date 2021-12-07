class Room:
    __ROOM_COST = 0
    __CHILDREN = []
    __APPLIANCES = []

    def __init__(self, name: str, budget: float, members_count: int) -> None:
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.expenses = 0
        self.room_cost = self.__ROOM_COST
        self.children = self.__CHILDREN
        self.appliances = self.__APPLIANCES

    @property
    def total_cost(self):
        return self.expenses + self.room_cost

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError(f"Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *expenses_data):
        for expenses_list in expenses_data:
            for obj in expenses_list:
                self.expenses += obj.get_monthly_expense()

    def can_pay(self):
        return self.budget >= self.total_cost

    def __repr__(self):
        info = [
            f"{self.family_name} with {self.members_count} members. "
            f"Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$",
        ]

        for n, child in enumerate(self.children):
            info.append(f"--- Child {n + 1} monthly cost: {child.get_monthly_expense():.2f}$")

        appliances_cost = sum([appliance.get_monthly_expense() for appliance in self.appliances])
        info.append(f"--- Appliances monthly cost: {appliances_cost:.2f}$")
        return '\n'.join(info)
