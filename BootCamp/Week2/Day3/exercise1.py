import pandas as pd
#Loading dataset

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore the structure
print("Printing first 5 rows: \n", df.head(5))
print("Printing last 5 rows: \n", df.tail(5))

print(df.info())
