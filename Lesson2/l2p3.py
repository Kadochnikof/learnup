purchases = []
purchase = input("Введите наименование покупки (завершить - 'стоп'): ")
while purchase != "стоп":
    purchases.append(purchase)
    purchase = input("Введите наименование покупки (завершить - 'стоп': ")
print("Список товаров: ")
i = 0
while i < len(purchases):
    print(purchases[i])
    i += 1