import pandas as pd

df = pd.read_csv("")
df2 = pd.read_csv("")
# Renaming the column

df = df.rename(columns={"old_name":"new_name"})

# converting datatypes
df["column_name"] = df["column_name"].astype("float")
df["column_name"] = pd.to_datetime(df["column_name"])

# modifying existing cols
df["new_column"] = df["existing-col"] * 2


combined = pd.concat([df,df2], axis = 0) #combine 2 data frames in rows
combined2 = pd.concat([df,df2], axis = 1)  # combine 2 data frames in cols

merged = pd.merge(df,df2, on="common_column") #merging on a common column

merged2 = pd.merge(df,df2, how = "left", on = "common_column") # left join

merged3 = pd.merge(df,df2, how = "inner", on = "common_column") # inner join

joined = df.join(df2,how = "inner")
