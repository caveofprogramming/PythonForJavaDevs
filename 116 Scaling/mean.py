import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

df["SpendingGroup"] = pd.cut(df["Spending"], bins=3, labels=(0, 1, 2))
df["GenderCode"] = LabelEncoder().fit_transform(df["Gender"])

y = to_categorical(df["SpendingGroup"])

X = df[["Age", "Income", "GenderCode"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.3)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
