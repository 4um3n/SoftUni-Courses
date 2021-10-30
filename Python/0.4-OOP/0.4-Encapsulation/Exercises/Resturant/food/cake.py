from .dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str):
        price = Cake.PRICE
        calories = Cake.CALORIES
        grams = Cake.GRAMS
        super().__init__(name, price, grams, calories)
