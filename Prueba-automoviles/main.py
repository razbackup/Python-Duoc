import functions as fn
patentes = []
vehiculos = []
estacinamiento = fn.generar_estacinamiento()
on = True
while on:
    try:
        print("-----------------------")
        print("Bienvenido a Automotora Eleseo")
        print("1) Registrar Vehiculo")
        print("2) Consultar y Asignar Estacionamineto Vehiculo")
        print("3) Consultar Estacinamiento")
        print("4) Salir")
        print("-----------------------")
        opc = int(input("Opcion: "))
        if opc == 1:
            vehiculo = fn.registrar_vehiculo(patentes)
            vehiculos.append(vehiculo)
            patentes.append(vehiculo[0])
        elif opc == 2:
            if len(patentes) < 1:
                print("No hay patentes registradas")
            else:
                patente = str(input("Ingresa patente: ")).strip().upper()
                check = fn.consultar_vehiculo(patentes, patente)
                if check != -1:
                    asig = fn.asignar_estacionamiento(vehiculos, list(estacinamiento), check)
                    print(f"El vehiculo de la pantente {patente} fue asignado en {asig[1]}")
                    print("Datos")
                    print(f"Patente: {patente}")
                    print(f"Marca: {asig[2][1]}")
                    print(f"Precio: ${asig[2][2]}")
                    for i in asig[0]:
                        print(i)
                else:
                    print("Patente no encontrada / invalida")
        elif opc == 3:
            print("Lugares disponibles y no disponibles (X)")
            print(estacinamiento)
            if len(vehiculos) < 1:
                print("No vehiculos disponibles aun")
            else:
                for i in vehiculos:
                    try:
                        print("-------------")
                        print(f"Asignado en {i[3]}")
                        print(f"Patente: {i[0]}")
                        print("-------------")
                    except IndexError:
                        print("-------------")
                        print(f"Patente: {i[0]}")
                        print(f"Aun no asignado")
                        print("-------------")
        elif opc == 4:
            print("Saliendo...")
            on = False
        else:
            print("No existe esa opcion")
    except ValueError:
        print("Dato invalido")