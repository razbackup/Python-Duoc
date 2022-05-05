"""
Ingrese un número entero mayor a cero por teclado e indique si es o no “Primo”
"""

while True:
    val = False
    n = int(input(f"Numero: "))
    if n <= 0:
        print("Numero tiene que ser mayor 0")
    else:
        for i in range(2,n):
            if n%i == 0:
                val = True
        if val:
            print("No Primo")
        else:
            print("primo")
