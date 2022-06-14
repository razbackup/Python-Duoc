from func import *
while True:
    print("Menu")
    print("1) Calcular IVA")
    print("2) Descuento")
    print("3) Calcular IMC")
    opc = int(input("Opcion: "))
    if opc == 1:
        producto = int(input("Valor del producto: "))
        print(calcularIva(producto))
    elif opc == 2:
        producto = int(input("Valor del producto: "))
        descuento = float(input("Descuento: "))
        print(calcularDescuento(descuento,producto))
    elif opc == 3:
        peso = int(input("Inserte su peso en KG: "))
        altura = int(input("Inserte su estatura CM: "))
        print(calcularIMC(altura,peso))
    else:
        break

    