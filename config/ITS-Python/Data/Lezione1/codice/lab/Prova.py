import pandas as pd

data = {'col_1': [3, 2, 1, 0], 'col_2': [2, 3, 4, 5]}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame.from_dict(data)

print("Data Frame 1")
print(df1)
print("-----------")
print("Data Frame 2")
print(df2)
print("-----------")
print("Data Frame 1 info")
print(df1.info())
print("-----------")
print("Data Frame 2 info")
print(df2.info())