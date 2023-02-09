import math
class Square():
    def __init__(self, a, b):
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
