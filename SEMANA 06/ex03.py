import pandas as pd

df = pd.read_csv("classification_results_trial_0001.csv")
diferente = df["real_class"] != df["predicted_class"]
tabela_de_erros = df[diferente]

print(tabela_de_erros.describe()) 

'''
Os resultados objetidos mostra que o modelo estava super confiante em vários dos seus tabela_de_erros
(perto de 0.5), ele errou com conviccção, chegando a quase 90% de certeza em uma predição incorreta.
'''