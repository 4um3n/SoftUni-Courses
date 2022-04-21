from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    DEFAULT_OXYGEN_LEVEL = 50

    def __init__(self, name: str) -> None:
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)

    def breathe(self) -> None:
        self.oxygen -= self.OXYGEN_DECREASING_PER_BREATHE
