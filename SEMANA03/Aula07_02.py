"""Aula 02 - Atributos de classe e instancia"""

#Classe pessoa possui atributos de instancia (nome e email)
#atributos de classe: especie
class Pessoa:
    especie = 'Humano'
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa('Maria da silva', 'maria@email.com')
pessoa2 = Pessoa('Joao santos', 'joao@email.com')

#Alterar um atributo de classe na instancia(objeto),aletra somente naquela instancia
pessoa1.especie = 'Alienigena'

#Muda todos os objetos, mudando um atributo de classe na classe
Pessoa.especie = 'Veiculos voadores'

print(pessoa1.nome,pessoa1.email,pessoa1.especie)
print(pessoa2.nome,pessoa2.email,pessoa2.especie)

print(Pessoa.especie)