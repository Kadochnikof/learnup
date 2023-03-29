class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        
    def __next__(self):
        while self.counter < self.limit:
            self.counter += 1
            return "Овец: " + str(self.counter)
        else:
            return "Овцы кончились"
        
iterator = SimpleIterator(5)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))



def my_generator(val):
    while val > 0:
        val -= 1
        yield val

gen = my_generator(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

nums = list(x**2 for x in range(100))
print(nums)