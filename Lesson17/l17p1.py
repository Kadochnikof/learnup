import threading
import time


def fact1(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
    return result


# many_threads1 - вычисляет факториал x частей-диапазонов x разными потоками.
# n - конечно число факториала, x - кол-во потоков
def many_threads1(n, x):
    threads = []
    for i in range(1, x+1):
        t = threading.Thread(target=fact1, name=str(
            i), args=(n*(i-1) // x, n*(i) // x))
        print("Старт, конец: ", n*(i-1) // x, n*(i) // x, end="\n")
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return threads


t_start1 = time.time()
many_threads1(100000, 16)
t_end1 = time.time()
print(f"Общее время, threads: {t_end1 - t_start1}")

t_start2 = time.time()
fact1(1, 100000)
t_end2 = time.time()
print(f"Общее время, main: {t_end2 - t_start2}")
print("Вывод: Многопоточность в данном случае быстрее")
