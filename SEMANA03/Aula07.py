"""Aula 01  Introdução a orientação a objetos"""

retangulo1 = {
    'base':10.,
    'altura':5.0
}

retangulo2 = {
    'base':6,
    'altura':3
}

#realizar os calculos
def calcular_area(retangulo):
    return retangulo['base'] * retangulo ['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])


print(calcular_area(retangulo1))
print(calcular_area(retangulo2))

print(calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo2))

#Classe representa um conceito
#Esta abaixo representa um retangulo
#classe possui atributos: base e altura
#Clase possui metodos (função dentro da classe)
class Retangulo:
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

#Instanciando objetos do tipo Retangulo
#Chamando o metodo construtor
retangulo1 = Retangulo(10.0,5.0)
retangulo2 = Retangulo(6.0,3.0)

print(type(retangulo1),retangulo1)
print(retangulo1.base,retangulo1.altura)

