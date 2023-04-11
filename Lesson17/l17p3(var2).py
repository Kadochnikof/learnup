import threading
import time


class myThreadClass(threading.Thread):
    def __init__(self, argA, argB):
        super().__init__()
        self.argA = argA
        self.argB = argB

    def run(self):
        fact(self.argA, self.argB)


num_thread = 1  # глобальная переменная = номер потока
counter = 1  # глобальная переменная - счетчик результата


def fact(start, end):
    """Возводит число в факториал"""
    global num_thread
    global counter
    for i in range(start, end + 1):
        counter *= i
    num_thread += 1

# limit - число факториала
# num_of_threads - число потоков


def many_threads(limit, num_of_threads):
    """Распределение множества потоков"""
    threads = []
    for i in range(1, num_of_threads+1):
        argA = limit*(i-1) // num_of_threads
        argB = limit*(i) // num_of_threads
        print(f"Поток: {i} - Старт отсчета: {argA+1}, конец отсчета: {argB}")
        t = myThreadClass(argA+1, argB)
        threads.append(t)
        t.start()
        print(f"Старта потока: {i}")
        # print(i, " поток, ответ: ", counter)
    for t in threads:
        t.join()


def func_time(threadsOn, threadsOff):
    """threadsOn - с потоком, threadsOff без потоков"""
    if threadsOn < threadsOff:
        print(
            f"Функция с потоками выполняется быстрей на: {threadsOff-threadsOn:.10f} сек.")
    else:
        print(
            f"Функция без потоков выполняется быстрей на: {threadsOn - threadsOff:.10f} сек.")


start_t = time.time()
many_threads(1000, 10)
counter = 1
num_thread = 0
thread_time = time.time() - start_t
print(f"Функция с потоками выполняется за: {thread_time:.4f} сек.")

factorial_t = time.time()
fact(1, 1000)
factorial_time = time.time() - factorial_t
print(f"Функция без потоков выполняется за: {factorial_time:.4f} сек.")

func_time(thread_time, factorial_time)
