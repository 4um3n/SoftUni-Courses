class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: float):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption
