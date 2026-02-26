import pandas as pd
df = pd.read_csv("classification_results_trial_0001.csv")
imagens_malign = df[df["real_class"] == "malign"]

top5_maiores = imagens_malign.sort_values("prob_benign" , ascending=False ).head(5) #Maior para o menor

print(top5_maiores)