'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

import random
n = int(input("Введите размер списка: "))
a = []
for i in range(0, n):   # генерируем случайный массив с числами от -10 до 10
    a.append( random.randint(-10,10))
print("Массив A:" + str(a))

min = int (input ("Введите минимальное значение: "))
max = int (input ("Введите максимальное значение: "))
res_arr = []
for i in range(len(a)):
    if a[i] >= min and a[i] <= max:
        res_arr.append(i)
print("Индексы:" + str(res_arr))