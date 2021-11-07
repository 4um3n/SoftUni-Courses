from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self) -> None:
        self.astronauts = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut:
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
