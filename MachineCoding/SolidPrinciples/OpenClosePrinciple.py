from abc import  ABC,abstractmethod
from math import pi
class Shape:

    def __init__(self,shape_type):
        self._shape_type=shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        super().__init__("circle")
        self._radius=radius

    def calculate_area(self):
        return  (pi * self._radius**2)


class Rectangle(Shape):

    def __init__(self,width,height):
        super().__init__("rectange")
        self._width=width
        self._height=height

    def calculate_area(self):
        return  self._width*self._height



circle=Circle(5)
print(circle.calculate_area())
rectange=Rectangle(3,4)
print(rectange.calculate_area())

