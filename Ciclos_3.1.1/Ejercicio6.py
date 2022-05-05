texto = "hola"
vocales = "aeiou"
vocal,conosonante = 0,0
for i in texto:
    if i in vocales:
        vocal+=1
    else:
        conosonante+=1

print(f"""
Cantidad de Vocales: {vocal}
Cantidad de Consonante: {conosonante}
""")