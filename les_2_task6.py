# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1ce0CVEqWnkHNB60przWkWJl4bebQ4WlK/view?usp=sharing
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ.
"""
import random

MAX_TRY = 10
MAX_NUM = 100

num = random.randint(0, MAX_NUM)
i = 0
while i < MAX_TRY:
    print(f'Осталось {MAX_TRY - i} попыток')
    ans = int(input('Введите число: '))
    if ans > num:
        print(f'Ваше число больше')
    elif ans < num:
        print(f'Ваше число меньше')
    else:
        print(f'Вы угадали!')
        break
    i += 1
if i == MAX_TRY:
    print(f'Вы не угадали число {num} с {MAX_TRY} попыток')
