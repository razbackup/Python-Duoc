
cont,nombres,apellidos = 1,list(),list()
while True:
    try:
        while cont < 4:
            nombre = str(input(f"Nombre numero {cont}: "))
            apellido = str(input(f"Apeliido {cont}: "))
            if nombre.strip() == "" or apellido.strip() == "":
                print("No puede haber un campo vacio!")
            else:
                nombres.append(nombre.capitalize())
                apellidos.append(apellido.capitalize())
                cont+=1
        break
    except ValueError:
        print("Invalido.")

sync = [[nombres[0],apellidos[0]],[nombres[1],apellidos[1]],[nombres[2],apellidos[2]]]
sync.sort()
for i in sync:
    for x in i:
        print(x)
        