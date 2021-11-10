from project.software.software import Software


class LightSoftware(Software):
    DEFAULT_SOFTWARE_TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int) -> None:
        capacity_consumption = int(capacity_consumption + capacity_consumption * 0.50)
        super().__init__(name, self.DEFAULT_SOFTWARE_TYPE, capacity_consumption, memory_consumption // 2)
