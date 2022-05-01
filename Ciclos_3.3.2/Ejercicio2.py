arr = list()
while True:
    try:
        n = int(input("Numero: "))
        if n == 0:
            break
        else:
           arr.append(n) 
    except ValueError:
        print("Dato Invalido...")
arr.sort()
print(arr)
