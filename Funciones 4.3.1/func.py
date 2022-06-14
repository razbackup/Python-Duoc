def calcularIva(valor):
    return f"Valor de IVA aplicado {int(valor*0.19)} iva agregado al producto: {int(valor + (valor*0.19))}"
def calcularDescuento(desc,valor):
    a = valor*(desc/100)
    total = valor - a
    return total
def calcularIMC(altura,peso):
    imc = round(peso/altura**2 * 10000,1)
    if imc < 18.5:
        return f"su imc es de {imc} y usted esta en bajo peso"
    elif imc > 18.5 or imc < 24.9:
        return f"su imc es de {imc} y usted esta en peso adecuado"
    elif imc > 25.0 or imc < 29.9:
        return f"su imc es de {imc} y usted esta en peso adecuado"
    elif imc > 30.0 or imc < 34.9:
        return f"su imc es de {imc} y usted esta en Obesidad grado 1"
    elif imc > 35.0 or imc < 39.9:
        return f"su imc es de {imc} y usted esta en Obesidad grado 2"
    elif imc > 40:
        return f"su imc es de {imc} y usted esta en Obesidad grado 3"

        

