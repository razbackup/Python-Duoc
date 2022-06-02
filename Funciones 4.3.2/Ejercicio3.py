def calcularDigito(rut):
    if not len(str(rut)) == 8:
        return "El rut tiene que contener 8 digitos / el rut no puede contener guion!"
    else:
        arr = [i for i in str(rut)]
        arr.reverse()
        cont = 2
        res = 0
        for i in arr:
            cont = 2 if cont == 8 else cont
            res+=int(i)*cont
            cont+=1
        digito = 11-(res-(int(res/11)*11))
        if digito == 11:
            digito = 0
        elif digito == 10:
            digito = "K"
        arr.reverse()
        arr.append("-")
        arr.append(str(digito))
    return "".join(arr)

# n = int(input("Rut sin digito: "))
n = int(input("Rut sin guion: "))
print(calcularDigito(n))

