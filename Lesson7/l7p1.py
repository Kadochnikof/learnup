import re
class User():
    def __init__(self) -> None:
        self.login = None

    def setLogin(self, login):
        pattern = r'\w{1,20}'
        if bool(re.fullmatch(pattern, login)) == False:
            raise Exception("WrongLoginException")
        else:
            self.login = login
            print("Логин введен корректно")
try:
    user = User()
    user.setLogin(input("Введите логин: "))
except Exception as info:
    print(info)


