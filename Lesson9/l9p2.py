# Задание 2. Модифицируйте программу “Список продуктов” из начальных уроков нашего курса. 
# Реализуйте подключение к БД и таблицу с продуктами, сохраняйте и получайте данные с помощью sqlite3.

import sqlite3
connect = sqlite3.connect('SpisokProduktov.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS lists (
    product VARCHAR(64)   
)''')



cursor.execute("""INSERT INTO users VALUES 
               ("Uchenik", "Andrei", "Kad", "48349", "kad@kad.ru", "12345"),
               ("Uchitel", "Roman", "Swat", "12349", "learn@up.ru", "3241235"),
               ("Passashir", "Maria", "Girl", "89446", "Mari@au.rf", "24536fgh")
               """)
connect.commit()
        
cursor.execute("SELECT login, name, surname, phone, email FROM users")
users = cursor.fetchall()


cursor.execute("DELETE FROM users")
print(users)
