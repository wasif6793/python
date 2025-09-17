import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

selected_cols = df[["species","sepal_length"]]
print(selected_cols)
df.to_csv("flower_species.csv")
df.to_excel("flower_spec.xlsx")
# Filtering the rows
filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered Rows: \n",filtered_rows)