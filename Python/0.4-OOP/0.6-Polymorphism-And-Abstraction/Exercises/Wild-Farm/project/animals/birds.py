from project.food import Food, Meat
from project.animals.animal import Bird


class Owl(Bird):
    WEIGHT_GAIN_PER_FOOD_PIECE = 0.25

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * Owl.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_GAIN_PER_FOOD_PIECE = 0.35

    def make_sound(self):
        return f"Cluck"

    def feed(self, food: Food):
        self.weight += food.quantity * Hen.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity
