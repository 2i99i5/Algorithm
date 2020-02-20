# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1ce0CVEqWnkHNB60przWkWJl4bebQ4WlK/view?usp=sharing
4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
 Количество элементов (n) вводится с клавиатуры.
"""


def devil_sum(num):
    if num == 1:
        return 1
    sum = (-0.5) ** (num - 1)
    return sum + devil_sum(num - 1)


n = int(input('Введите натуральное число n = '))
sum = devil_sum(n)
print(f'Сумма равна {sum}')

"""
sum = 1
i = 1
while n > i:
    sum = sum + (-1 / 2) ** i
    i += 1
print(f'Сумма равна {sum}')
"""
