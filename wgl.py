import pandas as pd
import numpy as np
import matplotlib as plt

maint = pd.read_csv('wgl_wo_6.25.csv', index_col='Plant Name')
print(maint)
