class Math(object):
    def sumDosNum(self,n1,n2):
        return n1+n2
    def resDosNum(self,n1,n2):
        return n1-n2
    def multiDosNum(self,n1,n2):
        return n1*n2
    def diviDosNum(self,n1,n2):
        return n1/n2
    #def logaritmo():
    def potencia(self,base, potencia):
        result=base**potencia
        return result
    def perimCuadrado(self,lado):
        result=lado*4
        return result
    def perimRectangulo(self,lado1, lado2):
        result=(lado1+lado2)*2
        return result   
    def perimCirculo(self,radio):
        PI=3.1416
        result=PI*2*radio
        return result
    def fisica(self,n, n1, n2):
        if(n == 1):
            return n1/n2
        elif(n == 2):
            return n1*n2
        else:
            return n2/n1
math1=Math()
print(math1.sumDosNum(2,-7))
math2=Math()
print(math2.resDosNum(5,8))
math3=Math()
print(math3.multiDosNum(5,5))
math4=Math()
print(math4.diviDosNum(82,40))
math5=Math()
print(math5.perimCuadrado(2))
math6=Math()
print(math6.perimRectangulo(4,8))
math7=Math()
print(math7.perimCirculo(5))
math8=Math()
print(math8.fisica(5,4,8))
math9=Math()
print(math9.potencia(16,2))
