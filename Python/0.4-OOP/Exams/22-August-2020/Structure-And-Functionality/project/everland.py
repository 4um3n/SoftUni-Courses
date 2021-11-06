class Everland:
    def __init__(self) -> None:
        self.rooms = []

    def add_room(self, room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        monthly_consumption = sum([room.expenses + room.room_cost for room in self.rooms])
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def _check_room_payment_possibilities(self, room) -> str:
        if room.budget < room.expenses + room.room_cost:
            self.rooms.remove(room)
            return f"{room.family_name} does not have enough budget and must leave the hotel."
        else:
            room.budget -= room.expenses + room.room_cost
            return f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left."

    def pay(self) -> str:
        info = []
        for room in self.rooms:
            info.append(self._check_room_payment_possibilities(room))

        return '\n'.join(info)

    def status(self) -> str:
        info = [f"Total population: {sum([room.members_count for room in self.rooms])}"]
        [info.append(repr(room)) for room in self.rooms]
        return '\n'.join(info)
