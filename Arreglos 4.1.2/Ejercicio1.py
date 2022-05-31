from numpy import *
from random import randint as rd
arregloA = array([rd(0,500) for i in range(1,101)])
arregloPar = [i for i in arregloA if i%2 == 0]
print(f"Elementos Pares: {arregloPar}")
print(f"Elemento Maximo: {arregloA.max()}")
print(f"Elemento Posicion Max: {max(where(arregloA == arregloA.max())[0])}")
print(f"Elemento Menor: {arregloA.min()}")
arregloB = arregloA.copy()
print(f" Elementos multiplicados por tres {arregloB * 3}")
print(f"Suma de los elementos: {arregloB.sum()}")
print(f"Promedio de los elementos: {round(arregloB.mean(),2)}")

