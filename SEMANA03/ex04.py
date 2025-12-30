# ex03.py
def linha_para_dict(linha, chaves):
    """Recebe uma linha e uma lista de chaves e retorna um dicionário."""
    valores = linha.strip().split(',')
    
    dicionario = {}
    
    for i in range(len(chaves)):
        if i < len(valores):
            dicionario[chaves[i]] = valores[i].strip()
            
    return dicionario

if __name__ == "__main__":
    linha_teste = "SP000001, Maria da Silva, maria@email.com"
    chaves_teste = ['prontuario', 'nome', 'email']
    
    resultado = linha_para_dict(linha_teste, chaves_teste)
    print("--- Teste Conversão Genérica ---")
    print(resultado)