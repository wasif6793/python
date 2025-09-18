import numpy as np
import pandas as pd
from pandas import pivot
from typing_extensions import get_origin

df = pd.DataFrame({
    "Name":["Wasif","Amjad",np.nan,"Harsh"],
    "Age":[24,np.nan,23,21],
    "Score":[84,22,np.nan,83]
})


grouped = df.groupby("Name")

for name, group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()

# Aggregation function
df.groupby("Name")["Age"].mean()
df.groupby("Name").agg({"Age":["mean","max","sum"]})

pivott = df.pivot_table(
    values="Age",    #Numeric column
    index="Name",     #Category column
    aggfunc="mean"

)

def range_func(x):
    return x.max() - x.min()

print(df.groupby("Name")["Age"].agg(range_func))

# for mean
print(df.groupby("Name")["Age"].mean())

# Max
print(df.groupby("Name")["Age"].max())

# Multi aggregation
print("Multi Agg: \n",df.groupby("Name").agg({"Age":["mean","max","min"]}))