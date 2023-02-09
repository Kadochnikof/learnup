import re
class User():
    def __init__(self) -> None:
        self.password = None
        self.newPassword = None

    def setPassword(self, password):
        pattern = r'[_\da-zA-Z0-9]{1,20}'
        if bool(re.fullmatch(pattern, password)) == False:
            raise Exception("WrongPasswordException")
        else:
            self.password = password
            return password
        
    def confirmPassword(self, password):
        newPassword = self.password
        pattern = r'[_\da-zA-Z0-9]{1,20}'
        if bool(re.fullmatch(pattern, newPassword)) == False or newPassword != password:
            raise Exception("WrongPasswordException")
        else:
            print("Пароль введён успешно")           

try:
    user = User()
    user.setPassword(input("Введите пароль: "))
    user.confirmPassword(input("Подтвердите пароль: "))
except Exception as info:
    print(info)


