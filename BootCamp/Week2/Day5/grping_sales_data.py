import pandas as pd
import chardet
# chardet is used to detect encoding in python
with open("sales_data_sample.csv", "rb") as f:
    result = chardet.detect(f.read())
print(result)


df = pd.read_csv("sales_data_sample.csv",encoding="latin1")

print("Original data: \n",df)

grped = df.groupby(["PRODUCTLINE","COUNTRY"]).agg({
    "PRICEEACH":"sum",
    "ORDERNUMBER":"count"
})

print("Grpd by order date:\n \n",grped.head())


print("Using Pivot table to find sale per region and per year \n")

pivot = pd.pivot_table(
    df,
    values="PRICEEACH",
    index="COUNTRY",
    columns="SALES",
    aggfunc="sum",
    fill_value=0
)

print(pivot)
