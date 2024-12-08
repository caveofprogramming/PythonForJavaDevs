import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.cluster import KMeans

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

model = KMeans(n_clusters=2)

X = df[["Age", "Spending"]]
model.fit(X)

df["Cluster"] = model.labels_

sn.scatterplot(df, x="Age", y="Spending", palette="husl", hue="Cluster")
plt.show()