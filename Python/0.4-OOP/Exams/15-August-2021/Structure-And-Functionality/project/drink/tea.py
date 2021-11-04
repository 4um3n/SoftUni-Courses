from project.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name=name, portion=portion, price=Tea.PRICE, brand=brand)
