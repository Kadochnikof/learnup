a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))

def nod(a, b):
    setA = set()
    setB = set()
    for i in range(1, a):
        if a % i == 0:
            setA.add(i)
    for i in range(1, b):
        if b % i == 0:
            setB.add(i)
    c = max(setA & setB)
    d = a * b / c
    print("Наибольший делитель чисел: ", c)
    print("Наименьшее кратное число: ", d)
    return c, d

nod(a, b)