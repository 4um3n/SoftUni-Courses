from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, oxygen=50)

    def breathe(self):
        self.oxygen -= Astronaut.OXYGEN_DECREASING_PER_BREATHE
