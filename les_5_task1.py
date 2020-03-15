# coding: utf-8

# PEP-8
"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

companies = {}
n = int(input("Количество предприятий: "))
s = 0
for i in range(n):
    name = input("Предприятие №" + str(i + 1) + ": ")
    profit = []
    for j in range(4):
        print(f'{j + 1}-й квартал')
        profit.append(int(input("прибыль: ")))
    companies[name] = profit
    s += sum(profit)

avrg = s / n
print("\nСредняя прибыль: %.0f." % avrg)
print("\nКомпании с прибылью выше средней:")
for i in companies:
    if sum(companies[i]) > avrg:
        print(i)
print("\nКомпании с прибылью ниже средней:")
for i in companies:
    if sum(companies[i]) < avrg:
        print(i)
