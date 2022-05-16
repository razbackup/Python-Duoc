arr = list()
total= 0
for i in range(1,11):
    n = int(input(f"Numero {i}: "))
    arr.append(n)
for i in arr:
    total+=i
print(f"Total: {total} Promedio: {total/len(arr)}")