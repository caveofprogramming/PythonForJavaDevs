import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

df["SpendingGroup"] = pd.cut(df["Spending"], bins=3, labels=(0, 1, 2))
df["GenderCode"] = LabelEncoder().fit_transform(df["Gender"])

y = to_categorical(df["SpendingGroup"])

print(y)

print(df)