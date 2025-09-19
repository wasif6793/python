import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Inspect
print(df.info())
print(df.describe())


# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna((df["Embarked"].mode()[0]))

# Remove duplicates
df = df.drop_duplicates()

# Filter data: Passangers in first class
first_class = df[df["Pclass"] == 1]
print("First class PAssangers: \n", first_class)

survivalbyclass = df.groupby("Pclass")["Survived"].mean()
survivalbyclass.plot(kind="bar", color = "skyblue")
plt.title("Survival rate by class")
plt.ylabel("Survival rate")
plt.show()

# Histogram: Age distribution
sns.histplot(df["Age"],kde=True,bins = 20, color = "Blue")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Freq")
plt.show()

# Scatterplot: Age vs fare
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color ="green")
plt.title("Age vs fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()