try:
    n = int(input("Numero: "))
    if not (n < 5 or n > 100):
        if n%2 == 0:
            print("Numero par")
        else:
            print("Numero impar")
        for i in range(2,n):
            if n%i == 0:
                print("Es primo")
                break
            else:
                print("No es primo")
                break
    else:
        print("Numero no puede ser menor a 5 o mayor 100")
except ValueError:
    print("Dato invalido")
