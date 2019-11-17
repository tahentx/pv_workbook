
def min_value(q):
  j = 3
  foo = {x: abs(x - j) for x in q}
  print(min(foo, key=foo.get))
min_value([4,2,5,7,6])
