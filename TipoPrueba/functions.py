from random import randint
def validador_codigo(codigo):
        if len(codigo) == 4:
            return codigo
        else:
            return True
def comparador_codigo(codigo,codigos):
    if not codigos.count(codigo):
        return codigo
    else:
        return True

def guardar_producto(codigo):
    while True:
        nombre = str(input("Nombre: ")).upper().strip()
        if len(nombre) < 3:
            print("Nombre tiene que ser mayor a 3 caracteres...")
        else:
            print("Nombre guardado correctamente...")
            break
    while True:
        try:
            precio = int(input("Precio: "))
            if precio < 1:
                print("Precio tiene que ser mayor a 0")
            else:
                print("Precio guardado correctamente...")
                break
        except ValueError:
            print("Error tipo de valor no valido.")
    while True:
        medida = str(input("Unidad de medida: ")).upper().strip()
        if not medida in ['K','U']:
            print("La unidad de medida no es valida...")
        else:
            print("La unidad de medida guardado correctamente...")
            break
    return [codigo,nombre,precio,medida]

def buscar_producto(codigo,codigos,productos):
    if not codigos.count(codigo):
        return True
    index = codigos.index(codigo)
    return productos[index]

def generar_orden(codigo,codigos,productos):
    valido = validador_codigo(codigo)
    if valido == True:
        return 'Codigo invalido..'
    producto = buscar_producto(codigo,codigos,productos)
    if producto == True:
        return 'Codigo no encontrado, registrado nuevamente'
    n_orden = randint(1,1000)
    while True:
        nombre = str(input("Nombre del proveedor: ")).upper().strip()
        if len(nombre) < 1:
            print("Nombre de proveedor invalido, tiene que tener mas de un caracter.")
        else:
            print("Nombre de proveedor registrado")
            break
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad < 1:
                print("Cantidad invalida no puede ser menor a 1")
            else:
                print("Cantidad registrada correctamente.")
                break
        except ValueError:
            print("Valor invalido")
    total = cantidad * producto[2]
    return [n_orden, nombre, cantidad, total, producto]
    
