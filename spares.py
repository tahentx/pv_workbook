import pandas as pd
import numpy as np

# Create new storerooms
df = pd.DataFrame(
    {"Storeroom ID" : ["Service Truck 20","Service Truck 34"]}
)

for x in df:
    df["Default Buyer"] = 'CJ Kneringer'

print(df)
