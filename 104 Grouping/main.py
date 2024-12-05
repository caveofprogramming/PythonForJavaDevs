import pandas as pd

df = pd.read_csv("mall_customers.csv", index_col=0)
df.columns = ["Gender", "Age", "Income", "Spending"]

gp = df.groupby("Gender")

print("Number of groups:", gp.ngroups)
print("Groups:", gp.groups)
print("Group keys:", gp.groups.keys())

print(gp.get_group("Female"))
print(type(gp.get_group("Female")))
