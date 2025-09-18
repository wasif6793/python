import pandas as pd
import numpy as np


data = {
    "Class":["A","B","A","C","C","B"],
    "Score":[89,87,76,54,54,76],
    "Age":[23,24,22,25,26,23]
}

df = pd.DataFrame(data)

print("Original data: \n", df)

grped = df.groupby("Class").mean()

print("Grouped: \n",grped)

# Calculate summary stats for grped data

stats = df.groupby("Class").agg(
    {"Score":["mean","max","min"],
    "Age":["mean","max","min"]}
)

print("Statsss: \n",stats)