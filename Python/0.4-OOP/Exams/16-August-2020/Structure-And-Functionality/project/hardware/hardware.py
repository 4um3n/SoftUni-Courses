from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int) -> None:
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.taken_memory = 0
        self.taken_capacity = 0
        self.software_components = []

    def install(self, software: Software):
        if self.taken_capacity + software.capacity_consumption > self.capacity or \
                self.taken_memory + software.memory_consumption > self.memory:
            raise Exception(f"Software cannot be installed")

        self.taken_capacity += software.capacity_consumption
        self.taken_memory += software.memory_consumption
        self.software_components.append(software)

    def uninstall(self, software: Software) -> None:
        if software in self.software_components:
            self.software_components.remove(software)

    def __repr__(self) -> str:
        software_types, used_memory, used_capacity, software_names = [], [], [], []
        for software in self.software_components:
            software_types.append(software.software_type)
            used_memory.append(software.memory_consumption)
            used_capacity.append(software.capacity_consumption)
            software_names.append(software.name)

        software_names = 'None' if not software_names else ', '.join(software_names)
        info = [
            f"Express Software Components: {software_types.count('Express')}",
            f"Light Software Components: {software_types.count('Light')}",
            f"Memory Usage: {sum(used_memory)} / {self.memory}",
            f"Capacity Usage: {sum(used_capacity)} / {self.capacity}",
            f"Type: {self.hardware_type}",
            f"Software Components: {software_names}",
        ]

        return '\n'.join(info)
