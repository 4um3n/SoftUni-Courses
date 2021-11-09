class EntertainmentDevice:
    @staticmethod
    def connect_device_to_power_outlet(device):
        return f"Connected {device} to power outlet!"


class HDMIConnectorMixin(EntertainmentDevice):
    @staticmethod
    def connect_to_device_via_hdmi_cable(device):
        return f"Connected {device} via HDMI!"


class RCAConnectorMixin(EntertainmentDevice):
    @staticmethod
    def connect_to_device_via_rca_cable(device):
        return f"Connected {device} via RCA!"


class EthernetConnectorMixin(EntertainmentDevice):
    @staticmethod
    def connect_to_device_via_ethernet_cable(device):
        return f"Connected {device} to the Internet!"


class Television(RCAConnectorMixin, HDMIConnectorMixin):
    def connect_to_dvd(self, dvd_player):
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)

    def __str__(self):
        return f"Television"


class DVDPlayer(HDMIConnectorMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)

    def __str__(self):
        return f"DVD Player"


class GameConsole(EthernetConnectorMixin, HDMIConnectorMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        return self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)

    def __str__(self):
        return f"Game Console"


class Router(EthernetConnectorMixin):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)

    def __str__(self):
        return f"Router"


if __name__ == '__main__':
    tv = Television()
    dvd = DVDPlayer()
    game = GameConsole()
    router = Router()

    print(tv.connect_to_dvd(dvd))
    print(tv.connect_to_game_console(game))
