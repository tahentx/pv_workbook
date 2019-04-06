import pandas as pd
events = pd.read_csv('jspevents.csv', index_col="Plant")
df = pd.DataFrame(events)
print(df)
