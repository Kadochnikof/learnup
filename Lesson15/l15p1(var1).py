def my_decorator1(func):  
    def createList1(n):
        arr = []
        for i in range(1, n):
            if i % 2 == 0:
                arr.append(i)
        print(arr)
    return createList1
  
    
def my_decorator2(func):
    def createList2(n):
        func(n)
    return createList2

@my_decorator1
def my_func1(n):
    pass  

@my_decorator2
def my_func2(n):
    arr = [n for n in range(1, n) if n % 2 == 0]
    print(arr)
   

my_func1(13)
my_func2(15)