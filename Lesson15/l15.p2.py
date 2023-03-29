from sqlite3 import *
# Через декоратор запишите информацию в базу данных.


class DBConnect():
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.conn = connect(self.db)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise


def my_decorator(func):
    def action():
        name, a = func()
        with DBConnect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        score INTEGER);
        """)
            cursor.execute(
                "INSERT INTO users (name, score) VALUES (?, ?)", [name, a])
            conn.commit()
    return action


@my_decorator
def quiz():
    name = input("Введите имя пользователя: ")
    a = 0
    print(f"{name}, добро пожаловать в Викторину!")
    theme = input("Выберите тему: Автомобили / Космос / Животные: ").lower()
    if theme == "автомобили":
        print("Выбрана тема Автомобили!")
        print("1-й вопрос: Что изображено на логотипе марки Peugeot?")
        print("1 - Тигр", "2 - Лев", "3 - Волк", sep="\n")
        quest1 = int(input())
        if quest1 == 2:
            a += 1
        print("2-й вопрос: Как называется марка машина, производимая в России?")
        print("1 - Porshe", "2 - Ferarri", "3 - lada", sep="\n")
        quest2 = int(input())
        if quest2 == 3:
            a += 1
        print("3-й вопрос: Какая марка машины производится компанией Илона Маска?")
        print("1 - Fiat", "2 - Tesla", "3 - lada", sep="\n")
        quest3 = int(input())
        if quest3 == 2:
            a += 1

    elif theme == "космос":
        print("Выбрана тема Космос!")
        print("1-й вопрос:Какая планета является первой по счету от Солнца")
        print("1 - Земля", "2 - Венера", "3 - Меркурий", sep="\n")
        quest1 = int(input())
        if quest1 == 3:
            a += 1
        print("2-й вопрос: У какой планеты есть кольца?")
        print("1 - Плутон", "2 - Уран", "3 - Сатурн", sep="\n")
        quest2 = int(input())
        if quest2 == 3:
            a += 1
        print("3-й вопрос: Как называется наша Галактика?")
        print("1 - Андромеда", "2 - Млечный путь", "3 - Лада", sep="\n")
        quest3 = int(input())
        if quest3 == 2:
            a += 1
    elif theme == "животные":
        print("Выбрана тема Животные!")
        print("1-й вопрос: К какому классу относится Человек")
        print("1 - Насекомые", "2 - Млекопитающие", "3 - Хордовые", sep="\n")
        quest1 = int(input())
        if quest1 == 2:
            a += 1
        print("2-й вопрос: Какое животное строит плотины?")
        print("1 - Бобр", "2 - Ласка", "3 - Утконос", sep="\n")
        quest2 = int(input())
        if quest2 == 1:
            a += 1
        print("3-й вопрос: Кто из этих животных по своему классу не является рыбой?")
        print("1 - Акула", "2 - Осетр", "3 - Дельфин", sep="\n")
        quest3 = int(input())
        if quest3 == 3:
            a += 1
    else:
        print("К сожалению, название категории введено неверно")
    print(f"{name}, Ваш счет: {a} из 3.")
    return name, a


quiz()
