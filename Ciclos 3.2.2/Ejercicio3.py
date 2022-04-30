menor,adulto,adultoMayor,total = 0,0,0,0
print("""
   | Cliente       Intervalos                          Precio | 
1) | Menores       Mayores a 7 años y menores que 12   $4000  |
2) | Adultos       Desde los 12 años hasta los 65      $7000  |
3) | Adulto Mayor  Desde los 65 años                   $3000  |
""")
while True:
    print("""
    1).- Ingresar Compra
    2).- Salir
    """)
    opc = int(input("Opcion: "))
    if opc == 1:
        pp = int(input("Tipo de entrada: "))
        if pp == 1:
            menor = int(input("Cantidad: "))
            total+=(4000*menor)
        elif pp == 2:
            adulto = int(input("Cantidad: "))
            total+=(7000*adulto)
        elif pp == 3:
            adultoMayor = int(input("Cantidad: "))
            total+=(3000*adultoMayor)
        else:
            print("Invalid...")
    elif opc == 2:
        break
    else:
        print("Invalid...")

print(f"""
    - - - Boleta - - -
    Entradas de Menores: {menor}
    Entradas de Mayores: {adulto}
    Entradas de Adultos mayores: {adultoMayor}

    Total ${total}
""")