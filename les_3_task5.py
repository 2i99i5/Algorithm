# coding: utf-8

# PEP-8
"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_pos = -1
i = 0
while i < SIZE:
    if array[i] < 0 and (max_pos == -1 or array[i] > array[max_pos]):
        max_pos = i
    i += 1

print('отрицательных элементов нет' if max_pos == -1 else f'{array[max_pos]} на {max_pos + 1} позиции')
