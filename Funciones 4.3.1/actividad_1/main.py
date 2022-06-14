stop = True
users = []
import src.functions as fn
while stop:
    try:
        print("1) Crear usuario")
        print("2) Listar Usuarios")
        print("3) Salir")
        opc = int(input("Opcion: "))
        if opc == 1:
            nombre = str(input(f"Nombre: "))
            apellido = str(input("Apellido: "))
            edad = int(input("Edad: "))
            users.append(fn.usuario(nombre,apellido,edad))
            print("Usuario registrado")
        elif opc == 2:
            for i in users:
                print(i)
        stop = False if opc == 3 else True
    except ValueError:
        print("Hay un valor que es erroneo")
