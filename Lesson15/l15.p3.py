def debug(func):
    def action(x, y):
        print(f"Имя вызываемой функции: {func.__name__} с аргументами {x} и {y}")
        print(f"Результат выполнения функции: {func(x, y)}")
        return func(x, y)
    return action


@debug
def summNum(x, y):
    return x + y

result = summNum(2, 3)
print(result)
