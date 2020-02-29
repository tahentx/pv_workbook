import pandas as pd
import altair as alt
t = [3,5,2,3,4,2,5,6,7,7,8,2,4,3]
hist = {}
for x in t:
  hist[x] = hist.get(x, 0) + 1
data = pd.DataFrame(list(hist.items()))
