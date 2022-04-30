total = 0
liviano,normal,pesado = 0,0,0
while True:
    print("""
    
      |    Kilos     |   Categoria   |   Valor   |
      1)   0 - 5         Liviano         $1000 
      2)   6 - 10        Normal          $4500
      3)   11 - 20       Pesado          $8000

      9) Salir a Pagar
    """)
    opc = int(input("Opcion: "))
    if opc == 1:
        liviano = int(input("Cantidad Livina: "))
        total+= (1000 * liviano)
    elif opc == 2:
        normal = int(input("Cantidad Normal: "))
        total+= (4500 * normal)
    elif opc == 3:
        print("LLeva pesado")
        pesado = int(input("Cantidad Pesado: "))
        total+= 8000 * pesado
    elif opc == 9:
        break
    else:
        print("Invalido..")

print(f"""
        - - - Boleta - - - 
        Cantidad de Liviano: {liviano} 
        Cantidad de Normal: {normal} 
        Cantidad de Pesado: {pesado}

        Total a pagar: ${total} 
    
    """)