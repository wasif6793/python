import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
del df['species']

#  correlation matrix calculation
corr_mat = df.corr()

# plot heatmap
sns.heatmap(corr_mat,annot=True,cmap="coolwarm")
plt.title("Seabron ka plot")
plt.show()