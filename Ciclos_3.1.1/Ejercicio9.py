while True:
    total = 0
    n = int(input("Numero: "))
    if n <= 0:
        print("Numero ti que ser mayor a 0")
    else:
        for i in range(1, n):
            if n % i == 0:
                total += i
    if total == n:
        print(f"Numero Perfecto es: {n}")
    else:
        print(f"Numero No perfecto es: {n}")


