import sqlite3
connect = sqlite3.connect('data.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task VARCHAR(128), 
    is_done INTEGER(1) DEFAULT 0 NOT NULL
)''')

def view_Tasks(connect, cursor):
    cursor.execute("SELECT id, task FROM tasks WHERE is_done = 0")
    tasks = cursor.fetchall()
    return tasks

def accept_task(connect, cursor, search):
    cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ? OR task = ?", [search, search])
    connect.commit()

action = input("""Добро пожаловать в \"Список дел\"
1 - вывести список дел
2 - добавить дело
3 - выполнить дело

0 - выйти из программы:\n""")
while action !="0":
    if action == "1":
        print("Список дел: ")
        for row in view_Tasks(connect, cursor):
            print(row[0], "-", row[1])      
              
    elif action == "2":
        task = input("Введите новое дело: ")
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", [task])
        connect.commit()
        print("Дело \"" + task + "\" добавлено!")
        
    elif action == "3":
        for row in view_Tasks(connect, cursor):
            print(row[0], "-", row[1])        
        search = input("Введите номер дела или его название: ")
        accept_task(connect, cursor, search)
        print("Дело ", search, " выполнено")
    else:
        print("Команда не найдена")
    action = input("""
1 - вывести список дел
2 - добавить дело
3 - выполнить дело

0 - выйти из программы:\n""")