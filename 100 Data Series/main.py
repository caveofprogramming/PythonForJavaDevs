import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['Dogs', 'Cats', 'Mice'],
    index=['Meat', 'Fish', 'Vegetables'],
)

cats = df['Cats']

print(list(cats.index))
print(type(cats.values))

