tabla = []
m = 1
while True:
    try:
        n = int(input("Numero: "))
        while m <= 10:
            tabla.append(m*n)
            m+=1
        break
    except ValueError:
        print("Ingresa un valor valido!.")
print(tabla)
        