"""Создаём общий класс Фигуры и отдельно классы прямоугольника и квадрата
используя принцип Барбары Лисков"""

class Figures: 
    def area():
        pass


class Rectangle(Figures):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self):
        calcArea = self.side_a * self.side_b
        print("Площадь прямоугольника: ", calcArea, "см2")
        return calcArea


class Square(Figures):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        calcArea = self.side ** 2
        print("Площадь квадрата: ", calcArea, "см2")
        return calcArea


rect = Rectangle(4, 5)
rect.area()

sq = Square(5)
sq.area()
