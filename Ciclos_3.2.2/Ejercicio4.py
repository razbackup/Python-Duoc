user1,user2,user3 = None,None,None
pass1,pass2,pass3, = None,None,None
while True:
    try:
        print("""
        1. Iniciar Sesión
        2. Registro de Usuario.
        3. Salir
        """)
        opc = int(input("Opcion: "))
        if opc == 1:
            if (user1 == None and user2 == None and user3 == None) and (pass1 == None and pass2 == None and pass3 == None):
                print("No Existen Usuarios!")
            elif  user1 != None and pass1 != None or user2 != None and pass2 != None or user3 != None and pass3 != None:
                try:
                    loginUser = str(input("Usuario: "))
                    loginPass = str(input("Contraseña: "))
                    while True:
                        if user1 == loginUser and pass1 == loginPass:
                            get = True
                            break
                        elif user2 == loginUser and pass2 == loginPass:
                            get = True
                            break
                        elif user3 == loginUser and pass3 == loginPass:
                            get = True
                            break
                        else:
                            print("Intente Nuevamente...")
                            get = False
                            break
                except ValueError:
                    print("Dato No valido!")
                if get:
                    print(f"Bienvenido: {loginUser}")
                    while True:
                        print("""
                            - - - Que te gustaria hacer? - - -
                            1) Realizar llamada
                            2) Enviar Correo
                            3) Cerrar Sesion                    
                        """)
                        opc = int(input("Selecciona: "))
                        if opc == 1:
                            while True:
                                try:
                                    number = int(input("Ingresa tu numero: "))
                                    for i in str(number):
                                        if i != "9":
                                            print("Tiene que empezar con 9!")
                                            noNumber = False
                                            break
                                        else:
                                            noNumber = True
                                            break
                                    if noNumber:
                                        if number < 900000000 or number > 999999999:
                                            print("Tu numero no esta correcto!, Intenta denuevo!")
                                        else:
                                            print("Numero escrito correctamente!")
                                            break
                                    else:
                                        print("Intenta denuevo!")
                                except ValueError:
                                    print("Dato Invalido..")
                        elif opc == 2:
                            while True:
                                valueCorreo = False
                                try:
                                    correo = str(input("Correo: "))
                                    for i in correo:
                                        if i == "@":
                                            valueCorreo = True
                                            break
                                    if valueCorreo:
                                        print("Correo Guardado correctamente!")
                                    else:
                                        print("Correo Invalido!")
                                except ValueError:
                                    print("Dato Invalido..")
                        elif opc == 3:
                            print("Cerrando Sesion!.")
                            break
                        else:
                            print("Opcion invalida..")
                else:
                    print("Usuario no Encontrado!.")

        elif opc == 2:
            while True:
                try:
                    if user1 == None and pass1 == None:
                        user1 = str(input("Registra Usuario: "))
                        pass1 = str(input("Registra Constraseña: "))
                        if user1 == "" or pass1 == "":
                            print("No puede haber un campo vacio")
                            user1 = None
                            pass1 = None
                        else:
                            print("Registrado con exito")
                            break
                    elif user2 == None and pass2 == None:
                        user2 = str(input("Registra Usuario: "))
                        pass2 = str(input("Registra Constraseña: "))
                        if user2 == "" or pass2 == "":
                            print("No puede haber un campo vacio")
                            user2 = None
                            pass2 = None
                        else:
                            print("Registrado con exito")
                            break
                    elif user3 == None and pass3 == None:
                        user3 = str(input("Registra Usuario: "))
                        pass3 = str(input("Registra Constraseña: "))
                        if user3 == "" or pass3 == "":
                            print("No puede haber un campo vacio")
                            user3 = None
                            pass3 = None
                        else:
                            print("Registrado con exito")
                            break
                    else:
                        print("Ops, usuarios llenos no queda para registrar.")
                except ValueError:
                    print("Dato Invalido")
        elif opc == 3:
            print("Saliendo....")
            break
        else:
            print("Invalid...")
    except ValueError:
        print("Dato invalido")