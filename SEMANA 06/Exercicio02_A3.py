import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metrics.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) #1 linha, 2 colunas (largura 12, altura 5)

#grafico 1: accuracy
ax1.plot(df.index, df["train_acc"], label="train")
ax1.plot(df.index, df["val_acc"], label="valid")
ax1.set_title("model accuracy")
ax1.set_ylabel("accuracy")
ax1.set_xlabel("epoch")
ax1.legend(loc="upper left") 

#grafico 2: loss
ax2.plot(df.index, df["train_loss"], label="train")
ax2.plot(df.index, df["val_loss"], label="valid")
ax2.set_title("model loss")
ax2.set_ylabel("loss")
ax2.set_xlabel("epoch")
ax2.legend(loc="upper left")

plt.tight_layout()
plt.show()