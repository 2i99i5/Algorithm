# coding: utf-8

# PEP-8
"""
1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa") -> 6
func("sova") -> 9
s o v a so ov va sov ova / =9
"""

import hashlib


def count_substr(s):
    c_list = set()
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            if j - i != len(s):  # исключаем строку целиком
                c_list.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return len(c_list)


st = " a a"
print(f'Количество различных подстрок в строке \'{st}\' = {count_substr(st)}')
st = "sova"
print(f'Количество различных подстрок в строке \'{st}\' = {count_substr(st)}')
