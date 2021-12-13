from project.race import Race
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Controller:
    __CARS_MAPPER = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def __init__(self) -> None:
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:
        if car_type in self.__CARS_MAPPER:
            if self._find_car_by_model(model) is not None:
                raise Exception(f"Car {model} is already created!")

            car = self.__CARS_MAPPER[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        if self._find_driver_by_name(driver_name) is not None:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        if self._find_race_by_name(race_name) is not None:
            raise Exception(f"Race {race_name} is already created!")
        
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        driver = self._find_driver_by_name(driver_name)
        car = self._get_car_by_type(car_type)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            message = f"Driver {driver_name} changed his car from {driver.car.model} to {car.model}."
            car.is_taken = True
            driver.car.is_taken = False
            driver.car = car
            return message

        car.is_taken = True
        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        race = self._find_race_by_name(race_name)
        driver = self._find_driver_by_name(driver_name)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if race.is_driver_in(driver):
            return f"Driver {driver_name} is already added in {race_name} race."

        race.add_driver(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str) -> str:
        race = self._find_race_by_name(race_name)
        
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if not race.can_start:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        return race.start()

    def _find_car_by_model(self, model: str):
        for car in self.cars:
            if car.model == model:
                return car

    def _find_driver_by_name(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def _find_race_by_name(self, name):
        for race in self.races:
            if race.name == name:
                return race

    def _get_car_by_type(self, car_type: str):
        for car in self.cars[::-1]:
            if car.car_type == car_type and not car.is_taken:
                return car
