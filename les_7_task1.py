# coding: utf-8

# PEP-8
"""
1.Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
  Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random

OFFSET = 100  # смещение генератора случайных чисел
QUANTITY = 20  # количество элементов списка


def revers_short_bubble(arr):
    flag = True
    sort_len = len(arr) - 1
    while sort_len > 0 and flag:
        flag = False
        for i in range(sort_len):
            if arr[i] < arr[i + 1]:
                flag = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        sort_len -= 1


array = [random.randint(-OFFSET, OFFSET - 1) for _ in range(QUANTITY)]
print(f'Исходный массив:\n{array}')
revers_short_bubble(array)
print(f'Отсортированный массив:\n{array}')
