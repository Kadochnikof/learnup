#Напишите выполняющую ту же задачу генераторную функцию. 
# В качестве аргументов она должна принимать количество элементов и диапазон.
from random import randrange
def my_generator(lim, range):
    while lim > 0:
        lim -= 1
        nums = randrange(range)
        yield "Случайное число: " + str(nums)

gen = my_generator(5, 10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
