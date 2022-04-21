from abc import ABC, abstractmethod


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float) -> None:
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value == ' ':
            raise ValueError(f"Name cannot be empty string or white space!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(f"Price cannot be less than or equal to zero!")

        self.__price = value

    def __repr__(self) -> str:
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
