from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_DECREASING_PER_BREATHE = 15

    def __init__(self, name: str):
        super().__init__(name, oxygen=90)

    def breathe(self):
        self.oxygen -= Meteorologist.OXYGEN_DECREASING_PER_BREATHE
