# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
# def string_transformer(s):
#     if not s:
#         return ''
#     else:
#         s = s.split()
#         return s
    
# string_transformer("Example string")
from itertools import count
import string

def name_value(my_list):
    alphabet = list(string.ascii_lowercase)
    for item in my_list:
        if ' ' in item:
            item = item.split()
            for subitem in item:
                my_list.append(subitem)
        if item in alphabet:
            item = alphabet.index(item) + 1
            print(item)
    # list_total = sum([my_list.index(x) + 1 for x in my_list])

name_value(['t','a','a','g'])