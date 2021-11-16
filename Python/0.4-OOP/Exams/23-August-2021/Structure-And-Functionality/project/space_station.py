from project.planet.planet import Planet
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    __ASTRONAUTS_CREATION_MAPPER = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }
    __DEFAULT_OXYGEN_INCREASING_VALUE = 10

    def __init__(self) -> None:
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def _get_mission_report(self, planet: Planet, mission_astronauts: list) -> str:
        participated_astronauts_count = 0
        for astronaut in mission_astronauts:
            participated_astronauts_count += 1
            while astronaut.oxygen - astronaut.OXYGEN_DECREASING_PER_BREATHE >= 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

            if not planet.items:
                self.successful_missions += 1
                self.planet_repository.remove(planet)
                return f"Planet: {planet.name} was explored. " \
                       f"{participated_astronauts_count} astronauts participated in collecting items."

        self.unsuccessful_missions += 1
        return f"Mission is not completed."

    def _get_astronauts_for_mission(self) -> list:
        suitable_astronauts = self.astronaut_repository.get_suitable_astronauts()
        if not suitable_astronauts:
            raise Exception(f"You need at least one astronaut to explore the planet!")

        if len(suitable_astronauts) > 5:
            return suitable_astronauts[:5]
        return suitable_astronauts

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type not in SpaceStation.__ASTRONAUTS_CREATION_MAPPER:
            raise Exception(f"Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        astronaut = SpaceStation.__ASTRONAUTS_CREATION_MAPPER[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend(items.split(', '))
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exists!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        self.astronaut_repository.recharge_astronauts_oxygen(self.__DEFAULT_OXYGEN_INCREASING_VALUE)

    def send_on_mission(self, planet_name: str) -> str:
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception(f"Invalid planet name!")

        mission_astronauts = self._get_astronauts_for_mission()
        return self._get_mission_report(planet, mission_astronauts)

    def report(self) -> str:
        return f"{self.successful_missions} successful missions!\n" \
               f"{self.unsuccessful_missions} missions were not completed!\n" \
               f"Astronauts' info:\n" \
               f"{repr(self.astronaut_repository)}"
