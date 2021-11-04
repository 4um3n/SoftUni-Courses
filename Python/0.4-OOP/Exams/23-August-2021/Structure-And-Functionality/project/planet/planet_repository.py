class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        for planet in self.planets:
            if planet.name == name:
                return planet
