import functions as fn
on = True
asientos = fn.crear_asientos()
users = []
ruts = []
while on:
    try:
        print("--------------------------------")
        print("1) Ver Asientos disponibles.")
        print("2) Comprar asiento.")
        print("3) Anular vuelo.")
        print("4) Modificar datos de pasajero.")
        print("5) Salir.")
        print("--------------------------------")
        opc = int(input("Opcion: "))
        if opc == 1:
            while True:
                try:
                    n = int(input("Numero de asiento a checkear: "))
                    check = fn.check_asiento(str(n),asientos)
                    if check:
                        print(f"Asiento disponible!: {n}")
                    else:
                        print(f"Asiento no disponible {n}")
                    print(asientos)
                    break
                except ValueError:
                    print("Valor incorrecto.")
        elif opc == 2:
            user = fn.registrar_pasajero(ruts)
            while True:
                try:
                    print("Asientos Disponibles")
                    print(asientos)
                    n = int(input("Numero de asiento: "))
                    check = 0
                    if n < 1 or n > 42:
                        check = 80
                        print("Numero de asiento no existe")
                        break
                    if str(n) in [str(i) for i in range(31,43)]:
                        tipo = "Vip"
                        valor = 24000
                    else:
                        tipo = "Normal"
                        valor = 78900
                    if check != -1:
                        while True:
                            try:
                                print(f"Total a pagar: {valor}, Tipo: {tipo},")
                                cantidad = int(input('Cantidad a pagar: '))
                                if cantidad < 1:
                                    print("La cantidad a apagar no puede ser menor a 1")
                                else:
                                    if cantidad < valor:
                                        print("La cantidad a pagar es insuficiente.")
                                    else:
                                        print(f"Vuelo pagado!, Su vuelto es de {cantidad - valor}")
                                        check = fn.comprar_asiento(str(n),asientos)
                                        if check == -1:
                                            print("No existe ese asiento!")
                                            break
                                        else:
                                            user.append(check)
                                            users.append(user)
                                            ruts.append(user[0])
                                            print("--------------------------------")
                                            print("Usuario Registrado!")
                                            print(f"Rut: {user[0]}")
                                            print(f"Nombre: {user[1]}")
                                            print(f"Numero de telefono: {user[2]}")
                                            print(f"Banco: {user[3]}")
                                            print(f"Precio pagado: {user[-1][0]}")
                                            print(f"Tipo: {user[-1][1]}")
                                            print(f"Numero de vuelo: {user[-1][2]}")
                                            print(f"Numero de asiento: {user[-1][3]}")
                                            print("--------------------------------")
                                            break
                            except ValueError:
                                print("Error de valor")
                                break
                        break
                    else:
                        print("Asiento no disponible")
                        break
                except ValueError:
                    print("Valor incorrecto.")
        elif opc == 3:
            if len(users) < 1:
                print("No hay usuarios registrados")
            else:
                anular = fn.anular_vuelo(ruts,users,asientos)
                if anular != -1:
                    print("Vuelo anulado!")
                else:
                    print("Su vuelo no existe")
        elif opc == 4:
            while True:
                if len(users) < 1:
                    print("No hay usuarios en el sistema")
                    break
                try:
                    print("--------------------------------")
                    print("Tipo de datos para cambiar.")
                    print("1) Nombre")
                    print("2) Telefono")
                    print("3) Salir")
                    print("--------------------------------")
                    dato = int(input("Opcion: "))
                    if dato == 1:
                        fn.modificar_usuario(dato,ruts,users)
                        break
                    elif dato == 2:
                        fn.modificar_usuario(dato,ruts,users)
                        break
                    elif dato == 3:
                        print("Saliendo de modificar...")
                        break
                    else:
                        print("Dato invalido")
                except ValueError:
                    print("Dato invalido")
        elif opc == 5:
            print("Hasta luego")
            on = False
    except ValueError:
        print("Dato invalido")