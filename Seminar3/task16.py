# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.
#
# 5
# 1 2 3 4 5
# 3
# -> 1
import random
n = int(input("Введите N: "))
a = []
for i in range(0, n):   # генерируем случайный массив с числами от 0 до 9
    a.append( random.randint(0,9))
print("Массив A:" + str(a))
x = int (input ("Введите Х: "))
print ("Кол-во числа "+str(x)+ " в массиве А равно " + str(a.count(x)))
