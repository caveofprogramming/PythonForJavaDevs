import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

sn.pairplot(df, height=2, aspect=1, palette="husl", hue="Gender")

plt.show()
