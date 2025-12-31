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


aluno1 = Aluno("2021001", "Ana Paula", "ana.paula@email.com")
aluno2 = Aluno("2021001", "Carlos Silva", "carlos.silva@email.com")

print(aluno1 == aluno2)  

aluno3 = eval('Aluno("SP0101", "João da Silva", "joao@email.com")')
print(aluno3)