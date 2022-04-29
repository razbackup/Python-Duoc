# los ciclos en python son muy facil de usar y entender
# Tenemos que entender que un bucle principalmente sirve para repetir una seccion de codigo
# Esto su objetivo es no repetir mas codigo del que ya usamos y usarlo cuantas veces queramos

# Primero tenemos el bucle (for) este tipo de bucle nos sirve para recorrer listas,Diccionarios o Rangos
# Su estructura esta compuesta por la palabra for (para o por) luego de una variable local que seria (i) y luego por donde queremos que la variable itere con in (en) y la lista o el rango

for i in range(0,10+1):
    print(i)

# Es importante saber que en caso de un rango, i solo sera 9 porque porque el elemento o numero 10 es donde frena y al momento que sea 10 el bucle no continuara en ese caso hay que usar un +1 o un numero mas

# De esta manera tenemos numeros de 1 al 10 en i ya que i es una variable que cambiara 10 veces tenienen 1 2 3 4 5 6 7 8 9 10.

# Ejemplo con una lista.
lista = ["elemento 1","elemento 2",True,200,600,("idk",True)]
for i in lista:
    print(i)
    print(type(i))

# Lo que poseemos aqui es principalmente una lista llena de elementos estos pueden ser bool,str,int o cualquiera en este caso tenemos str,int,bool y tuples

# Caracteristica que diferencia a for de while es que for solo recorrerar los elementos que tengamos y luego frenara, a diferencia de while que hay que condicionarlo para que frene

# While, este tipo de bucles si se usa para repetir un codigo determinada veces
while True:
    print("1) Si, 2) No")
    opc = int(input("Quieres que se repita: ? "))
    if opc == 1:
        print("Si repite!")
    elif opc == 2:
        print("Okey Adios")
        break
    else:
        print("Invalid..")

# Como vemos tenemos un While (Mientras) True (Verdadero) Mientras sera verdadero, se ejecutara todo el codigo que este dentro de la estructura, en esta tiene una condicional donde 1 hace continuar el bucle mientras que la opcion dos lo detiene usando break que break se usa principalmente para eso para cortar bucles

# Tambien podemos usar como condicional el while.

cont = 0
while cont <= 10:
    print(f"Hola soy el numero: {cont}")
    cont+=1

# En este ultimo bucle tenemos un contador que incrementa hasta que cumple la condicion del While
# y este se repetira tantas veces se incremente.
