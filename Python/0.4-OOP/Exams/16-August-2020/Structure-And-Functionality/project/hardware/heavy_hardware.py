from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        capacity *= 2
        memory = memory * 0.75
        super().__init__(name, "Heavy", capacity, int(memory))
