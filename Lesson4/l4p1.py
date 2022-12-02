#arr = ["перец", "лежебока", "трансильвания", "потому", "сайдкик"]
arr = input("Введите несколько слов для создания списка:").split( )

def cutString():
    newArr = []
    for i in arr:
        if len(i) > 7:
            a = str(i[0:7]) + "..."
            newArr.append(a)
        else:
            newArr.append(i)
    print(newArr)
cutString()