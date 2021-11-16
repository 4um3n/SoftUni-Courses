from project.hardware.hardware import Hardware
from project.software.software import Software
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    __HARDWARE_CREATION_MAPPER = {
        "power": PowerHardware,
        "heavy": HeavyHardware,
    }

    __SOFTWARE_CREATION_MAPPER = {
        "express": ExpressSoftware,
        "light": LightSoftware,
    }

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int) -> None:
        power_hardware = System.__HARDWARE_CREATION_MAPPER['power'](name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int) -> None:
        power_hardware = System.__HARDWARE_CREATION_MAPPER['heavy'](name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_express_software(
            hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        express_software = System.__SOFTWARE_CREATION_MAPPER['express'](name, capacity_consumption, memory_consumption)
        return System._register_software(express_software, hardware_name)

    @staticmethod
    def register_light_software(
            hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        light_software = System.__SOFTWARE_CREATION_MAPPER['light'](name, capacity_consumption, memory_consumption)
        return System._register_software(light_software, hardware_name)

    @staticmethod
    def _register_software(software: Software, hardware_name: str):
        hardware = System._get_hardware_by_name(hardware_name)
        if hardware is None:
            return f"Hardware does not exist"

        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def _get_hardware_by_name(name: str) -> Hardware:
        for hardware in System._hardware:
            if hardware.name == name:
                return hardware

    @staticmethod
    def _get_software_by_name(name: str) -> Software:
        for software in System._software:
            if software.name == name:
                return software

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> str:
        hardware = System._get_hardware_by_name(hardware_name)
        software = System._get_software_by_name(software_name)
        if hardware is None or software is None:
            return f"Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze() -> str:
        info = [
            f"System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}"
        ]
        total_memory, total_capacity = 0, 0
        total_memory_consumption, total_taken_capacity = 0, 0
        for hardware in System._hardware:
            total_memory += hardware.memory
            total_capacity += hardware.capacity
            total_memory_consumption += hardware.taken_memory
            total_taken_capacity += hardware.taken_capacity

        info.append(f"Total Operational Memory: {total_memory_consumption} / {total_memory}")
        info.append(f"Total Capacity Taken: {total_taken_capacity} / {total_capacity}")
        return '\n'.join(info)

    @staticmethod
    def system_split() -> str:
        info = []
        for hardware in System._hardware:
            info.append(f"Hardware Component - {hardware.name}")
            info.append(repr(hardware))

        return '\n'.join(info)
