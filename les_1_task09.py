# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1tUlAq3ZSsDFw6i7wOHrY2A6gigWQQ_JQ/view?usp=sharing
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""

a = int(input('Введи число a: '))
b = int(input('Введи число b: '))
c = int(input('Введи число c: '))

if a > b:
    if b > c:
        print(f'{b=}')
    else:
        if a > c:
            print(f'{c=}')
        else:
            print(f'{a=}')
else:
    if a > c:
        print(f'{a=}')
    else:
        if c > b:
            print(f'{b=}')
        else:
            print(f'{c=}')
