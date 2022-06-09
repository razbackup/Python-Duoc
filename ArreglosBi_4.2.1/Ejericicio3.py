from numpy import *
# print(diag([1,2,3]))
# 
# arr = array([[1,0,0],[0,2,0],[0,0,3]])
# print(arr)

arr = zeros((3,3), dtype=int)
cont = 0
num = 1
for i in arr:
    i[cont] = num
    num+=1
    cont+=1
print(arr)
        
