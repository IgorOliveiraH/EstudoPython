""" Aula 04 - Propriedades """

# forma de controlar acesso aos atributos de uma instância
# formas personalizadas de obter e alterar o valor do atributo

class Retangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    # getter
    @property
    def base(self):
        return self._base
    
    # setter
    @base.setter
    def base(self, valor):
        if valor <= 0.0:
            raise ValueError("A base deve ser maior que zero.")
        self._base = valor

    # getter
    @property
    def altura(self):
        return self._altura
    
    # setter
    @altura.setter
    def altura(self, valor):
        if valor <= 0.0:
            raise ValueError("A altura deve ser maior que zero.")
        self._altura = valor

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
    
retangulo01 = Retangulo(10.5, 5.0)
retangulo01.base = -1  # alterando diretamente o atributo

print(retangulo01.base, retangulo01.altura)