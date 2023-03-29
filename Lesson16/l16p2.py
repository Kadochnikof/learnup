#Напишите класс-итератор, объекты которого генерируют случайные числа 
# в количестве и в диапазоне, которые передаются в конструктор.
from random import randrange
class SimpleIterator:
    def __init__(self, limit, range):
        self.limit = limit
        self.range = range
        self.counter = 0
        
    def __next__(self):
        while self.counter < self.limit:
            self.counter += 1
            nums = randrange(self.range)
            return "Случайное число: " + str(nums)
        else:
            return "Лимит исчерпан"
        
iterator = SimpleIterator(5, 10)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
