import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

data = np.random.rand(5,5)
sns.heatmap(data,annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()


data = {
    "Class":["A","B","A","C","C","B"],
    "Score":[89,87,76,54,54,76],
    "Age":[23,24,22,25,26,23]
}

df = pd.DataFrame(data)
sns.pairplot(df)
plt.show()