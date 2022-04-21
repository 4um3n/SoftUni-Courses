class PizzaDelivery:
    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients.update({ingredient: 0})

        self.ingredients[ingredient] += quantity
        self.price += price_per_ingredient * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_ingredient):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        elif self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= price_per_ingredient * quantity

    def make_order(self):
        self.ordered = True
        ingredients = ', '.join([f'{k}: {v}' for k, v in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {ingredients} and the price will be {self.price}lv."

