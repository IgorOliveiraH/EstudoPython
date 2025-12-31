""" Aula 07 - Relacionamento entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[CEP: {self.cep}, Numero: {self.numero}]'

    
    def __str__(self):
        return f'Endereco[{self.cep}, {self.numero}]'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    
    def __str__(self):
        return f'Telefone[({self.ddd}) {self.numero}]'

class Pessoa:
    def __init__(self, cpf,  nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []


    def add_endereco(self, endereco):
        self.enderecos.append(endereco) 

    def print_enderecos(self):
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[CPF: {self.cpf}, Nome: {self.nome}, Telefone: {self.telefone}, Enderecos: {self.enderecos}]'
    

pessoa = Pessoa("123.456.789-00", "Maria da Silva", Telefone("11", "98765-4321"))
pessoa.add_endereco(Endereco("01001-000", 100))
pessoa.add_endereco(Endereco("02002-000", 200))
pessoa.print_enderecos()

print(pessoa)
print(pessoa.telefone.ddd, pessoa.telefone.numero)