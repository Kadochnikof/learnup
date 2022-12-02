class Car():
    def __init__(self, model: str, type: str, color: str, weight: int, max_speed: int) -> None:
        self.__model = model
        self.__type = type
        self.__color = color
        self.__weight = weight
        self.__max_speed = max_speed

    def setModel(self, model):
        self.__model = model
        print("Установлена модель: ", model)
        
    def getModel(self):
        print("Марка машины: ")
        return self.__model

    def setType(self, type):
        self.__type = type
        print("Установлен тип кузова: ", type)
        
    def getType(self):
        print("Тип кузова: ")
        return self.__type

    def setColor(self, color):
        self.__color = color
        print("Установлен цвет: ", color)
        
    def getColor(self):
        print("Цвет машины: ")
        return self.__color

    def setWeight(self, weight):
        self.__weight = weight
        print("Установлен вес машины: ", weight)
        
    def getWeight(self):
        print("Вес машины: ")
        return self.__weight

    def setMax_speed(self, max_speed):
        self.__max_speed = max_speed
        print("Установлена максимальная скорость: ", max_speed)
        
    def getMax_speed(self):
        print("Максимальная скорость: ")
        return self.__max_speed

car1 = Car("Приора", "Седан", "Красный", 1044, 160)
print(car1.getModel())
print(car1.getType())
print(car1.getColor())
print(car1.getWeight())
print(car1.getMax_speed())
car1.setModel("BMW")
car1.setType("Хэтчбек")
car1.setColor("Синий")
car1.setWeight("950")
car1.setMax_speed("300")
print(car1.getModel())
print(car1.getType())
print(car1.getColor())
print(car1.getWeight())
print(car1.getMax_speed())