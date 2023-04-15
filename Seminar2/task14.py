# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. 
n1 = input('Enter N:')
if not n1.isdigit():
    print("Wrong number!")
    exit()
n = int(n1)
s = 0
for i in range(0,n):
    s = 2**i
    if not s<=n:
        exit()
    print (s)
