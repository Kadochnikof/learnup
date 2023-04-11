"""Создаём класс прямоугольника и отдельно класс частного случая в виде квадрата
нарушая принцип Барбары Лисков"""


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        calcArea = self.side_a * self.side_b
        print("Площадь прямоугольника: ", calcArea, "см2")
        return calcArea


class Square(Rectangle):
    def __init__(self, side):
        self.side_a = side
        self.side_b = side


rect = Rectangle(4, 5)
rect.area()

sq = Square(5)
sq.area()
