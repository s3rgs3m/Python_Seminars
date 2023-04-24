'''
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

def pwr(a : int, b: int):
    result = 1
    for i in range(0,b):
        result *= a
    return result

a = int(input("Введите A: "))
b = int(input("Введите B: "))

print("A^B: "+ str(pwr(a,b)))