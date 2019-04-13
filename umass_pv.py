import pandas as pd
import numpy as np
data = pd.read_csv('umass.csv')
df = pd.DataFrame(data)

# print shape of data
print(df.shape)

# print columns
print(df.columns)

# print general Information about the dataset
print(df.info())
