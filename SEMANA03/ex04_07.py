class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = int(codigo)
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []
    
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

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)
    

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, projeto):
        self.codigo = int(codigo)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.projeto = projeto


projeto = Projeto(101, "Desenvolvimento de Software", "Maria Oliveira")
participacao1 = Participacao(1, "2024-01-15", "2024-06-15", projeto)
participacao2 = Participacao(2, "2024-02-01", "2024-07-01", projeto)

projeto.add_participacao(participacao1)
projeto.add_participacao(participacao2)

for i in projeto.participacoes:
    print(i.codigo, i.data_inicio, i.data_fim)  