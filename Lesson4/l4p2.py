def defA(x):
    if x <= 3:
        f1 = x**2 - 3 * x + 9
    else:
        f1 = 1 / (x**3 + 6)
    print(f1)
    return f1

def defB(x):
    if x <= 2:
        f2 = x**2 - 4 * x + 5
    else:
        f2 = 1 / (x**2 - 4 * x + 5)
    print(f2)
    return f2

def defC(x):
    if x > 3:
        f3 =  - 3 * x + 9
    else:
        f3 = x**3 / (x**2 + 8)
    print(f3)
    return f3

defA(2)
defA(4)
defB(2)
defB(4)
defC(2)
defC(4)