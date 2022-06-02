from numpy import *
def numeroPrimo(n):
    flag = False
    for i in range(2,n):
            if n%i == 0:
                flag = True
    if flag:
        return f"{n} No primo"
    else:
        return f"{n} Primo"
def factorial(n):
    return f"Factorial del numero {n}: {array([i*n for i in range(1,n)]).sum()} "
def palindrome(w):
    arr = [i for i in w]
    arr.reverse()
    return f"Es palindrome {w}" if w == "".join(arr) else f"No es palindrome {w}"
while True:
    print("Menu")
    print("1) Numero Primo")
    print("2) Factorial")
    print("3) Palindrome")
    print("4) Salir")
    opc = int(input("Opcion: "))
    if opc == 1:
        n = int(input("Numero: "))
        print(numeroPrimo(n))
    elif opc == 2:
        numero = int(input("Ingrese un numero: "))
        print(factorial(numero))
    elif opc == 3:
        palabra = str(input("Palabra: "))
        print(palindrome(palabra))
    elif opc == 4:
        quit()