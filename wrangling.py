import pandas as pd
a7 = pd.read_csv('a7_plantview.csv', index_col = 0)
df = pd.DataFrame(a7)
print(df)
