import threading
import time
a = 1
counter = 1
def factorial(start, end):
    """Возводит число в факториал"""
    global counter
    global a
    for i in range(start, end + 1):
        counter *= i
    print(str(a)," поток =",counter)       # Для проверки работы функций, использовать с маленькими
    a += 1                                 # числами желательно до 50
    
  

    
def threading_factorial(n,number_of_threads):
    """функция делит число на количество потоков и возводит в факториал"""
    threads = []
    f = n // number_of_threads
    a = f
    w = 1
    v = 0 
    for i in range(1,n + 1):
        if n % number_of_threads == 0:
            if i == f:
                t = threading.Thread(target = factorial,args = (w, f))
                threads.append(t)
                t.start()
                w = f +1
                f += a
            else:
                continue
        else:
            if  n % number_of_threads != 0:
                if  i == f:
                    if v != number_of_threads - 2 :
                        t = threading.Thread(target = factorial,args = (w, f))
                        threads.append(t)
                        t.start()
                        w = f +1
                        f += a + 1
                        v += 1
                    else:
                        t = threading.Thread(target = factorial,args = (w, f))
                        threads.append(t)
                        t.start()
                        w = f +1
                        f = n
                        v += 1

                else:
                    continue      
    for i in threads:
        i.join

def func_time(a,b):
    """а - с потоком, b без потоков"""
    if a < b:
        print("Функция с потоками выполняется быстрей на: " f'{b-a:.10f} "сек."')
    else:
        print("Функция без потоков выполняется быстрей на: " f'{a - b:.10f} "сек."')
    



start_t = time.time()
threading_factorial(1000,3)
counter = 1
a = 0
thread_time = time.time() -  start_t 
print("Функция с потоками выполняется:"f'{thread_time:.4f} "сек."')

factorial_t = time.time()
factorial(1,1000) # jn 1 до числа вычесления 
factorial_time = time.time() - factorial_t
print("Функция без потоков выполняется:"f'{factorial_time:.4f} "сек."\n')

func_time(thread_time,factorial_time)






