def producto(cod,nom,pre,med,prods):
    meds = ["K","U"]
    cods = []
    for i in prods:
        cods.append(i)
    if not len(cod) == 4:
        return "El codigo tiene que ser de 4 digitos"
    elif cod in cods:
        return "Codigo repetido porfavor intentar con otro."
    if not len(nom) > 2:
        return "El nombre tiene que ser mayor de 3 caracteres"
    if not pre > 0:
        return "El precio no puede ser menor a 0"
    if not med in meds:
        return "El tipo de medida no es valido!"
    return [cod,nom,pre,med]
def buscarProducto(cod,prods):
    cods = []
    for i in prods:
        cods.append(i[0])
    if cod in cods:
        index = cods.index(cod)
        print("Codigo encontrado")
        return prods[index]
    else:
        return False

def generarOrden(provedor,cantidad,prods):
    resCantidad = cantidad * prods[2]
    if len(provedor) < 1:
        return False
    elif not cantidad < 1:
        return False
    return [resCantidad,prods]
    