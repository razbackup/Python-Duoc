import numpy as np
import random as r
arr = np.array([10])
lista = list()
cont = 0
for i in arr:
    while cont <= int(i):
        nArr = np.append(arr,r.randint(1,10))
        print(nArr)
        cont+=1
