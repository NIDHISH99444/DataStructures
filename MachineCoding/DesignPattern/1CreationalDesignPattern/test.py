from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Adding a new shape doesn't modify existing classes
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def print_area(shape: Shape):
    print("The area is:", shape.area())

# Each derived class can be used in place of Shape
rectangle = Rectangle(2, 3)
circle = Circle(5)
triangle = Triangle(4, 5)

print_area(rectangle)
print_area(circle)
print_area(triangle)