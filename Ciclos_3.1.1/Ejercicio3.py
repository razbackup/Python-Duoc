while True:
    cont = 1
    total = 0
    n = 233
    if n < 103 or n > 987:
        print("Numero Incorrecto")
    else:
        while cont < 3:
            nr = n%10
            n = n//10
            total = ((nr+total) * 10)
            cont+=1
        break
print(int(total)+n)