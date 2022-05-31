from numpy import *
from random import randint as rn
arr = array([rn(0,100) for i in range(1,11)])
arr2 = arr[:].copy()
print(f"elemento mayor: {arr2.max()}")
print(f"elemento menor: {arr2.min()}")
print(f"Suma de elementos: {arr2.sum()}")
print(f"Promedio de los elementos: {arr2.mean()}")
print(f"Elementos: {[i for i in arr2]}")

