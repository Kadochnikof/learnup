# Задание 2. Модифицируйте программу “Список продуктов” из начальных уроков нашего курса. 
# Реализуйте подключение к БД и таблицу с продуктами, сохраняйте и получайте данные с помощью sqlite3.

import sqlite3
connect = sqlite3.connect('SpisokProduktov.db')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS lists (
    product VARCHAR(64)   
)''')

def view_lists(connect, cursor):
    cursor.execute("SELECT product FROM lists")
    tasks = cursor.fetchall()
    return tasks

def add_product(connect, cursor):
    product = input("Введите название продукта: ")
    cursor.execute("INSERT INTO lists (product) VALUES (?)", [product])
    connect.commit()

action = input("""Добро пожаловать в \"Список продуктов\"
1 - вывести список продуктов
2 - добавить продукт
3 - Очистить список продуктов

0 - выйти из программы:\n""")
while action !="0":
    if action == "1":
        print("Список продуктов: ")
        for row in view_lists(connect, cursor):
            print(row[0])      
              
    elif action == "2":
        product = input("Введите новый продукт: ")
        cursor.execute("INSERT INTO lists (product) VALUES (?)", [product])
        connect.commit()
        print("Продукт \"" + product + "\" добавлен!")
    elif action == "3":
        cursor.execute("DELETE FROM lists")
        connect.commit()
        print("Список очищен")
    else:
        print("Команда не найдена")
    action = input("""
1 - вывести список продуктов
2 - добавить продукт
3 - Очистить список продуктов

0 - выйти из программы:\n""")
    
    

