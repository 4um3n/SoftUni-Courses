class Room:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people_count):
        if self.is_taken or people_count > self.capacity:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests += people_count

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.is_taken = False
        people = self.guests
        self.guests = 0
        return people

