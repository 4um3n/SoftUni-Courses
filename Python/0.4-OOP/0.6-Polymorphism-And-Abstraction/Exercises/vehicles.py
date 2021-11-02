from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int) -> None:
        required_fuel = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int) -> None:
        required_fuel = distance * (self.fuel_consumption + 1.6)

        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * 0.95
