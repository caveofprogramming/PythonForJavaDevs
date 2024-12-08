import pandas as pd

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

print(df.loc[:, "Age":"Spending"].mean())

print(df["Age"].mean())

gp = df.groupby("Gender")

print(gp.mean())
print()
print(gp.mean().loc["Female", "Age"])
