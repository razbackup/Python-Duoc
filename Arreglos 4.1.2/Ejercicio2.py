from numpy import *
from random import randint as rd
arrA = array([rd(0,1000) for i in range(0,10)])
print(f"Elementos: {arrA}")
print(f"Elementos pares {array([i for i in arrA if i%2 == 0])}")
print(f"Suma de elementos impares {array([i for i in arrA if not i%2 == 0]).sum()}")
print(f"Numeros primos: ")
