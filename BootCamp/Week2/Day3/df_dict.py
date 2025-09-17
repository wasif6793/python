import pandas as pd

df = pd.DataFrame({"Name":["Wasif","AMjad"],"Age":[24,23],"Batch":["CYbs","BTech"]})
print(df.head())

# New age
df['age_plus_ten'] =  df["Age"] + 10
print(df)

# filtering the data
filtering_row = df[df['age_plus_ten'] >33]
print(filtering_row)

csv_file = filtering_row.to_csv("df_dictcsv.csv")
