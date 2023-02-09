import re
accounts = []
class User():
    
    def __init__(self, name, age: int, city) -> None:
        self.name = name
        self.age = age
        self.city = city

    def newUser(self, user):
        pattern = r'[_\da-zA-Z0-9]{1,20}'
        if bool(re.fullmatch(pattern, user)) == False:
            raise Exception("WrongUserException")
        elif user not in accounts:
            accounts.append(user)
            print(f'Пользователь {user} добавлен')
            self.user = user
        else:
            print(f'Выбран аккаунт {user}.')
            print("Имя: ", self.name, "\nВозраст: ", self.age, "\nГород: ", self.city)
            try:
                begin = int(input("""Что Вы хотите изменить: 
                1 - Имя аккаунта\n
                2 - Возраст аккаунту\n
                3 - Город аккаунта ?"""))
                if begin == 1:
                    self.setName(input("Введите новое имя: "))
                elif begin == 2:
                    self.setAge(int(input("Введите новый возраст: ")))
                elif begin == 3:
                    self.setCity(input("Введите новый город: "))
                else:
                    raise Exception("Введено неверное значение")
            except Exception as info:
                print(info)
                addUser()
       
    def setName(self, name):
        pattern = r'[\da-zA-Z]{1,20}'
        if bool(re.fullmatch(pattern, name)) == False:
            raise Exception("WrongNameException")
        else:
            self.name = name
            print(f'Имя пользователя {self.user} установлено на {user.name}')
            return name

    def setAge(self, age):
        if bool(age >= 1) == False:
            raise Exception("WrongAgeException")
            
        else:
            self.age = age
            print(f'Возраст пользователя {self.user} установлен на {user.age}')
            return age

    def setCity(self, city):
        pattern = r'[-\da-zA-Z]+'
        if bool(re.fullmatch(pattern, city)) == False:
            raise Exception("WrongCityException")
        else:
            self.city = city
            print(f'Город пользователя {self.user} установлен на {user.city}')
            return city


user = User("", 0, "")
Margaret = User('Margo', 67, "Monaco")
Maxim = User('Maxim', 25, "Kiev")
Nasty = User('Nastya', 44, "Paris")

def change():
    try:
        user.setName(input("Введите имя аккаунта: "))
        try:
            user.setAge(int(input("Введите возраст: ")))
            try:
                user.setCity(input("Введите город: "))
            except Exception as info:
                print(info)
                user.setCity(input("Введите город: "))
        except Exception as info:
            print(info)
            user.setAge(int(input("Введите возраст: ")))
    except Exception as info:
        print(info)
        user.setName(input("Введите имя аккаунта: "))

def addUser():
    try:
        begin = int(input("""Введите цифру 1, чтобы добавить или изменить пользователя \n 
        Цифру 2, чтобы посмотреть список уже добавленных пользователей """))
        if begin == 2:
            print(accounts)
            addUser()

        elif begin == 1:
            try:
                user.newUser(input("Введите имя аккаунта: "))
                change()
            except Exception as info:
                print(info)
                
        else:
            raise Exception("Введено неверное значение")
        addUser()
    except Exception as info:
        print(info) 
        addUser()

addUser()