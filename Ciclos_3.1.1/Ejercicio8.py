n = int(input("Numero: "))
for i in range(1,11):
        print(f"- - - Tabla {i} - - -")
        for x in range(1,11):
            print(f"Numero: {x} X {i}: {x*i}")