import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("classification_results_trial_0001.csv")

#primeiro gráfico (real class)
contagem = df["real_class"].value_counts()
plt.bar(contagem.index, contagem.values)
plt.title("Contagem Real (real_class)")

#nova janela (imprimir os dois graficos)
plt.figure() 


#segundo gráfico (predicted_class)
contagem2 = df["predicted_class"].value_counts()
plt.bar(contagem2.index, contagem2.values)
plt.title("Contagem da IA (predicted_class)")

#terceiro gráfico (prob_benign)
plt.figure()
plt.hist(df["prob_benign"], bins=10, color='green', edgecolor='black')
plt.title("3. Histograma de Probabilidade Benign")

#quarto gráfico (histograma de prob_malign)
plt.figure()
plt.hist(df["prob_malign"], bins=10, color='red', edgecolor='black')
plt.title("4. Histograma de Probabilidade Malign")

#quinto gráfico (acertos vs erros)
plt.figure()
acertos = df[df["real_class"] == df["predicted_class"]]
erros = df[df["real_class"] != df["predicted_class"]]

#sexto grafico (x e o)
plt.scatter(acertos["prob_benign"], acertos["prob_malign"], color='blue', label='Acerto')
plt.scatter(erros["prob_benign"], erros["prob_malign"], color='red', label='Erro', marker='X', s=100)
plt.title("5. Dispersão: Acertos vs Erros")
plt.xlabel("Probabilidade Benign")
plt.ylabel("Probabilidade Malign")
plt.legend()

#setimo grafico (FP OU FN)
FP = ((df["real_class"] == "benign") & (df["predicted_class"] == "malign")).sum()
FN = ((df["real_class"] == "malign") & (df["predicted_class"] == "benign")).sum()

plt.figure()
plt.bar(["Falso Positivo (FP)", "Falso Negativo (FN)"], [FP, FN], color=['orange', 'darkred'])
plt.title("6. Comparação de Erros (FP vs FN)")
plt.ylabel("Quantidade")

plt.show()

'''
 Qual erro é mais comum (FP ou FN)?
Ao analisar o Gráfico 6 gerado pelo código, podemos visualizar que o FN ficou maior

2. E em contexto médico: qual é mais preocupante e por quê?
O Falso Negativo (FN) é o mais preocupante. No contexto de câncer, um Falso Negativo significa
 que o paciente tem um tumor maligno (real malign), mas a IA previu que era benigno
   (predicted benign). Isso faria com que um paciente gravemente doente fosse mandado 
   para casa sem tratamento, o que pode ser fatal. 
'''