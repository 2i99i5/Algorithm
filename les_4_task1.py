# coding: utf-8

# PEP-8
"""
2.4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
 Количество элементов (n) вводится с клавиатуры.
"""
import timeit
import cProfile


# 1. Рекурсия
def recursion_sum(num):
    if num == 1:
        return 1
    sum_ = (-0.5) ** (num - 1)
    return sum_ + recursion_sum(num - 1)


# 2. Цикл
def cycle_sum(num):
    summ1 = 1
    i = 1
    while num > i:
        summ1 += (-1 / 2) ** i
        i += 1
    return summ1


# 3. Цикл из разбора ДЗ
def cycle2_sum(num):
    item = 1
    summ2 = 0
    for _ in range(num):
        summ2 += item
        item /= -2
    return summ2


# 4. Геометричская прогрессия из разбора ДЗ
def geometry_sum(num):
    return 1 * (1 - (-0.5) ** num) / (1 - (-0.5))


"""
n = int(input('Введите натуральное число n = '))
sum_ = cycle_sum(10000000)
print(f'Сумма равна {sum_}')
"""

print('Геометрическая прогрессия')
print(timeit.timeit('geometry_sum(10)', number=1000, globals=globals()))  # 0.00047419999999999754
print(timeit.timeit('geometry_sum(20)', number=1000, globals=globals()))  # 0.0004615000000000001
print(timeit.timeit('geometry_sum(40)', number=1000, globals=globals()))  # 0.000429800000000001
print(timeit.timeit('geometry_sum(80)', number=1000, globals=globals()))  # 0.0003759000000000019
print(timeit.timeit('geometry_sum(160)', number=1000, globals=globals()))  # 0.00037660000000000124
print(timeit.timeit('geometry_sum(320)', number=1000, globals=globals()))  # 0.00037600000000000133
print(timeit.timeit('geometry_sum(640)', number=1000, globals=globals()))  # 0.00040830000000000033
cProfile.run('geometry_sum(40)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:41(geometry_sum)
cProfile.run('geometry_sum(80)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:41(geometry_sum)
cProfile.run('geometry_sum(160)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:41(geometry_sum)
cProfile.run('geometry_sum(320)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:41(geometry_sum)
cProfile.run('geometry_sum(640)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:41(geometry_sum)

print('Цикл for')
print(timeit.timeit('cycle2_sum(10)', number=1000, globals=globals()))  # 0.0028152999999999997
print(timeit.timeit('cycle2_sum(20)', number=1000, globals=globals()))  # 0.003219099999999999
print(timeit.timeit('cycle2_sum(40)', number=1000, globals=globals()))  # 0.0036699000000000037
print(timeit.timeit('cycle2_sum(80)', number=1000, globals=globals()))  # 0.0068333000000000005
print(timeit.timeit('cycle2_sum(160)', number=1000, globals=globals()))  # 0.013639900000000003
print(timeit.timeit('cycle2_sum(320)', number=1000, globals=globals()))  # 0.029284799999999993
print(timeit.timeit('cycle2_sum(640)', number=1000, globals=globals()))  # 0.058918
cProfile.run('cycle2_sum(40)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:31(cycle2_sum)
cProfile.run('cycle2_sum(80)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:31(cycle2_sum)
cProfile.run('cycle2_sum(160)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:31(cycle2_sum)
cProfile.run('cycle2_sum(320)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:31(cycle2_sum)
cProfile.run('cycle2_sum(640)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:31(cycle2_sum)

print('Цикл while')
print(timeit.timeit('cycle_sum(10)', number=1000, globals=globals()))  # 0.0029106999999999883
print(timeit.timeit('cycle_sum(20)', number=1000, globals=globals()))  # 0.005505299999999991
print(timeit.timeit('cycle_sum(40)', number=1000, globals=globals()))  # 0.011728800000000011
print(timeit.timeit('cycle_sum(80)', number=1000, globals=globals()))  # 0.023169800000000018
print(timeit.timeit('cycle_sum(160)', number=1000, globals=globals()))  # 0.047327600000000025
print(timeit.timeit('cycle_sum(320)', number=1000, globals=globals()))  # 0.09735930000000004
print(timeit.timeit('cycle_sum(640)', number=1000, globals=globals()))  # 0.19177770000000005
cProfile.run('cycle_sum(40)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:21(cycle_sum)
cProfile.run('cycle_sum(80)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:21(cycle_sum)
cProfile.run('cycle_sum(160)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:21(cycle_sum)
cProfile.run('cycle_sum(320)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:21(cycle_sum)
cProfile.run('cycle_sum(640)')  # 0.000    0.000    0.000    0.000 les_4_task1.py:21(cycle_sum)

print('Рекурсия')
print(timeit.timeit('recursion_sum(10)', number=1000, globals=globals()))  # 0.004038299999999939
print(timeit.timeit('recursion_sum(20)', number=1000, globals=globals()))  # 0.007862900000000006
print(timeit.timeit('recursion_sum(40)', number=1000, globals=globals()))  # 0.016339899999999963
print(timeit.timeit('recursion_sum(80)', number=1000, globals=globals()))  # 0.033074200000000054
print(timeit.timeit('recursion_sum(160)', number=1000, globals=globals()))  # 0.06908829999999999
print(timeit.timeit('recursion_sum(320)', number=1000, globals=globals()))  # 0.14181900000000003
print(timeit.timeit('recursion_sum(640)', number=1000, globals=globals()))  # 0.2969859
cProfile.run('recursion_sum(40)')  # 40/1    0.000    0.000    0.000    0.000 les_4_task1.py:13(recursion_sum)
cProfile.run('recursion_sum(80)')  # 80/1    0.000    0.000    0.000    0.000 les_4_task1.py:13(recursion_sum)
cProfile.run('recursion_sum(160)')  # 160/1    0.000    0.000    0.000    0.000 les_4_task1.py:13(recursion_sum)
cProfile.run('recursion_sum(320)')  # 320/1    0.000    0.000    0.000    0.000 les_4_task1.py:13(recursion_sum)
cProfile.run('recursion_sum(640)')  # 640/1    0.000    0.000    0.000    0.000 les_4_task1.py:13(recursion_sum)

"""
Вывод: Вычисление по формуле геометрической прогрессии даёт сложность О(1) и является самым быстрым.
Остальные реализации алгоритма имеют сложность O(n) за счёт однократного прохода по массиву данных.
Цикл for выполняется быстрее чем while. Рекурсивный вызов является самым медленным, и кроме того может вызывать
переполнение стека.
"""
