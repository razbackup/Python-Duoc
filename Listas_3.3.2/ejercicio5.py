names = list()
lastNames = list()
sortNames = []
for i in range(3):
    name = str(input(f"Nombre {i+1}: ")).capitalize()
    lastName = str(input(f"Apellido {i+1}: ")).capitalize()
    names.append(name)
    lastNames.append(lastName)
    auxComplete = f"{name} {lastName}"
    sortNames.append(auxComplete) 
lastNames.sort()
names.sort()
sortNames.sort()
print(f"Nombres: {names} Apellidos: {lastNames}")
for i in sortNames:
    print(i)