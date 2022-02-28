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
def saludo(nombre):
    return 'hola ', nombre, ' como estas?'
def despedida(nombre):
    return 'Adios ', nombre, ' nos vemos pronto'
def datos(nombreCompleto, id, codigo):
    return 'tu nombre es: ', nombreCompleto, ' tu numero de identificacion es: ', id, ' y tu codigo es: ', codigo 
