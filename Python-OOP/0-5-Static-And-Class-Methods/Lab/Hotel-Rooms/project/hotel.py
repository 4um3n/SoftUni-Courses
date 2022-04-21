from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people_count: int):
        for room in self.rooms:
            if room.number == room_number:
                is_taken = room.take_room(people_count)
                if is_taken is None:
                    self.guests += people_count

                return is_taken

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                info = room.free_room()
                if isinstance(info, int):
                    self.guests -= info
                    return

                return info

    def status(self):
        info = [f"Hotel {self.name} has {self.guests} total guests"]
        free_rooms, taken_rooms = [], []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms.append(str(room.number))
            else:
                free_rooms.append(str(room.number))

        info.append(f"Free rooms: {', '.join(free_rooms)}")
        info.append(f"Taken rooms: {', '.join(taken_rooms)}")
        return '\n'.join(info)
