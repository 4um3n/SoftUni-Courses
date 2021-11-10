from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    DEFAULT_HARDWARE_TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int) -> None:
        memory = int(memory + memory * 0.75)
        capacity = int(capacity * 0.25)
        super().__init__(name, self.DEFAULT_HARDWARE_TYPE, capacity, memory)
