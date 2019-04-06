import pandas as pd
events = pd.read_csv('jspevents.csv')
df = pd.DataFrame(events)
print(type(df))
