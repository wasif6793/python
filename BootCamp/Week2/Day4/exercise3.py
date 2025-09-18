import pandas as pd
import numpy as np
data = {
    "Name":["Wasif","Amjad",np.nan,"Harsh"],
    "Age":[24,np.nan,23,21],
    "Score":[84,22,np.nan,83]
}
data1 = {
    "Name":["Aman","Rohit","Anurag",np.nan],
    "Age":[20,np.nan,21,22],
    "Score":[22,12,10,np.nan]
}

data2 = {
    "Name":["Amit","Rohan","Anu","Rohila"],
    "Age":[np.nan,25,21,22],
    "Score":[np.nan,10,100,99]
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df)
print(df1)
print(df2)
print("End.....\n")
mergeing_dataframes = pd.concat([df,df1,df2],ignore_index=True)
print(mergeing_dataframes)

clean_data = mergeing_dataframes.loc[:,mergeing_dataframes.isnull().mean() <= 0.3]
print(clean_data)