import functions as fn
arr = []
on = True
while on:
    try:
        print("1. Factorial")
        print("2. Invertir número")
        print("3. Lista con nombres de personas")
        print("4. Salir")
        opc = int(input("Opcion: "))
        if opc == 1:
            try:
                n = int(input("Ingresa el numero: "))
                if n < 1:
                    print("El numero en cuestion no puede se menor a 1")
                else:
                    print(f"El factorial de {n} es: {fn.factorial(n)}")
            except ValueError:
                print("El dato ingresado es invalido")
        elif opc == 2:
            try:
                n = int(input("Numero: "))
                if n < 15 or n > 125:
                    print("El numero en custion tiene que ser entre 15 y 125.")
                else:
                    print(f"El numero {n} invertido es: {fn.invertir_numero(n)}")
            except ValueError:
                print("El dato ingresado es invalido")
        elif opc == 3:
            n_nom = 0
            on_ = True
            while on_:
                try:
                    print(f"1) Ingresar numero de nombres")
                    print(f"2) Ingresar nombres")
                    print(f"3) Listar nombres")
                    print(f"4) Salir de opcion de nombres")
                    opc = int(input("Opcion: "))
                    if opc == 1:
                        n_nom = fn.solicitar_cantidad_nombres()
                    elif opc == 2:
                        if n_nom == 0:
                            print("No hay cantidad de nombres a ingresar, porfavor ingrese nombres en la opcion 1")
                        else:
                            print(f"Cantidad de nombre a ingresar {n_nom}")
                            arr = fn.ingresar_nombres(n_nom,arr)
                            n_nom = 0
                    elif opc == 3:
                        if len(arr) == 0:
                            print("No hay ningun nombre en la lista, pofavor ingrese nombres en la opcion 2")
                        else:
                            print(f"Cantidad de nombres listados {len(arr)}")
                            cont = 1
                            print("################################s")
                            for i in fn.listar(arr):
                                print(f"{cont}) {i}")
                                cont+=1
                            print("################################")
                    elif opc == 4:
                        print("Saliendo....")
                        on_= False
                    else:
                        print("Numero invalido")
                except ValueError:
                    print("Dato invalido")
        elif opc == 4:
            print("Usted saldrá del programa")
            on=False
        else:
            print("Numero invalido")
    except ValueError:
                print("Dato invalido")