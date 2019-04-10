import pandas as pd
data = pd.read_csv('umass.csv')
sites = pd.DataFrame(data)
print(sites['Event Type'].unique())
