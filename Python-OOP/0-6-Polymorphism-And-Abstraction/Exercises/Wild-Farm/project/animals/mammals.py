from project.food import Food, Vegetable, Fruit, Meat
from project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_GAIN_PER_FOOD_PIECE = 0.10

    def make_sound(self):
        return f"Squeak"

    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        
        self.weight += food.quantity * Mouse.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_GAIN_PER_FOOD_PIECE = 0.40

    def make_sound(self):
        return f"Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * Dog.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_GAIN_PER_FOOD_PIECE = 0.30

    def make_sound(self):
        return f"Meow"
    
    def feed(self, food: Food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * Cat.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_GAIN_PER_FOOD_PIECE = 1

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += food.quantity * Tiger.WEIGHT_GAIN_PER_FOOD_PIECE
        self.food_eaten += food.quantity
