while True:
    inicio = int(input("Primer Numero: "))
    fin = int(input("Segundo Numero: "))
    if fin < inicio:
        print("El primer numero no puede ser menor al ultimo")
    else:
        print("Rango de numeros")
        while inicio <= fin:
            print(f"Numero: {inicio}")
            inicio+=1