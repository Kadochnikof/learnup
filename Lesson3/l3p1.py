a = int(input("Введите число 'a' от 1 до 10: "))
if a > 0 and a <= 10:
    b = int(input("Введите число 'b', от 'a' до 10: "))
    if b >= a and b <= 10:
        c = int(input("Введите число 'c' от 1 до 10: "))
        if c > 0 and c <= 10:
            d = int(input("Введите число 'd', от 'c' до 10: "))
        else:
            print("Неправильные вводные данные")
    else:
        print("Неправильные вводные данные")
else:
        print("Неправильные вводные данные")
        
for i in range(c, d + 1):
  print("\t", i, end = "")
for j in range(a, b + 1):
    print("\n", j, end = "")
    for k in range(c, d + 1):
        print("\t", j * k, end = "")