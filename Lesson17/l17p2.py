import urllib.request
import time
import threading

urls = [
    'https://www.yandex.ru', 'https://www.google.com', 
    'https://www.habrahabr.ru', 'https://www.python.org', 'https://docs.python.org', 
    'https://en.wikipedia.org', 'https://ru.wikipedia.org', 
]

def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()
    
start_t_main = time.time()
for url in urls:
    read_url(url)
    # print(url)
print("Время на прочтение urls, main: ", time.time() - start_t_main)

start_t_threads = time.time()
threads = []
for url in urls:
    t = threading.Thread(target=read_url, name=str(url), args=(url,))
    # print(t.name)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Время на прочтение urls, threads: ", time.time() - start_t_threads)
       
print("Вывод: Многопоточность в данном случае быстрее")
