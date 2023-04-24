'''

'''

n = int(input("Введите кол-во кустов: "))
a = []
for i in range (0,n):
    a.append(int(input("Введите ягоды на "+ str(i+1)+ " кусте: ")))

print (a)
berry=[]
berry.append(a[0]+a[n-1]+a[1])
for i in range (1,n-1):
    berry.append(a[i-1]+a[i]+a[i+1])
print ("Можно собрать максимум: " + str((max(berry))))