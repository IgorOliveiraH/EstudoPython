arq = open("arquivo.txt","w")

#arq.write() #passar string
#arq.writelines() #passar uma lista
 
arq.write ('Olá,tudo bem?\n')

x = ['caio','joao','marcos']
arq.writelines(x)

arq.close

'''Abrir arquivo por contexto'''
with open("arquivo.txt",'w') as arq:
    arq.write('teste')

    print('fim')