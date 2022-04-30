user1,user2,user3 = None,None,None
pass1,pass2,pass3, = None,None,None
while True:
    print("""
    1. Iniciar Sesión
    2. Registro de Usuario.
    3. Salir
    """)
    opc = int(input("Opcion: "))
    if opc == 1:
        if (user1 == None and user2 == None and user3 == None) and (pass1 == None and pass2 == None and pass3 == None):
            print("No Existen Usuarios!")
        elif  (user1 == None or user2 == None or user3 == None) and (pass1 == None or pass2 == None or pass3 == None):
            loginUser = str(input("Usuario: "))
            loginPass = str(input("Contraseña: "))
            for i in user1 and user2 and user3:
                pass

    elif opc == 2:
        if user1 == None and pass1 == None:
            user1 = str(input("Registra Usuario: "))
            pass1 = str(input("Registra Constraseña: "))
        elif user2 == None and pass2 == None:
            user2 = str(input("Registra Usuario: "))
            pass2 = str(input("Registra Constraseña: "))
        elif user3 == None and pass3 == None:
            user3 = str(input("Registra Usuario: "))
            pass3 = str(input("Registra Constraseña: "))
        else:
            print("Ops, usuarios llenos no queda para registrar.")
    elif opc == 3:
        print("Saliendo....")
        break
    else:
         print("Invalid...")