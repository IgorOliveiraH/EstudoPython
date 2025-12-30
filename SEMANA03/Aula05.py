''' Aula 01 - debug'''

def somar(nota1,nota2,nota3):
    soma = nota1+nota2+nota3
    return soma

def calcular_media(nota1,nota2,nota3):
    soma = somar(nota1,nota2,nota3)
    media = soma/3
    return media

breakpoint()
nota1 = 10.0
nota2 = 3.0
nota3 = 5.5

media = calcular_media(nota1,nota2,nota3)
print (media)