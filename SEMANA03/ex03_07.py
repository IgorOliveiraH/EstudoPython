class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = int(codigo)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    def __repr__(self):
        return f'Aluno({self.prontuario}, {self.nome}, {self.email})'
    
    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor is None or valor == 0:
            raise ValueError("Não devem ser inseridos valores nulos ou iguais a zero")
        self._email = valor

    def __eq__(self, valor):
        if isinstance(valor, self.__class__):
            return self.prontuario == valor.prontuario
        return False

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
    

aluno = Aluno("SP0101", "João da Silva", "joao@email.com")
projeto = Projeto(101, "Desenvolvimento de Software", "Maria Oliveira")
participacao = Participacao(1, "2024-01-15", "2024-06-15", aluno, projeto)

print(participacao.aluno)
print(participacao.projeto)