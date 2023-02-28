# Задание 3. Используя знания об SQL и sqlite3, 
# создайте консольное приложение регистрации и авторизации пользователя в системе.
import sqlite3
connect = sqlite3.connect('dataTask3.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    login VARCHAR(64), 
    password VARCHAR(64)    
)''')
cursor.execute("DELETE FROM users")
cursor.execute("""INSERT INTO users VALUES 
               ("Uchenik", "123asd"),
               ("Uchitel", "qwerty!"),
               ("Girl", "dsa321")
               """)
connect.commit()

def view_users(connect, cursor):
    cursor.execute("SELECT login, password FROM users")
    users = cursor.fetchall()
    return users

def change_pass(connect, cursor, search):
    old_pass = input("Введите старый пароль: ")
    cursor.execute("SELECT login FROM users WHERE login = ? AND password = ?", [search, old_pass])
    users = cursor.fetchone()
    if users is None:
        print("Введен неверный пароль.")
        change_pass(connect, cursor, search)
    else:
        new_pass = input("Введите новый пароль: ")
        cursor.execute("UPDATE users SET password = ? WHERE login = ?", [new_pass, search])
        connect.commit()
        print("Пароль пользователя ", search, " изменен")

action = input("""Добро пожаловать в \"Систему авторизации пользователей\"
1 - вывести список пользователей
2 - добавить пользователя
3 - изменить пароль

0 - выйти из программы:\n""")

while action !="0":
    if action == "1":
        print("Список пользователей: ")
        for row in view_users(connect, cursor):
            print(row[0], " - ", row[1])      
              
    elif action == "2":
        login = input("Введите нового пользователя: ")
        cursor.execute("SELECT login FROM users where login = ?", [login])
        users = cursor.fetchone()
        # check = cursor.execute("SELECT login FROM users where login = ?", [login])
        if users is None:
            password = input("Введите пароль: ")
            cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", [login, password])
            connect.commit()
            print("Пользователь \"" + login + "\" добавлен!")
        else:
            print("Пользователь уже существует")
        
    elif action == "3":
        search = input("Введите Логин пользователя для изменения пароля: ")
        cursor.execute("SELECT login FROM users where login = ?", [search])
        users = cursor.fetchone()
        if users is None:
            print("Такого пользователя не существует")
        else:
            change_pass(connect, cursor, search)
        
    else:
        print("Команда не найдена")
    action = input("""
1 - вывести список пользователей
2 - добавить пользователя
3 - изменить пароль

0 - выйти из программы:\n""")