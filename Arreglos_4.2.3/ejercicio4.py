import string as st
import random as rd
from numpy import *
strr = [i for i in st.ascii_letters]
arr = ones((4,4), dtype=str)
for i in arr:
    for j in range(0,4):
        i[j] = strr[rd.randint(0,len(strr)-1)]
print(arr)
vocales = ['a','e','i','o','u']
aux = []
for i in arr:
    cont = 0
    while cont <= 3:
        if vocales.count(i[cont].lower()):
            aux.append(i[cont])
        cont+=1
print(f"Cantidad de vocales {len(aux)} Vocales encontradas {aux}")
