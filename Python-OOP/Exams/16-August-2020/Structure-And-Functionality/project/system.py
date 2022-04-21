from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    __hardware_mapper = {
        "Power": PowerHardware,
        "Heavy": HeavyHardware,
    }

    __software_mapper = {
        "Light": LightSoftware,
        "Express": ExpressSoftware,
    }

    _hardware: list = []
    _software: list = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = System.__hardware_mapper["Power"](name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = System.__hardware_mapper["Heavy"](name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._get_hardware_by_name(hardware_name)
        software = System.__software_mapper["Express"](name, capacity_consumption, memory_consumption)
        return System._register_software(hardware, software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._get_hardware_by_name(hardware_name)
        software = System.__software_mapper["Light"](name, capacity_consumption, memory_consumption)
        return System._register_software(hardware, software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System._get_hardware_by_name(hardware_name)
        software = System._get_software_by_name(software_name)
        if hardware is None or software is None:
            return f"Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        info = [
            f"System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
        ]
        total_memory, total_capacity = 0, 0
        total_memory_consumption, total_capacity_consumption = 0, 0

        for hardware in System._hardware:
            total_capacity += hardware.capacity
            total_memory += hardware.memory
            total_capacity_consumption += hardware.capacity - hardware.left_capacity
            total_memory_consumption += hardware.memory - hardware.left_memory

        info.extend([
            f"Total Operational Memory: {total_memory_consumption} / {total_memory}",
            f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"
        ])
        return '\n'.join(info)

    @staticmethod
    def system_split():
        return '\n'.join([str(hardware) for hardware in System._hardware])

    @staticmethod
    def _get_hardware_by_name(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def _get_software_by_name(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    @staticmethod
    def _register_software(hardware, software):
        if hardware is None:
            return f"Hardware does not exist"

        hardware.install(software)
        System._software.append(software)
