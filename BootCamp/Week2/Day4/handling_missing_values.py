import pandas as pd

df= pd.read_csv("")

# Dropping missing values
df= df.dropna()
# df.fillna(method = "ffill")

# filling missing values
df["column_name"] = df["column_name"].fillna(0)

# Interpolation
df['column_name'] = df['column_name'].interpolate()



