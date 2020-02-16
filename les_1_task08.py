# coding: utf-8

# PEP-8
"""
https://drive.google.com/file/d/1tUlAq3ZSsDFw6i7wOHrY2A6gigWQQ_JQ/view?usp=sharing
8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
y = int(input('Введи год y: '))
if y % 4 != 0:
    print("Обычный")
else:
    if y % 100 == 0:
        if y % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")
    else:
        print("Високосный")
