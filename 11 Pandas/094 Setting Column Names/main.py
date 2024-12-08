import pandas as pd

df = pd.read_csv('exercises.csv', sep=',', index_col=0)

df.columns = df.columns.str.strip()

print(df.columns)
print(df.head())
