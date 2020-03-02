# coding: utf-8

# PEP-8
"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
NAT_MIN = 2
NAT_MAX = 99
NUM_MIN = 2
NUM_MAX = 9

amount = 0
for i in range(NUM_MIN, NUM_MAX + 1):
    for j in range(NAT_MIN, NAT_MAX + 1):
        if j % i == 0:
            amount += 1
    print(f'числу {i} кратны {amount} чисел')
    amount = 0
