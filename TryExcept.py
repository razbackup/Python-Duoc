# Los controladores de errores Try y Except, son una estructura que permite controlar errores multiples errores al momento de ejecutar el codigo

# Usualmente se usan cuando hay un input porque este esta sujeto a errores.
# Ejemplo
try:
    numero = int(input("Numero: "))
    print(numero)
except ValueError:
    print("Error de Valor")

# Esto si se ingresa un Str,bool o cualquier otro tipo de dato este no lo aceptara y arrojara un error en este caso el error siempre es de Valor.

# luego esta finally que este menciona el fin del try/except (Teniendo o no Errores)
# Ejemplo
try:
    numero = int(input("Numero: "))
    print(numero)
except ValueError:
    print("Error de Valor")
finally:
    print("Fin del Try")


# luego tenemos Raise que es cuando queremos lanzar un error en tal linea y que el codigo si se detenga dando detalles
x = 10
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Luego tenemos raise pero con TyperError que lo que hace esto es que por ejemplo tu le añades un sipo de error.
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")


# En total tendriamos
# Try/Except/finally/raise/raise TypeError