
def min_value(q, j=3):
  foo = {x: abs(x - j) for x in q}
  minval = min(foo.values())
  return [k for k,v in foo.items() if v == minval]
min_value([4,2,5,7,6])
