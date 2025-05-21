from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2  

    def perimeter(self):
        return 2 * math.pi * self.radius
        
class Rectangle(Shape):

    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return self.height * self.base

    def perimeter(self):
        return 2 * (self.height + self.base)
    


circle1 = Circle(2)
circle2 = Circle(124)

print(circle1.area())
print(circle1.perimeter())
print()
print(circle2.area())
print(circle2.perimeter())
print()

rectangle1 = Rectangle(12,32)
rectangle2 = Rectangle(2, 9)

print(rectangle1.area())
print(rectangle1.perimeter())
print()
print(rectangle2.area())
print(rectangle2.perimeter())