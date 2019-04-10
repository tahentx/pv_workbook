import pandas as pd
import numpy as np
data = pd.read_csv('umass.csv')
sites = pd.DataFrame(data)

# print column headers
for x in data :
    print(x)
