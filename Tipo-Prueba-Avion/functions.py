import numpy as np
from random import randint as rd
def crear_asientos():
    arr = []
    num = 1
    cont = 0
    aux = []
    while num <= 45:
        if cont == 6:
            arr.append(np.array(aux))
            aux = []
            cont = 0
        cont+=1
        aux.append(str(num))
        num+=1
    return np.array(arr)
def check_asiento(num,asientos):
    if int(num) > 42 or int(num) < 1:
        return False
    aux = []
    for i in asientos:
        for j in i:
            aux.append(j)
    if aux.count(num):
        return True
    else:
        return False

def verificar_rut(rut):
    try:
        if len(str(rut)) != 8:
            return False
        else:
            aux = [i for i in str(rut)]
            aux.reverse()
            values = []
            mul = 2
            for i in aux:
                if mul == 8:
                    mul = 2
                a = mul*int(i)
                values.append(a)
                mul+=1
            values = sum(values)
            res = 11 - (values - ((int(values/11)) * 11))
            if res == 11:
                res = 0
            if res == 10:
                res = "K"
            return f"{str(rut)[0:2]}.{str(rut)[2:5]}.{str(rut)[5:8]}-{str(res)}"
    except ValueError:
        return False

def registrar_pasajero(ruts):
    while True:
        nombre = str(input('Nombre: ')).capitalize().strip()
        if len(nombre) < 1 or len(nombre) > 35:
            print("Nombre invalido.")
        else:
            print("Nombre registrado!")
            break
    while True:
        try:
            rut = int(input('Rut (sin puntos ni gion): '))
            res = verificar_rut(rut)
            if ruts.count(res):
                print("RUT ya registrado! ingresa otro...")
            else:
                if res == False:
                    print("Rut invalido")
                else:
                    print("Rut registrado!")
                    print(res)
                    break
        except ValueError:
            print("Dato invalido.")
    while True:
        try:
            telefono = int(input('Telefono: +569'))
            if len(str(telefono)) != 8:
                print("Telefono invalido")
            else:
                print("Telefono registrado!")
                telefono = f"+56 9 {str(telefono)}"
                break
        except ValueError:
            print("Dato invalido.")
    while True:
        banco = str(input('Banco: ')).strip().upper()
        if len(banco) < 1 or len(banco) > 35:
            print("Banco invalido")
        else:
            print("Banco Registrado!")
            break
    return [res,nombre,telefono,banco]
def comprar_asiento(num,asientos,vuelos):
    while True:
        n_vuelo = rd(1,1000)
        if not vuelos.count(n_vuelo):
            vuelos.append(n_vuelo)
            break
    check = check_asiento(num,asientos)
    if check == True:
        index = 0
        lista_index = 0
        for i in asientos:
            if list(i).count(num):
                index = list(i).index(num)
                break
            lista_index+=1
        list(asientos)[lista_index][index] = "X"
        if num in [str(i) for i in range(31,43)]:
            return [240000,"Asiento Vip",n_vuelo,num,lista_index,index]
        else:
            return [78900,"Asiento Normal",n_vuelo,num,lista_index,index]
    else:
        return -1
def anular_vuelo(ruts,users,asientos,vuelos):
    while True:
        rut = int(input('Rut (sin puntos ni gion): '))
        res = verificar_rut(rut)
        if res == False:
            print("Rut invalido")
        else:
            break
    if ruts.count(res):
        index_user = ruts.index(res)
        num = users[index_user][-1][3]
        check = check_asiento(num,asientos)
        if check == False:
            index = users[index_user][-1][4]
            lista_index = users[index_user][-1][5]
            list(asientos)[index][lista_index] = f"{num}"
            print("--------------------------------")
            print(f"Usuario: {users[index_user][1]}, Numero de vuelo: {users[index_user][-1][2]}, Numero de Silla: {users[index_user][-1][3]}, Valor del vuelo devuelto: ${users[index_user][-1][0]}")
            print("--------------------------------")
            users.pop(index_user)
            ruts.pop(index_user)
            vuelos.pop(index_user) 
            return 200
        else:
            return -1
    else:
        return -1

def modificar_usuario(dato,ruts,users):
    while True:
        rut = int(input('Rut (sin puntos ni gion): '))
        res = verificar_rut(rut)
        if not ruts.count(res):
            print("Rut no existe en el sistema")
            break
        if res == False:
            print("Rut invalido")
        else:
            break
        if ruts.count(res):
            index_user = ruts.index(res)
        if dato == 1:
            while True:
                name = str(input("Nuevo nombre: ")).strip().capitalize()
                if not len(name) < 1:
                    users[index_user][1] = name
                    print("Nombre cambiado!")
                    break
                else:
                    print("Ingresa un nombre valido!")
        elif dato == 2:
            while True:
                telefono = int(input('Nuevo numero de telefono: +569'))
                if not len(str(telefono)) != 8:
                    telefono = f"+56 9 {str(telefono)}"
                    users[index_user][2] = telefono
                    print("Telefono Cambiado!")
                    break
                else:
                    print("Telefono invalido")

#print(comprar_asiento("2",asientos))
#print(asientos)

