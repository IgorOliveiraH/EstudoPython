'''Exercicio pratico S3-A2'''

def dados(nome_arquivo):
    lista_alunos = []
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            
            if len(partes) >= 3:
                dicionario_aluno = {
                    "prontuario": partes[0].strip(),
                    "nome": partes[1].strip(),
                    "email": partes[2].strip()
                }
                lista_alunos.append(dicionario_aluno)
    
    return tuple(lista_alunos)

if __name__ == "__main__":
    try:
        dados = dados("alunos.txt")
        print("--- Dados dos Alunos ---")
        for aluno in dados:
            print(aluno)
    except FileNotFoundError:
        print("Erro: O arquivo 'alunos.txt' não foi encontrado.")