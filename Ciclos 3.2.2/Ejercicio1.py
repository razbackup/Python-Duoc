vocales = "aeiou"
frase = str(input("Palabra: "))
cont = 0
for i in frase:
    for x in vocales:
        if i == x:
            cont+=1

if cont <= 2:
    print("Perdiste")
elif cont >= 3 and cont <= 5:
    print("Casi ganas!")
else:
    print("Ganaste!!")
