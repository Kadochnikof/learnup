import math
class Rectangle():
    def __init__(self, name: str, a: int, b: int) -> None:
        self.name = name
        self.a = a
        self.b = b

    def perimeter(self):
        per = 2 * (self.a + self.b)
        print("Периметр прямоугольника равен: ", per)
        return per

    def area(self):
        ar = self.a * self.b  
        print("Площадь прямоугольника равна: ", ar)
        return ar  

class Triangle():
    def __init__(self, name: str, a: int, b: int, c: int) -> None:
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        per = self.a + self.b + self.c
        print("Периметр Треугольника равен: ", per)
        return per

    def area(self):
        p = (self.a + self.b + self.c) / 2
        ar = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        print("Площадь Треугольника равна: ", ar)
        return ar  

class Circle():
    def __init__(self, name: str, a: int) -> None:
        self.name = name
        self.a = a

    def perimeter(self):
        per = 2 * math.pi * self.a 
        print("Периметр Круга равен: ", per)
        return per

    def area(self):
        ar = self.a * self.a * math.pi
        print("Площадь Круга равна: ", ar)
        return ar  

figures = [Rectangle("Прямоугольник 1", 5, 6), Rectangle("Прямоугольник 2", 9, 9), 
Triangle("Треугольник 1", 2, 3, 4), Triangle("Треугольник 2", 5, 6, 7), 
Circle("Круг 1", 5)]

for figure in figures:
    print(figure.name)
    figure.perimeter()
    figure.area()