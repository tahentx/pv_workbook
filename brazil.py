import pandas as pd
brz = pd.read_csv('sudeste.csv', index_col = 0)
df = pd.DataFrame(brz)
print(df.shape)
