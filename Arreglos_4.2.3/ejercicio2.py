from numpy import *
arr = ones((10,4), dtype= int)
print(arr)
cont = 0
num = 1
for i in arr:
    index = 0
    for j in range(0,4):
        i[j] = num
        num+=1
print(arr)