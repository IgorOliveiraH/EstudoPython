import pandas as pd

df = pd.read_csv("classification_results_trial_0001.csv")

TP = ((df["real_class"] == "malign") & (df["predicted_class"] == "malign")).sum()
print("Verdadeiro Positivos de TP:", TP)

TN = ((df["real_class"] == "benign") & (df["predicted_class"] == "benign")).sum()
print("TN:", TN)

FP = ((df["real_class"] == "benign") & (df["predicted_class"] == "malign")).sum()
print("FP:", FP)

FN = ((df["real_class"] == "malign") & (df["predicted_class"] == "benign")).sum()
print("FN:", FN)

