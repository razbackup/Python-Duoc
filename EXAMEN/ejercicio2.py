import numpy as np
from random import randint as rd
arr = np.ones((3,3), dtype=int)
arr_uni = []
for i in arr:
    for j in (range(0,3)):
        i[j] = rd(1,100)
        arr_uni.append(i[j])
arr_uni = np.array(arr_uni)
print(f"Los elementos de la pimera diagonal son: {arr.diagonal()}")
print(f"El arreglo bidimensional es: \n{arr}")
print(f"Los elementos en el arreglo unidimensional son: {arr_uni}")
arr_uni.sort()
print(f"Los elementos en el arreglo unidimensional ordenados son: {arr_uni}")