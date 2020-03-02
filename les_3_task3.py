# coding: utf-8

# PEP-8
"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min = MAX_ITEM
max = MIN_ITEM
min_pos = 0
max_pos = 0
for id, item in enumerate(array):
    if item < min:
        min = item
        min_pos = id
    if item > max:
        max = item
        max_pos = id
array[min_pos], array[max_pos] = array[max_pos], array[min_pos]
print(array)
