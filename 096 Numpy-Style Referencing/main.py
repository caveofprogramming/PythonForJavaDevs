import pandas as pd

df = pd.read_csv('exercises.csv', sep=',', index_col=0)
df.columns = df.columns.str.strip()

print(df)

print(df.loc["Mon":"Sun":2])
print(df.loc[["Fri", "Mon"], "Pushups":"Squats"])
print(df.loc[:, "Pushups":"Squats"])

print(df.iloc[:, 1:3])