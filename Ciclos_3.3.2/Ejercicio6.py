arr = []
cont = 0
while True:
    try:
        nombre = str(input(f"Nombre numero {cont}: "))
        opc = int(input("Desa seguir Ingresando? 1) Si 2) No: "))
        if opc == 1:
            print("Nombre añadido.")
            arr.append(nombre)
        elif opc == 2:
            break
        else:
            print("Numero invalido.")
        cont+=1
    except ValueError:
        print("Valor invalido Ingrese nuevamente...")
        