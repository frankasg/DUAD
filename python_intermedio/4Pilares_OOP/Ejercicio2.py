import math
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    radius : float

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    


class Rectangle(Shape):
    length : float
    width : float

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def calculate_area(self):
        return self.length * self.width

class Square(Shape):
    side : float

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2
    
circle = Circle(6)
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

rectangle = Rectangle(15, 20)
rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

square = Square(8)
square_area = square.calculate_area()
square_perimeter = square.calculate_perimeter()

print(f"El perímetro del círculo es: {circle_perimeter:.2f}")
print(f"El perímetro del rectángulo es: {rectangle_perimeter:.2f}")
print(f"El perímetro del cuadrado es: {square_perimeter:.2f}")

print(f"El area del círculo es: {circle_area:.2f}")
print(f"El area del rectángulo es: {rectangle_area:.2f}")
print(f"El area del cuadrado es: {square_area:.2f}")