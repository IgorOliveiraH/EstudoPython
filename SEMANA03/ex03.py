# ex02.py
def dados(nome_arquivo):
    lista_projetos = []
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            
            if len(partes) >= 3:
                dicionario_projeto = {
                    "codigo": int(partes[0].strip()), # Convertendo para inteiro
                    "titulo": partes[1].strip(),
                    "responsavel": partes[2].strip()
                }
                lista_projetos.append(dicionario_projeto)
                
    return tuple(lista_projetos)

if __name__ == "__main__":
    try:
        dados = dados("projetos.txt")
        print("--- Dados dos Projetos ---")
        for projeto in dados:
            print(projeto)
    except FileNotFoundError:
        print("Erro: O arquivo 'projetos.txt' não foi encontrado.")