import pandas as pd

df = pd.read_csv("classification_results_trial_0001.csv")
diferente = df["real_class"] != df["predicted_class"]
tabela_de_erros = df[diferente]
print(tabela_de_erros)