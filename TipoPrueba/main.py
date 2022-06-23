import functions as fn
from random import randint as rd
on = True
productos = []
while True:
    print("#################")

    print("1) Ingresar producto")
    print("2) Buscar producto")
    print("3) Imprimir Orden de compra")

    print("#################")
    opc = int(input("Opcion: "))
    if opc == 1:
        try:
            while True:
                cod = str(input("Codigo: ")).upper()
                nombre = str(input("Nombre: ")).upper()
                precio = int(input("Precio: "))
                medida = str(input("Medida: ")).upper()
                res = fn.producto(cod,nombre,precio,medida,productos)
                if not isinstance(res,list):
                    print(res)
                else:
                    productos.append(res)
                    print("Producto guardado correctamente.")
                    break 
        except ValueError:
            print("Precio tiene un error, no es del tipo de dato correcto, ingrese la Opcion 1 nuevamente.")
    elif opc == 2:
        while True:
            cod = str(input("Codigo: ")).upper()
            res = fn.buscarProducto(cod,productos)
            if not res:
                print("Codigo ingresado no encontrado...")
                break
            else:
                print("#################")

                print(F"Codigo Buscado: {res[0]}")
                print(F"Nombre: {res[1]}")
                print(F"Precio: {res[2]}")
                print(F"Medida: {res[3]}")

                print("#################")
                break
    elif opc == 3:
        while True:
            provedor = str(input("Provedor: ")).upper()
            n_orden = rd(1,1000)
            cod = str(input("Codigo del producto: ")).upper()
            cantidad = int(input("Cantidad: "))
            orden = fn.generarOrden(provedorfn.buscarProducto(cod))
            if not (orden[0] or orden[1]):
                print("Nombre del provedor o la cantidad no puede ser nula/o")
            else:
                print(f"""
                Orden: {n_orden}
                Provedor: {provedor}
                Cantidad: {cantidad}

                Codigo Producto: {orden[1][0]}
                Nombre: {orden[1][1]}
                Precio: {orden[1][2]} c/u
                Medida: {orden[1][3]}

                Precio X Cantidad: {orden[0]}
                
            """)
            break

        