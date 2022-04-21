from abc import ABC, abstractmethod


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int) -> None:
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f"Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        food_price = sum([f.price for f in self.food_orders])
        drinks_price = sum([d.price for d in self.drink_orders])
        return food_price + drinks_price

    def clear(self) -> None:
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self) -> str:
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {type(self).__name__}\n" \
                   f"Capacity: {self.capacity}"
