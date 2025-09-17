import pandas as pd
s = pd.Series([10,20,30], index = ["a","b","c"])
print(s)

data = {"Name":["Wasif","Amjad"], "Age":[24,23]}
df = pd.DataFrame(data)
print(df)

#Load data from csv file
# df = pd.read_csv("data.csv")

# Load data from excel
# df = pd.read_excel("data.xlsx")


# Saving data in csv file
df.to_csv("data.csv")
# if don't want index in it then type: df.to_csv("data.csv", index = False)
df.to_excel("data.xlsx")

# Viewing data

print(df.head())
print(df.tail(3))
print("Info hai")
print(df.info())
print("Describe kiya hai")
print(df.describe())

print("Name and age")
print(df[["Name","Age"]])

print(df[df["Age"]>25])

print("Pehli row by position")
print(df.iloc[0])
print(df.iloc[:,0])
print("Loc hai sirf: \n",df.loc[0])