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

    def recharge_astronauts_oxygen(self, value):
        for astronaut in self.astronauts:
            astronaut.increase_oxygen(value)

    def get_suitable_astronauts(self):
        return [ast for ast in sorted(self.astronauts, key=lambda a: -a.oxygen) if ast.oxygen > 30]

    def __repr__(self) -> str:
        return '\n'.join([repr(astronaut) for astronaut in self.astronauts])
