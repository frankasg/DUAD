import math

class Circle:
    radius = 4

    def get_area(self):
        if self.radius < 0:
            raise ValueError("El radio no puede ser negativo")
        
        return math.pi * self.radius ** 2
    

circle = Circle()
area = circle.get_area()
print(f"El area del circulo es: {area:.2f}")