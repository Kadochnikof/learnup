import random
N = int(input("Введите кол-во столбцов: "))
M = int(input("Введите кол-во строк: "))
matrix = [[random.randrange(-11, 10) for i in range(N)] for j in range(M)]
print(matrix)
print([min(i) for i in matrix if matrix.index(i) % 2 == 1])
