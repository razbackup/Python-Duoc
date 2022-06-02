from numpy import *
from random import randint as rd
cont = 0
bi_arr = []
while cont <= 2:
    bi_arr.append([rd(0,100) for i in range(0,3)])
    cont+=1 
arr = array(bi_arr)
print(arr)
print(arr.mean())
print(arr.sum())
print(arr.max())
print(arr.min())
print(diag([arr[0][0],arr[1][1],arr[2][2]]))