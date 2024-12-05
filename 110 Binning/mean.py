import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

df["SpendingGroup"] = pd.cut(df["Spending"], bins=3, labels=(0, 1, 2))

print(df)