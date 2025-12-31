"""AULA 03 - METODOS DE CLASSE"""

class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    @classmethod # método de classe (não depende da instância)
    def criar_pela_lista(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def criar_pela_string(cls, string):
        base, altura = string.split(",")
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)



retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.criar_pela_lista([20.0, 3.5])
retangulo4 = Retangulo.criar_pela_string("15.0,4.0")

# print(retangulo3.base, retangulo3.altura, retangulo3.calcular_area(), retangulo3.calcular_perimetro())

print(retangulo4.base, retangulo4.altura, retangulo4.calcular_area(), retangulo4.calcular_perimetro())