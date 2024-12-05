import pandas as pd

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

df_filtered = df[(df['Gender'] == 'Female') & (df['Age'] > 40)]

print(df_filtered)