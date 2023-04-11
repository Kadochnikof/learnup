"""Для решения задачи выбираем т.н. Жадный алгоритм, то есть каждый шаг действия выбирает оптимальный вариант результата"""
data = open('file_pairs.txt', 'r')
data.readline()


summ = 0
reserve_num = 0
wrong_num = 0


def max_pair_sum(data):
    global summ, reserve_num, wrong_num
    for row in data:
        num_a, num_b = map(int, row.split())
        max_num = max(num_a, num_b)
        min_num = min(num_a, num_b)
        delta = max_num - min_num
        if delta % 3 != 0 and delta > reserve_num:
            reserve_num = min_num
            wrong_num = max_num
        summ += max_num


def check_sum(summ):
    if summ % 3 == 0:
        print(f"Сумма {summ} делится на 3 без остатка.")
        summ = (summ - wrong_num) + reserve_num
        print(f"Сумма изменена на: {summ}")
    else:
        print(f"Сумма: {summ}")


max_pair_sum(data)
check_sum(summ)
