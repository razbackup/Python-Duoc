total = 0
cont = 1
while cont < 6:
    n = int(input(f"Numero {cont}: "))
    if n < 0:
        print("Numero tiene que ser mayor a 0")
    else:
        total+=n
        cont+=1
print(total)