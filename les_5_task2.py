# coding: utf-8

# PEP-8
"""
2.Написать программу сложения и *умножения* двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def summ(x, y):
    template = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    if len(x) > len(y):
        x, y = y, x  # y должен быть длиннее
    y = y[::-1]  # реверс числа
    sum_ = []
    j = -1
    k = 0
    for i in y:  # побитово складываем с переносом разряда
        y_i = template.index(i)
        x_i = template.index(x[j])
        sum_.append(template[(y_i + x_i + k) % 16])
        if (y_i + x_i) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(x) - 1:
            break
    diff = len(y) - len(x)
    if diff:
        for _ in y[-diff:]:
            sum_.append(template[(template.index(y[-diff]) + k) % 16])
            if template.index(y[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
    if k == 1:
        sum_.append('1')
    return sum_[::-1]


def hex_to_dec(x):
    template = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    len_x = len(x)
    dec_x = 0
    for i in range(len_x):
        dec_x = dec_x + template.index(x[i]) * 16 ** (len_x - i - 1)
    return int(dec_x)


def multi_sum(x, y):
    num = hex_to_dec(x)
    mul = ['0']
    for _ in range(num):
        mul = summ(mul, y)
    return mul


x = input('Число x = ')
y = input('Число y = ')
print(summ(x, y))
# print(multi_sum(x, y))  # не работает
