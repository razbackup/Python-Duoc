import functions as fn
on = True
productos = [] # 1 producto, 2 producto
codigos = [] # 1 codigo, 2 codigo
while on:
    try:
        print("-----------------------------")
        print("1) Guardar un producto.")
        print("2) Buscar un producto.")
        print("3) Generar una orden.")
        print("4) Salir")
        print("-----------------------------")
        opc = int(input("Opcion: "))
        if opc == 1:
            print("Codigo mayor a 4 digitos\nNombre mayor a 3 digitos\nPrecio mayor a 0\nMarca de unidad U (Unidad) o K (Kilos)")
            while True:
                codigo = str(input("Codigo: ")).strip()
                codigo_validado = fn.validador_codigo(codigo)
                comparador = fn.comparador_codigo(codigo_validado,codigos)
                if codigo_validado == True or comparador == True:
                    print("Codigo invalido...")
                else:
                    prod = fn.guardar_producto(codigo_validado)
                    productos.append(prod)
                    codigos.append(prod[0])
                    break
        elif opc == 2:
            codigo = str(input("Codigo: ")).strip()
            codigo_validado = fn.validador_codigo(codigo)
            if codigo_validado == True:
                print("Codigo invalido...")
            else:
                producto = fn.buscar_producto(codigo_validado,codigos,productos)
                if producto == True:
                    print("Codigo no encontrado, registrado nuevamente")
                else:
                    print("- - - - - Producto Encontrado! - - - - -")
                    print(f"Codigo: {producto[0]}")
                    print(f"Nombre: {producto[1]}")
                    print(f"Precio: ${producto[2]}")
                    print(f"Medida: {producto[3]}")
                    print("- - - - - - - - - - - - - - - - - - - -")
        elif opc == 3: 
            while True:
                codigo = str(input("Codigo: ")).strip()
                orden = fn.generar_orden(codigo,codigos,productos)
                if not isinstance(orden,list):
                    print(orden)
                else:
                    print("==============================================")
                    print(f" Numero de Orden: {orden[0]}")
                    print(f" Nombre Proveedor: {orden[1]}")
                    print(f" Codigo producto: {orden[-1][0]}")
                    print(f" Nombre del producto: {orden[-1][1]}")
                    print(f" Precio del producto: ${orden[-1][2]}")
                    print(f" Unidad de medida: {orden[-1][3]}")
                    print(f" Cantidad seleccionada: {orden[2]}")
                    print(f" Total {orden[2]} X {orden[-1][2]}: ${orden[3]}")
                    print("================================================")
                    break
        elif opc == 4:
            cont = 5
            while cont <= 5:
                os.system('cls')
                print(f"Programa cerrandose en {cont}")
                cont+=1
                time.sleep(1)
            quit()
        else:
            print("Opcion invalida.")
    except ValueError:
        print("Valor invalido.")