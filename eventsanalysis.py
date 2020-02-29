import pandas as pd

events = pd.read_csv('EventsQ119.csv')
wo = pd.read_csv('WOQ119.csv')
print(wo.describe())
