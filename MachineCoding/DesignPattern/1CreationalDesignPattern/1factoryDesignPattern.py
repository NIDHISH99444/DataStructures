from abc import  ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("circle")

class Rectange(Shape):
    def draw(self):
        print("rectange")


class ShapeFactory:
    def create_shape(self,shape_type):
        if shape_type=='Circle':
            return Circle()
        elif shape_type=='Rectange':
            return  Rectange()


s=ShapeFactory()
circle=s.create_shape('Circle')
circle.draw()

