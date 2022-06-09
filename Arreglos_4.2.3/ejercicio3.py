from random import randint as rd
from numpy  import *
arr = ones((4,5), dtype= int)
cont = 0
for i in arr:
    for j in range(0,5):
        i[j] = rd(0,100)
cont = 0
print(arr)
for i in arr:
    cont+=1
    print(f" Suma fila {cont} {i.sum()}")
total = 0
x = 0
cont = 0
while x <= 4:
    cont = 0
    total = 0 
    while cont <= 3:
        total+= arr[cont][x]
        cont+=1
    x+=1
    print(f"Suma columna {x} {total}")
pos = 0
x = 0
total = 0
nums = []
while x <= 3:
    total+=arr[x][pos]
    nums.append(arr[x][pos])
    x+=1
    pos+=1
print(f"Suma de la primera diagonal {total} Numero de la diagonal {nums}")
for i in arr:
    cont = 0
    while cont <= 4:
        if not i[cont]%2 == 0:
            print(f"numeros impares {i[cont]}")
        cont+=1
