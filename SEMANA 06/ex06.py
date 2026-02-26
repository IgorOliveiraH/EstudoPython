import pandas as pd
df = pd.read_csv("classification_results_trial_0001.csv")
imagens_benign = df[df["real_class"] == "benign"]

top5_menores = imagens_benign.sort_values("prob_benign").head(5)

print(top5_menores)

'''
Conclusão: Indica que essas 5 imagens são os "casos difíceis" ou as maiores confusões do modelo 
(são os piores Falsos Positivos). Pode ser que a foto esteja com má qualidade, 
ou que esse tumor benigno específico tenha um formato muito esquisito que enganou 
a I.A. Olhar para essas 5 imagens ajudaria o programador a entender os pontos cegos da IA.

'''