import hashlib
from tkinter import *
import sqlite3
from tkinter import messagebox as mb

connect = sqlite3.connect('D:/LearnUp/Lesson10/dataTask1.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    login VARCHAR(64) NOT NULL UNIQUE, 
    password VARCHAR(64) NOT NULL
)''')

def password_sha256(user_password):
    salt = "learnup"
    password = bytes(user_password + salt, "utf-8")
    password_hash = hashlib.sha256(password)
    return password_hash.hexdigest()

def register():
    login = entLogin.get().strip()
    password = password_sha256(entPassword.get())
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)", [login, password])
    connect.commit()
    mb.showinfo("Регистрация", "Пользователь " + login + " успешно зарегистрирован")


def authWindow():
    
    def userAuth():
        login = entLoginAuth.get().strip()
        password = password_sha256(entPasswordAuth.get())
        cursor.execute("SELECT password FROM users WHERE login = ? AND password = ?", [login, password])
        info = cursor.fetchall()
        if len(info) > 0:
            mb.showinfo("Авторизация", "Добро пожаловать!")
        else:
            mb.showerror("Авторизация", "Неверный пароль")
          
    auth = Toplevel()
    auth.geometry("300x300")
    auth.title("Авторизация")
    auth.resizable(0, 0)

    lblMain = Label(auth, text = "Авторизация", font = "Calibri 20")
    lblMain.place(x = 20, y = 20)

    lblLogin = Label(auth, text = "Логин", font = "Calibri 12")
    lblLogin.place(x = 20, y = 100)

    entLoginAuth = Entry(auth, width = 14, font = "Calibri 12")
    entLoginAuth.place(x = 80, y = 100)

    lblPassword = Label(auth, text = "Пароль", font = "Calibri 12")
    lblPassword.place(x = 20, y = 160)

    entPasswordAuth = Entry(auth, width = 14, font = "Calibri 12")
    entPasswordAuth.place(x = 80, y = 160)

    btnAuth = Button(auth, text = "Войти", font = "Calibri 16", command = userAuth)
    btnAuth.place(x = 20, y = 250)

    
    
root = Tk()
root.geometry("300x300")
root.title("Регистрация")
root.resizable(0, 0)

lblMain = Label(text = "Регистрация", font = "Calibri 20")
lblMain.place(x = 20, y = 20)

lblLogin = Label(text = "Логин", font = "Calibri 12")
lblLogin.place(x = 20, y = 100)

entLogin = Entry(width = 14, font = "Calibri 12")
entLogin.place(x = 80, y = 100)

lblPassword = Label(text = "Пароль", font = "Calibri 12")
lblPassword.place(x = 20, y = 160)

entPassword = Entry(width = 14, font = "Calibri 12")
entPassword.place(x = 80, y = 160)

btnRegister = Button(text = "Зарегистрироваться", font = "Calibri 16", command = register)
btnRegister.place(x = 20, y = 200)

btnAuth = Button(text = "Войти", font = "Calibri 16", command=authWindow)
btnAuth.place(x = 20, y = 250)

root.mainloop()
