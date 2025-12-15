""" Aula 04 - Variáveis, Constantes e Literais """

# Variável container para guardar dados
# inferência de tipo

numero = 10
print(numero, type(numero))

# alterar o valor de uma variável
numero = 20
print(numero)

# multiplas atribuições
nome, idade, endereco = 'Maria', 20, 'Rua das ...'
print(nome, idade, endereco)

nome = 'Maria'
idade = 20
endereco = 'rua'

print(nome, idade, endereco)

# atribui o mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# snake_case
id_funcionario = 209
salarioAtual = 5000.50
print(id_funcionario, salarioAtual)

# Constantes
# Upper case - snake_case
PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais
idade = 27
print(idade)
print(27)

# Númericos
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('O filme estava "excelente"')

# Booleano
print(True, type(True))
print(False, type(False))