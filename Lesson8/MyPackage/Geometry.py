from SecondPackage.Circle import *
from SecondPackage.Square import *

class geometry():
    def __init__(self) -> None:
        pass
    
    def geom():
            
        enter = int(input("Выберите фигуру: \nПрямоугольник - цифра 1, Круг - цифра 2: "))
        if enter == 1:
            enter2 = int(input("Вы выбрали Прямоугольник. \nЧто Вы хотите посчитать? Площадь - цифра 1, Периметр - цифра 2: "))
            if enter2 == 1:
                square1 = Square(int(input("Длина прямоугольника: ")), int(input("Ширина прямоугольника: "))) 
                square1.area()
            elif enter2 == 2:
                square1 = Square(int(input("Длина прямоугольника: ")), int(input("Ширина прямоугольника: "))) 
                square1.perimeter()
            else:
                print("Неверный ввод")
        elif enter == 2:
            enter2 = int(input("Вы выбрали Круг. \nЧто Вы хотите посчитать? Площадь - цифра 1, Периметр - цифра 2: "))
            if enter2 == 1:
                Circle1 = Circle(int(input("Радиус круга: "))) 
                Circle1.area()
            elif enter2 == 2:
                Circle1 = Circle(int(input("Радиус круга: "))) 
                Circle1.perimeter()

        else:
            print("Неверный ввод")

geometry.geom()