# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n1 = input('Введите кол-во долек в длину: ')
if n1.isdigit()==False:
    print("Неверно введно кол-во")
    exit()
m1 = input('Введите кол-во долек в ширину: ')
if m1.isdigit()==False:
    print("Неверно введно кол-во")
    exit()
k1 = input('Введите сколько долек отломить за раз: ')
if k1.isdigit()==False:
    print("Неверно введно кол-во")
    exit()
n = int(n1)
m = int(m1)
k = int(k1)
if n<1 or m<1 or k<1 or k>=m*n:
    print("Введенные данные не удовлетворяют условиям задачи")
    exit()

if k%n==0 or k%m==0:
    print("Можно отломить")
else:
    print("Нельзя отломить")