from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_DECREASING_PER_BREATHE = 5

    def __init__(self, name: str):
        super().__init__(name, oxygen=70)

    def breathe(self):
        self.oxygen -= Biologist.OXYGEN_DECREASING_PER_BREATHE
