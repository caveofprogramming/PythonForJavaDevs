import pandas as pd

df = pd.read_csv('exercises.csv', sep=',', index_col=0)
df.columns = df.columns.str.strip()

df.at['Tue', 'Pushups'] = 40

print("Monday squats", df.iat[0, 2])

print(df)
