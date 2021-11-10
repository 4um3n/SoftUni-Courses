from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    DEFAULT_HARDWARE_TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int) -> None:
        memory = int(memory * 0.75)
        super().__init__(name, self.DEFAULT_HARDWARE_TYPE, capacity * 2, memory)
