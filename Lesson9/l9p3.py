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

cursor.execute("SELECT login FROM users")
users = cursor.fetchall()
print(users)