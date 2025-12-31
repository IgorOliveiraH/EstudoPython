class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def obter_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
    
    def calcula_pagamento(self):
        return self.salario - (self.salario * 0.1)  

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus
    
    def calcula_pagamento(self):
        return super().calcula_pagamento() + self.bonus

cliente = Cliente("João", "Silva", "123.456.789-00")
print(cliente.obter_nome_completo())

funcionario = Funcionario("Maria", "Souza", "987.654.321-00", 5000.0)
print(funcionario.obter_nome_completo())
print(funcionario.salario)
print(funcionario.calcula_pagamento())

programador = Programador("Ana", "Oliveira", "111.222.333-44", 7000.0, 1500.0)
print(programador.calcula_pagamento())