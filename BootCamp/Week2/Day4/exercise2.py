import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Wasif","Harsh","Amjad"],
    "Age":[23,24,25]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Score":[80,90,70]
})

print("Dataset 1: \n",df1)
print("Dataset 2: \n",df2)

merged = pd.merge(df1,df2, how ="inner",on ="ID")
print("Merged ds: \n",merged)


merged["Score_percent"] = (merged["Score"] / 100) * 100
print("Transformed Dataset \n", merged)
