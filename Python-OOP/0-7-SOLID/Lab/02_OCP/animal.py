from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return f"woof-woof"


class Cat(Animal):
    def make_sound(self):
        return f"meow"


class Chicken(Animal):
    def make_sound(self):
        return f"quack"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals_data = [Cat('cat'), Dog('dog')]
animal_sound(animals_data)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
