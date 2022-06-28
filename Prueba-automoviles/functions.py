import numpy as np
from random import randint as rd
def generar_estacinamiento():
    arr = []
    arr2  = []
    num = 1
    cont = 0
    while num <= 24:
        if cont == 4:
            arr.append(np.array(arr2))
            cont = 0
            arr2 = []
        arr2.append(str(num))
        num = num + 1
        cont = cont + 1
    return np.array(arr)

def obtener_lugar(estacionamientos):
    espace = rd(0,20)
    y = rd(0,4)
    x = 0
    cont = 0
    for i in estacionamientos:
        if list(i).count(str(f"{espace}")):
            if cont >= 4:
                cont = 3
            x = cont
            break
        else:
            cont+=1
    return [x,y]

def asignar_estacionamiento(vehiculos,estacionamientos,index):
    while True:
        indexs = obtener_lugar(estacionamientos)
        x = indexs[0]
        y = indexs[1]
        if not estacionamientos[y][x] == "X":
            break
    vehiculos[index].append(estacionamientos[y][x])
    lugar = estacionamientos[y][x]
    estacionamientos[y][x] = "X"
    return [estacionamientos,lugar,vehiculos[index]]


def consultar_vehiculo(patentes,patente):
    if patentes.count(patente):
        if len(patente) == 6:
            print("Patente encontrada")
            index = patentes.index(patente)
            return index
        else:
            return -1
    else:
        return -1
def registrar_vehiculo(patentes):
    on = True
    while on:
        print("Ejemplo: AE1234 o AEBE12")
        patente = str(input("Ingresa patente: ")).strip().upper()
        if patentes.count(patente):
            print("Esa patente ya existe!")
        else:   
            if len(patente) == 6:
                print("Patente registrada")
                on = False
            else:
                print("Patente invalida, ingrese nuevamente")
    on = True
    while on:
        print("Marca debe tener entre 2 o 15 caracteres")
        marca = str(input("Marca: ")).strip().upper()
        if not len(marca) < 2 or len(marca) > 15:
            print("marca registrada")
            on = False
        else:
            print("Marca invalida, ingrese nuevamente")
    on = True
    while on:
        try:
            print("El precio del vehiculo tiene que ser mayor a $5.000.000")
            precio = int(input("Precio: "))
            if precio > 5_000_000:
                print("Precio registrado")
                on = False
            else:
                print("Precio invalida, ingrese nuevamente") 
        except ValueError:
            print("Dato invalido")
    return[patente, marca, precio]
            