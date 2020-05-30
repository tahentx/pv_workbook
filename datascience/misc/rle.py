# kata: https://www.codewars.com/kata/57d6c3fb950d84fcfb0015c8/train/python
from itertools import groupby
def encode(input):
    freq = [len(list(group)) for key, group in groupby(input)]
    encoded = zip(list(set(input)),freq)
    output = []
    for char in list(input):
        for c in encoded:
            if char == c[0]:
                output.append(char + str(c[1]))
    output = list(set(output))
    output = ''.join(output)
    return output
    
    
    
encode("AAAALOTOOOOFTEEEEXXXXXXT")