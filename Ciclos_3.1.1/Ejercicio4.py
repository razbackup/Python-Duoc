amasado, molde, bague, integral = 0, 0, 0, 0
total = 0
print("""
            Panaderia

        1) Amasado $1.500 
        2) Molde $1.000 
        3) Baguette $2.000 
        4) Integral $3.000 

        9) Pagar!
    """)
while True:
    opc = int(input("Opcion: "))
    if opc == 1:
        amasado = int(input("Cantidad de Amasado: "))
        total = total + (1500 * amasado)
        print(f"Esocjiste {amasado} Amasado")
    elif opc == 2:
        molde = int(input("Cantidad de Molde: "))
        total = total + (1500 * molde)
        print(f"Escojiste {molde} Molde")
    elif opc == 3:
        bague = int(input("Cantidad de Baguette: "))
        total = total + (1500 * bague)
        print(f"Escojiste {bague} Baguette")
    elif opc == 4:
        integral = int(input("Cantidad de Integral: "))
        total = total + (1000 * integral)
        print(f"Escojiste {integral} Integral")
    elif opc == 9:
        if total > 5000:
            envio = "Gratis"
        else:
            envio = int(total * .10)
        print(f"""
            - - - BOLETA - - - 

            Envio: ${(envio)}
            Total a pagar: ${total}
        """)
    else:
        print("Opcion Invalida.")
