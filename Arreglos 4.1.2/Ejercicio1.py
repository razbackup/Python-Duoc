from numpy import *
from random import randint as rd
leng = [i for i in range(0,100)]
arregloA = array([rd(0,500) for i in range(0,100)])
arregloPar = [arregloA[i] for i in leng if i%2 == 0]
print(f"Elementos Pares: {arregloPar}")
print(f"Elemento Maximo: {arregloA.max()}")
print(f"Elemento Posicion Max: {max(where(arregloA == arregloA.max())[0])}")
print(f"Elemento Menor: {arregloA.min()}")
arregloB = arregloA.copy()
print(f" Elementos multiplicados por tres {arregloB * 3}")
print(f"Suma de los elementos: {arregloB.sum()}")
print(f"Promedio de los elementos: {round(arregloB.mean(),2)}")