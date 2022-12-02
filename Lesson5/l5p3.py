class User():
    def __init__(self, name = " ", surname = "", b_date = 0, city = "", hobby = "") -> None:
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
    def setName(self, name: str):
        self.name = name
    def setSurname(self, surname: str):
        self.surname = surname
    def setYear(self, b_date: int):
        self.b_date = b_date    
    def setCity(self, city: str):
        self.city = city
    def setHobby(self, hobby: str):
        self.hobby = hobby
user1 = User("Andrew", "Kadochnikov", 1990, "Saint-Petersburg", "music")
user2 = User("Ivan", "Ivanov", 2001, "Monaco", "swimming")
user3 = User()
user3.setName("Makar")
user3.setSurname("Alpatov")
user3.setYear(1969)
user3.setCity("Bali")
user3.setHobby("Art")
user1.printinfo()
user2.printinfo()
user3.printinfo()