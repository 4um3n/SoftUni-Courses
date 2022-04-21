from person import Person
from employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return f"teaching..."
