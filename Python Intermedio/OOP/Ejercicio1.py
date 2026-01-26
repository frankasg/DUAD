import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        if self.radius < 0:
            raise ValueError("El radio no puede ser negativo")
        
        return math.pi * self.radius ** 2
    

circle = Circle(4)
area = circle.get_area()
print(f"El area del circulo es: {area:.2f}")