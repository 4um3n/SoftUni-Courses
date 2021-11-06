class Appliance:
    def __init__(self, cost: float) -> None:
        self.cost = cost

    def get_monthly_expense(self) -> float:
        return self.cost * 30
