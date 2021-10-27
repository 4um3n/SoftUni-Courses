class Circle:
    pi = 3.14

    def __init__(self, r):
        self.radius = r

    def set_radius(self, r):
        self.radius = r

    def get_area(self):
        return Circle.pi * self.radius ** 2

    def get_circumference(self):
        return Circle.pi * self.radius * 2


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())