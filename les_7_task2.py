# coding: utf-8

# PEP-8
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

LEFT = 0  # левая граница генератора случайных чисел
RIGHT = 50  # правая граница генератора случайных чисел
QUANTITY = 21  # количество элементов списка


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[:len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2:])
    i = j = 0
    res_arr = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res_arr.append(right[j])
            j += 1
        else:
            res_arr.append(left[i])
            i += 1
    res_arr += left[i:]
    res_arr += right[j:]
    # print(res_arr)
    return res_arr


array = [random.randint(LEFT * 100, RIGHT * 100 - 1) / 100 for _ in range(QUANTITY)]
# array = [random.uniform(LEFT, RIGHT - 1) for _ in range(QUANTITY)]
print(f'Исходный массив:\n{array}')
print(f'Отсортированный массив:\n{merge_sort(array)}')
