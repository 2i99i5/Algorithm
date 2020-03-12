# coding: utf-8

# PEP-8
"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""
import timeit
import cProfile


def sieve(n):
    # По подсказке уравнение степенной функции y = 2.7344*x^1.154 округляю параметры, т.к. есть погрешность
    # проверил на n от 1 до 1000, для 10000, 100000
    end_num = round(2.74 * n ** 1.16)
    a = [i for i in range(end_num)]
    count = 0
    for i in range(2, end_num):
        if a[i] != 0:
            count += 1
            if count == n:
                return a[i]
            j = i + i
            while j < end_num:
                a[j] = 0
                j += i


"""
  # наивный перебор, работает очень медленно
def prime_(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        div = 2  # делитель
        while num % div != 0:
            div += 1
        if div == num:
            count += 1
    return num
"""


# перебор с проверкой нечетных и квадратов делителей
def prime(n):
    if n == 1:
        return 2
    elif n < 1:
        return None
    count = 1
    num = 1
    while count < n:
        num += 2
        div = 3  # делитель
        while div * div <= num and num % div != 0:
            div += 2
        if div * div > num:
            count += 1
    return num


print(f'{sieve(2) = }')  # 3
print(f'{prime(4) = }')  # 7
print(f'{sieve(5) = }')  # 11
print(f'{prime(1) = }')  # 2

print('Решето')
print(timeit.timeit('sieve(10)', number=1000, globals=globals()))  # 0.009728300000000002
print(timeit.timeit('sieve(20)', number=1000, globals=globals()))  # 0.0226165
print(timeit.timeit('sieve(40)', number=1000, globals=globals()))  # 0.0535156
print(timeit.timeit('sieve(80)', number=1000, globals=globals()))  # 0.1441228
print(timeit.timeit('sieve(160)', number=1000, globals=globals()))  # 0.35815620000000004
print(timeit.timeit('sieve(320)', number=1000, globals=globals()))  # 0.8352949000000001
print(timeit.timeit('sieve(640)', number=1000, globals=globals()))  # 2.014087
cProfile.run('sieve(40)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:20(sieve)
cProfile.run('sieve(80)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:20(sieve)
cProfile.run('sieve(160)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:20(sieve)
cProfile.run('sieve(320)')  # 0.001    0.001    0.001    0.001 les_4_task2.py:20(sieve)
cProfile.run('sieve(640)')  # 0.002    0.002    0.002    0.002 les_4_task2.py:20(sieve)

print('Без решета + модификации')
print(timeit.timeit('prime(10)', number=1000, globals=globals()))  # 0.00546409999999975
print(timeit.timeit('prime(20)', number=1000, globals=globals()))  # 0.01348079999999996
print(timeit.timeit('prime(40)', number=1000, globals=globals()))  # 0.04119010000000012
print(timeit.timeit('prime(80)', number=1000, globals=globals()))  # 0.1534321000000003
print(timeit.timeit('prime(160)', number=1000, globals=globals()))  # 0.40764489999999975
print(timeit.timeit('prime(320)', number=1000, globals=globals()))  # 1.2358623999999994
print(timeit.timeit('prime(640)', number=1000, globals=globals()))  # 3.6746745
cProfile.run('prime(40)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:37(prime)
cProfile.run('prime(80)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:37(prime)
cProfile.run('prime(160)')  # 0.000    0.000    0.000    0.000 les_4_task2.py:37(prime)
cProfile.run('prime(320)')  # 0.001    0.001    0.001    0.001 les_4_task2.py:37(prime)
cProfile.run('prime(640)')  # 0.003    0.003    0.003    0.003 les_4_task2.py:37(prime)

"""
Вывод: Вычисление методом Решета Эратосфена без модернизации обладает сложностью О(n) и является более быстрым.
Главная сложность состоит в наиболее точном определении интервала, на котором будет работать решето.
Без решета с доп. проверками при удвоении n, время утраивается. Сложность та же, но медленнее.
"""
