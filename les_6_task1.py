# coding: utf-8

# PEP-8
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Les2_Task2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

import sys
import inspect
from collections import Counter

A = 123456789  # искомое число 9 цифр
memory = {}  # словарь для записи результатов


def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += show_size(item)
    return size


# вариант 1
def while_1(num):
    # потребляет 40 байт при числе из 9 цифр
    memory[inspect.stack()[0][3]] = 0  # в inspect.stack()[0][3] имя вызывваемой функции
    even, odd = 0, 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)
    return f'четных - {even}, нечетных - {odd}'


# вариант 2
def for_2(num):
    # потребляет 88 байт при числе из 9 цифр
    memory[inspect.stack()[0][3]] = 0
    num = str(num)
    even = odd = 0
    for i in num:
        if i in {'0', '2', '4', '6', '8'}:
            even += 1
        else:
            odd += 1
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)
    return f'четных - {even}, нечетных - {odd}'


# вариант 3
def counter_3(num):
    # потребляет 225 байт при числе из 9 цифр
    memory[inspect.stack()[0][3]] = 0
    spam = []
    while num > 0:
        if num % 2 == 0:
            spam.append('even')
        else:
            spam.append('odd')
        num = num // 10
    spam = dict(Counter(spam))
    for loc in locals().values():
        memory[inspect.stack()[0][3]] += show_size(loc)
    return spam


print(f'в числе {A}')
print(while_1(A))
print(for_2(A))
print(counter_3(A))
print('*' * 50)
for name in memory:
    print(f'Функция {name} потребляет {memory[name]} байт памяти на переменные')

"""
Выводы:
OS: Win10x64
Преобразование типов занимает много памяти. Наиболее экономным вариантом является работа с числом (Вариант 1),
так как не создаются другие типы данных. Работа со словарями потребляет много памяти.
"""
