def my_decorator(func):
    def action(n):
        func(n)
    return action

@my_decorator
def my_func1(n):
    arr = []
    for i in range(1, n):
        if i % 2 == 0:
            arr.append(i)
    print(arr)  

@my_decorator
def my_func2(n):
    arr = [n for n in range(1, n) if n % 2 == 0]
    print(arr)
   

my_func1(13)
my_func2(15)