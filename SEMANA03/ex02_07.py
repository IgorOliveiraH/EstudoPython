class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = int(codigo)
        self.titulo = titulo
        self.responsavel = responsavel
    
    def __repr__(self):
        return f'{self.codigo}, {self.titulo}, {self.responsavel}'
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._responsavel = valor
    
    def __eq__(self, valor):
        if isinstance(valor, self.__class__):
            return self.codigo == valor.codigo
        return False


projeto1 = Projeto(101, "Desenvolvimento de Software", "Maria Oliveira")
projeto2 = Projeto(101, "Pesquisa em IA", "João Souza")
projeto3 = eval('Projeto(1, "Laboratório de Desenvolvimento de Software", "Pedro Gomes")')

print(projeto1 == projeto2) 