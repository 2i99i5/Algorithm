# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1tUlAq3ZSsDFw6i7wOHrY2A6gigWQQ_JQ/view?usp=sharing
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки.
"""
print('Введите координаты первой точки')
x1 = int(input('Введи число x1: '))
y1 = int(input('Введи число y1: '))
print('Введите координаты второй точки')
x2 = int(input('Введи число x2: '))
y2 = int(input('Введи число y2: '))

if x1 == x2:
    print('Нет решений')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Уравнение прямой имеет вид: y = {k}x + {b}')
