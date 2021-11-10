from project.software.software import Software


class ExpressSoftware(Software):
    DEFAULT_SOFTWARE_TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int) -> None:
        super().__init__(name, self.DEFAULT_SOFTWARE_TYPE, capacity_consumption, memory_consumption * 2)
