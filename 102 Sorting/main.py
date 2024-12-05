import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 4, 60).reshape(20, 3),
    columns=["One", "Two", "Three"],
    index=[chr(x) for x in range(65, 85)]
)

print(df)

df1 = df.sort_values(by=["One", "Two", "Three"], ascending=False)
print(df1)
print()
df2 = df.transpose()
df2 = df2.sort_values(by=["One", "Two", "Three"], axis=1, ascending=False)
print(df2)