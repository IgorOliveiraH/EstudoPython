"""Aula 05 - Métodos Especiais"""

# __str__(self): representação em string do objeto, para usuário 
# __repr__(self): representação canônica do objeto
    # usado para depuração, logging, etc.

class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f'Retangulo[base: {self.base}, altura: {self.altura}]'
    
    def __repr__(self):
        return f'Retangulo({self.base}, {self.altura})'
    
retangulo1 = Retangulo(10.0, 5.0)
print(retangulo1)  # chama o método __str__() implicitamente

retangulo3 = eval('Retangulo(15.0, 7.5)')
retangulo4 = eval(repr(retangulo3))

rep_string_retangulo = 'Retangulo(15.0, 7.5)'
print(retangulo1.__repr__())  
print(retangulo3)
print(retangulo4)