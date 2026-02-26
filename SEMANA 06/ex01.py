import pandas as pd
df = pd.read_csv("classification_results_trial_0001.csv")
contagem = df["real_class"].value_counts()
print(contagem)