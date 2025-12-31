""" Aula 06 - Equals e hashcode """

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def __eq__(self, valor): # iguala objetos com mesmos valores de cpf
        if isinstance(valor, self.__class__):
            return self.cpf == valor.cpf
        return False
    
    def __hash__(self): # gera um código único para o objeto baseado no cpf. Para uso em listas, dicionários, etc.
        return hash(self.cpf)

    def __repr__(self):
        return f"Pessoa({self.nome}, {self.cpf})"
        

pessoa1 = Pessoa("Maria da Silva", "123.456.789-00")
pessoa2 = Pessoa("Maria da Silva", "123.456.789-00")
pessoa3 = Pessoa("João Souza", "987.654.321-00")

pessoas = {pessoa1, pessoa2, pessoa3}

print(pessoas)

lista = [pessoa1, pessoa2, pessoa3] # permite elementos duplicados
print(lista)
print(lista.count(pessoa1)) # identifica que pessoa1 e pessoa2 são iguais