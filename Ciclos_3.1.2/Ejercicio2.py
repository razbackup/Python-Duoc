frase = str(input("Frase: ")).strip()
cont = 0
for i in frase:
    if i == " ":
        cont+=1

if frase.strip() == "":
    print(cont)
else:
    print(cont+1)