import pandas as pd

df = pd.read_excel("flower_spec.xlsx")

print(df.head(5))
print("Info hai df ka................")
print("Info hai df ka: \n",df.info())