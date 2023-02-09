import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    def perimeter(self):
        per = 2 * math.pi * self.radius
        print("Периметр Круга равен: ", per)
        return per
    
    def area(self):
        ar = self.radius * self.radius * math.pi
        print("Площадь Круга равна: ", ar)
        return ar      
    
