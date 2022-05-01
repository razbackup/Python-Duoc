arr = list()
cont = 1
total = 0
while True:
    try:
        while cont < 11:
            n = int(input(f"Numero {cont}: "))
            arr.append(n)
            cont+=1
        for i in arr:
            total+=i
        promedio = total / 10
        break
    except ValueError:
        print("Valor invalido")

print(f"""
Numeros: {arr}
Suma: {total}
Promedio: {promedio}
""")
