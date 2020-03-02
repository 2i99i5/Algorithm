# coding: utf-8

# PEP-8
"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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
print(f'{min_pos = }  {max_pos = }')
if max_pos < min_pos:
    min_pos, max_pos = max_pos, min_pos
sum_ = 0
for id in range(min_pos + 1, max_pos):
    sum_ += array[id]
print(f'{sum_= }')
