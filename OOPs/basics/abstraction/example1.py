from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * ( self.width + self.height)

rec = Rectangle(21,22)

print(f"Area of Rect: {rec.area()}")
print(f"Perim of Rect: {rec.perimeter()}")
print(Rectangle.mro())