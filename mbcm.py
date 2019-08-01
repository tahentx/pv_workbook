import altair as alt
import pandas as pd
import numpy as np


df = pd.read_csv('mbcm.csv')

B = df['Billable']

#
# source = pd.DataFrame({
#     'a': ['Billable', 'Not Billable', 'Unknown'],
#     'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
# })

# alt.Chart(source).mark_bar().encode(
#     x='a',
#     y='b'
# )
