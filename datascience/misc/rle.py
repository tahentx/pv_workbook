# kata: https://www.codewars.com/kata/57d6c3fb950d84fcfb0015c8/train/python
# from itertools import groupby
# def encode(input):
#     freq = [len(list(group)) for key, group in groupby(input)]
#     encoded = zip(list(set(input)),freq)
#     output = []
#     for char in list(input):
#         for c in encoded:
#             if char == c[0]:
#                 output.append(char + str(c[1]))
#     output = list(set(output))
#     output = ''.join(output)
#     return output
    
    
    
# encode("AAAALOTOOOOFTEEEEXXXXXXT")
vows = {
    'a' : 1,
    'e' : 2,
    'i' : 3,
    'o' : 4,
    'u' : 5,
}

def encode(st):
    st = list(st)
    output = []    
    for val in st:
        if val in vows.keys():
            output.append(vows.get(val))
        else:
            output.append(val)
    print(output)
# encode('hello')

def decode(st):
    # key_extract = [k for k, v in vows.items() if v in list(st)]
    st = list(st)
    for k,v in vows.items():
        v = str(v)
        for char in st:
            if v in st:
                st = st.replace(char,k)
            print(st)
decode("h2ll4")
