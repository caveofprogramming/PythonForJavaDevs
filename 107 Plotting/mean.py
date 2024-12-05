import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

plt.figure(figsize=(16,9))
plt.grid(True)
plt.title("Age vs Spending")
plt.xlabel("Age")
plt.ylabel("Spending")

plt.scatter(df["Age"].values, df["Spending"].values, color="green")
plt.show()