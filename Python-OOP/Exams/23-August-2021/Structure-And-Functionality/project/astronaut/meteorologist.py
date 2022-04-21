from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_DECREASING_PER_BREATHE = 15
    DEFAULT_OXYGEN_LEVEL = 90

    def __init__(self, name: str) -> None:
        super().__init__(name, self.DEFAULT_OXYGEN_LEVEL)

    def breathe(self) -> None:
        self.oxygen -= self.OXYGEN_DECREASING_PER_BREATHE
