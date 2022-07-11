def factorial(n):
    total = 1
    cont = 2
    while cont <= n:
        total = total * cont
        cont = cont + 1
    return total

def invertir_numero(n):
    valid = n
    while True:
        cont = 2
        total = 0
        while cont-1 < 3:
            n_resto = n%10
            n = n//10
            total = ((n_resto+total) * 10)
            cont = cont + 1
        break
    if valid < 100:
        return (int(total/10))
    else:
        return (int(total)+n)


def solicitar_cantidad_nombres():
    while True:
        try:
            n = int(input("Cantidad de nombres: "))
            if n < 1:
                return 0
            else:
                print("Cantidad de nombres ingresado correctamente")
                return n
        except ValueError:
            print("El dato ingresado es invalido")
        
        
def ingresar_nombres(n,arr):
    cont = 0
    n_user = 1
    while cont < n:
        name = str(input('Nombres: ')).strip().capitalize()
        if len(name) < 1:
            print("El nombre a ingresar tiene que tener almenos 1 caracter")
        else:
            arr.append(name)
            print(f"Nombre numero {n_user} ingresado correctamente.")
            n_user = n_user + 1
            cont+=1
           
    print(f"Los {n} nombres fueron guardados correctamente")
    return arr

def listar(arr):
    return arr


def listar(users):
    if len(users) == 0:
        return 0
    return users
    
        