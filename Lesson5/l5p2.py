class User():
    def __init__(self, name: str, surname: str, b_date: int, city: str, hobby: str) -> None:
        self.name = name
        self.surname = surname
        self.b_date = b_date
        self.city = city
        self.hobby = hobby
    def printinfo(self):
        print("Имя: ", self.name)
        print("Фамилия: ", self.surname)
        print("Возраст: ", 2022 - self.b_date)
        print("Город: ", self.city)
        print("Хобби: ", self.hobby)
user1 = User("Andrew", "Kadochnikov", 1990, "Saint-Petersburg", "music")
user2 = User("Ivan", "Ivanov", 2001, "Monaco", "swimming")

user1.printinfo()
user2.printinfo()