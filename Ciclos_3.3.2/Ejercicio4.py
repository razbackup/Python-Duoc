lista = list()
word = str()
cont = 1
while cont < 4:
    try:
        nombre = str(input(f"Nombre numero {cont}: "))
        lista.append(nombre)
        cont+=1
    except:
        print("Invalido.")
for i in lista:
    if len(i.strip()) > len(word.strip()):
        word = i
print(f"Nombre mas largo: {word}")
