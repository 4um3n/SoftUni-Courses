class Race:
    def __init__(self, name: str) -> None:
        self.name = name
        self.drivers: list = []

    @property
    def can_start(self):
        return len(self.drivers) >= 3

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError(f"Name cannot be an empty string!")
        self.__name = value

    def is_driver_in(self, driver):
        return driver in self.drivers

    def add_driver(self, driver):
        self.drivers.append(driver)

    def start(self):
        winners = [driver for driver in sorted(self.drivers, key=lambda dr: -dr.car.speed_limit)][:3]
        info = []
        for winner in winners:
            winner.number_of_wins += 1
            info.append(f"Driver {winner.name} wins the {self.name} race with a speed of {winner.car.speed_limit}.")

        return '\n'.join(info)
