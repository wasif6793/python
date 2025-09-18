#clean a dataset by handling missing values and remaining columns

import pandas as pd
import numpy as np

#create a sample dataset

data = {
    "Name":["Wasif","Amjad",np.nan,"Harsh"],
    "Age":[24,np.nan,23,21],
    "Score":[84,22,np.nan,83]
}

df = pd.DataFrame(data)

print("Original df: \n",df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

df = df.rename(columns={"Name":"Stu_Name", "Score":"Stu_Score"})
print("Dataset: \n", df)