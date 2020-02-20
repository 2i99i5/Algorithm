# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1ce0CVEqWnkHNB60przWkWJl4bebQ4WlK/view?usp=sharing
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = int(input('Введите натуральное число:'))
even = odd = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f'{even=}, {odd=}')
