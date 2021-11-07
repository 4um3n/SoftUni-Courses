from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    DEFAULT_PORTION_GRAMS = 245

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, self.DEFAULT_PORTION_GRAMS, price)
