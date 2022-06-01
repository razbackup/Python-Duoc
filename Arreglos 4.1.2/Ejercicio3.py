from numpy import *
from random import randint as rd
arregloA = array([rd(0,300) for i in range(0,10)])
arregloB = arregloA
print(f"Suma de cada elemento de los Arrays {arregloA + arregloB}")
print(f"Suma del conjunto de los elementos de ambos Arrays {(arregloA + arregloB).sum()}")
for i in arregloB:
    cont = 0
    print(f"Tabla del {i}")
    while cont <= 10:
        print(f"{cont} X {i} = {cont*i}")
        cont+=1
