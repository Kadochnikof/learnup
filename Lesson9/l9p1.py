import sqlite3
connect = sqlite3.connect('dataTask1.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    login VARCHAR(64), 
    name VARCHAR(64), 
    surname VARCHAR(64), 
    phone VARCHAR(64), 
    email VARCHAR(64), 
    password VARCHAR(64)    
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
