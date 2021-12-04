from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: list = []

    @property
    def left_capacity(self):
        return self.capacity - sum(s.capacity_consumption for s in self.software_components)

    @property
    def left_memory(self):
        return self.memory - sum(s.memory_consumption for s in self.software_components)

    @property
    def installed_express_software_count(self):
        return len([s for s in self.software_components if s.software_type == "Express"])

    @property
    def installed_light_software_count(self):
        return len([s for s in self.software_components if s.software_type == "Light"])

    def __check_software_dependencies(self, software: Software):
        if self.left_capacity < software.capacity_consumption or self.left_memory < software.memory_consumption:
            raise Exception(f"Software cannot be installed")

    def install(self, software: Software):
        self.__check_software_dependencies(software)
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    def __str__(self):
        software_names = [s.name for s in self.software_components]
        software_components = ', '.join(software_names) if self.software_components else "None"
        info = [
            f"Hardware Component - {self.name}",
            f"Express Software Components: {self.installed_express_software_count}",
            f"Light Software Components: {self.installed_light_software_count}",
            f"Memory Usage: {self.memory - self.left_memory} / {self.memory}",
            f"Capacity Usage: {self.capacity - self.left_capacity} / {self.capacity}",
            f"Type: {self.hardware_type}",
            f"Software Components: {software_components}"
        ]

        return '\n'.join(info)

