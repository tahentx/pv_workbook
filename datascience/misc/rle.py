# kata: https://www.codewars.com/kata/57d6c3fb950d84fcfb0015c8/train/python
from itertools import groupby
def encode(input):
    freq = [len(list(group)) for key, group in groupby(input)]
    encoded = zip(list(set(input)),freq)
    print(encoded)
    
    
encode("AAAALOTOOOOFTEEEEXXXXXXT")