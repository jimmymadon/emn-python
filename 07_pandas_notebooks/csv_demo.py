import pandas as pd

df = pd.read_csv(
    "/Users/jimmy/Code/VSCodeEMN_2021_Practicals/07_pandas_notebooks/data.csv")

print(df)
print(df.to_string())

print(df.head(10))
