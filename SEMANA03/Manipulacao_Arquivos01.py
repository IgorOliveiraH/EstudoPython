'''Aula 12 - Youtube Aula arquivos em python'''

arquivo = open("teste.txt", "r")

print(arquivo.readable()) #verificar se o arquivo pode ser lido
print(arquivo.read())
print(arquivo.readline()) #ler primeira linha do arquivo

lista = arquivo.readlines() #transformar em lista
print(lista)

arquivo.close()


'''adicionar coisas no arquivo'''

arquivo = open("teste.txt", "a")
arquivo.write ("\nTESTE02")
arquivo.close()


"apagar e começar arquivo novo"

arquivo = open("teste2.txt","w")
arquivo.write ("\nTESTE03")
arquivo.close()