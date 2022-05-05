menor = 0
mayor = 0
for i in range(1,6):
    n = int(input(f"Numero {i}: "))
    if n < 0:
        print("Numero menor a 0")
        menor+= 1
    else:
        print("Numero Mayor a 0")
        mayor+= 1

print(f"""
Cantidad de numeros mayores: {mayor} 
Cantidad de numeros menores: {menor} 

""")