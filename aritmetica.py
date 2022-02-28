from optparse import Option
from sqlite3 import TimestampFromTicks
from xml.etree.ElementTree import PI


def sumDosNum(n1,n2):
    return n1+n2
def resDosNum(n1,n2):
    return n1-n2
def multiDosNum(n1,n2):
    return n1*n2
def diviDosNum(n1,n2):
    return n1/n2
#def logaritmo():
def potencia(base, potencia):
    result=base**potencia
    return result
def perimCuadrado(lado):
    result=lado*4
    return result
def perimRectangulo(lado1, lado2):
    result=(lado1+lado2)*2
    return result   
def perimCirculo(radio):
    PI=3.1416
    result=PI*2*radio
    return result
def fisica(n, n1, n2):
    if(n == 1):
        return n1/n2
    elif(n == 2):
        return n1*n2
    else:
        return n2/n1
  

