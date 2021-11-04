from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    DEFAULT_PORTION_GRAMS = 200

    def __init__(self, name: str, price: float):
        super().__init__(name=name, portion=Bread.DEFAULT_PORTION_GRAMS, price=price)
