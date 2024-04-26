from abc import  ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def permiter(self):
        pass

class Rectange(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

    def permiter(self):
        return 2*(self.width+self.height)
        pass


r=Rectange(3,4)
print(r.permiter())



