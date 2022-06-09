from numpy import *
from random import randint as rd
arr = array([rd(0,10) for i in range(0,10)])
print(arr)
n = int(input("Numero: "))
for i in arr:
    if i == n:
        res = f"{n} Se encuentra en el array"
        break
    else:
        res = f"{n} No se encuentra en el array"
print(res)