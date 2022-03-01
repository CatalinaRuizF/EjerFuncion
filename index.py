'''import aritmetica as arit
from poo10322.EjerFuncion.text import concat
import text as txt'''

from text import Text
text=Text()

print(text.concat("holasss","-3"))
print(text.contarCaract("c","ca-ce-ci-co-cu"))
print(text.cambiarMayus("coca-cola"))
print (text.cambiarMinus("PEPSI"))
print (text.multiText(6,"*********-------"))
print(text.saludo(" jose"))
print(text.despedida("maria"))
print(text.datos("jesus","300.000.000","3.1416"))

from aritmetica import Math
aritmetica=Math()

print(aritmetica.sumDosNum(2,-3))
print(aritmetica.resDosNum(2,-3))
print(aritmetica.multiDosNum(2,-3))
print(aritmetica.diviDosNum(2,-3))
print (aritmetica.potencia (2,10))
print(aritmetica.perimCuadrado(12))
print(aritmetica.perimRectangulo(12,21))
print(aritmetica.perimCirculo(34))