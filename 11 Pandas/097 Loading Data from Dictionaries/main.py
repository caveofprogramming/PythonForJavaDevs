import pandas as pd

data = {
    "Mon":[1, 2, 3],
    "Tue":[0.1, 0.2, 0.3],
    "Wed":[5, 6, 7],
}

df = pd.DataFrame(data)
print(df)