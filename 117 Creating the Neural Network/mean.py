import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.metrics import Accuracy

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

model = Sequential()
model.add(Dense(200, activation="relu"))
model.add(Dense(100, activation="relu"))
model.add(Dense(3, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=[Accuracy()])

model.fit(X_train, y_train, epochs=30)

y_predicted = model.predict(X_test)