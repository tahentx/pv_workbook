import pandas as pd
import numpy as np

# Create new storerooms
df = pd.DataFrame(
    {"Storeroom ID" : ["Service Truck 20","Service Truck 34"]}
)

# Assign CJ as default buyer
for x in df:
    df["Default Buyer"] = 'CJ Kneringer'

# Write data to CSV
df.to_csv('storerooms.csv',sep='\t', encoding='utf-8')

inventory = pd.read_csv('mbs_servicetrucks_01.csv')
inventory['Storeroom Record ID'] = 'a0O1M00000sCL52UAG'
