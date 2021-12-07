class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room) -> None:
        self.rooms.append(room)

    def get_monthly_consumptions(self) -> str:
        income = sum([room.total_cost for room in self.rooms])
        return f"Monthly consumption: {income:.2f}$."

    def pay(self) -> str:
        info = []
        for room in self.rooms:
            if room.can_pay():
                room.budget -= room.total_cost
                info.append(f"{room.family_name} paid {room.total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                info.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(info)

    def status(self):
        info = [repr(room) for room in self.rooms]
        info.insert(0, f"Total population: {self._get_total_population()}")
        return '\n'.join(info)

    def _get_total_population(self):
        return sum([room.members_count for room in self.rooms])
