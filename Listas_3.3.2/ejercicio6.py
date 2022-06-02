names = list()
indexs = list()
cont = 1
while True:
    nombre = str(input(f"Nombre {cont}: "))
    names.append(nombre)
    opc = str(input("Desea seguir? Si? No?")).lower()
    if opc == "si":
        cont+=1
    else:
        print("Salir...")
        break
for i in names:
    indexs.append(len(i))
minElement = names.index(min(names))
print(f"Elementos de la lista {names} el elemento borrado fue ({names[minElement]})")
names.pop(minElement)
print(f"Tu lista actuale es: {names}")