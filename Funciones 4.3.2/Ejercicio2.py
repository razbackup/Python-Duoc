# 0 1 1 2 3 5 8 13
def fibonaccci(num):
    cont = 0
    total = 0
    while cont <= num:
        total+=cont
        cont+=1
    return f"La serie Fibonacci es {total}"

n = int(input("Numero: "))
print(fibonaccci(n))
