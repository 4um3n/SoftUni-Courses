from project.drink.drink import Drink


class Water(Drink):
    PRICE = 1.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name=name, portion=portion, price=Water.PRICE, brand=brand)
