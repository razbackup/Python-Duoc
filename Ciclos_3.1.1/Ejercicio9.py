from __future__ import barry_as_FLUFL


while True:
    total = 0
    val = False
    n = int(input("Numero: "))
    if n <= 0:
        print("Numero tiene que ser mayor a 0")
    else:
        for i in range(1, n):
            if n % i == 0:
                total += i
    if total == n:
        print(f"Numero Perfecto es: {n}")
    else:
        print(f"Numero No perfecto es: {n}")


