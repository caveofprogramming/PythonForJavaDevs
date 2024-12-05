import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(0, 4, 60).reshape(20, 3),
    columns=["One", "Two", "Three"],
    index=[chr(x) for x in range(65, 85)]
)

print(df)