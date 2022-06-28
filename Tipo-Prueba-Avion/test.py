a = 20990720
aux = [i for i in str(a)]
aux.reverse()
values = []
mul = 2
print(aux)
for i in aux:
    if mul == 8:
        mul = 2
    b = mul*int(i)
    print(mul)
    values.append(b)
    mul+=1
print(values)
values = sum(values)
print(values)
res = 11 - (values - ((int(values/11)) * 11))
if res == 11:
    res = 0
if res == 10:
    res = "K"

print(f"{str(a)[0:2]}.{str(a)[2:5]}.{str(a)[5:8]}-{str(res)}")