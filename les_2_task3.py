# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1ce0CVEqWnkHNB60przWkWJl4bebQ4WlK/view?usp=sharing
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
 Например, если введено число 3486, надо вывести 6843.
"""

num = int(input('Введите натуральное число num='))
mun = 0
while num > 0:
    mun = mun * 10 + num % 10
    num = num // 10
print(f'Обратное число {mun=}')

"""
# второй вариант
num = int(input('Введите натуральное число num='))
mun = ''
while num > 0:
    mun += str(num % 10)
    num = num // 10
mun = int(mun)
print(f'Обратное число {mun=}')
"""
