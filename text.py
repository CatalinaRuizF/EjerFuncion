def concat(txt1,txt2):
    return txt1+txt2
def contarCaract(c,cadena):
    cont = 0
    for i in cadena:
        if i == c:
            cont = cont + 1
    return cont
def cambiarMinus(cadena):
    return cadena.lower()
def cambiarMayus(cadena):
    return cadena.upper()
def multiText(nVeces, cadena):
    newCadena=nVeces*cadena
    return newCadena

'''def lineaAlinea(cadena):
    for i in cadena:
        newCadena=i
        if i ==' ':
            newCadena=newCadena+"\t"
    return newCadena'''