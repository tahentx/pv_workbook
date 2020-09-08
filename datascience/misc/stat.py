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
    total = []
    for item in my_list:
        for letter in item:
            if letter in alphabet:
                total.append(alphabet.index(letter))
    print(total)   

name_value(['tee','abb','ass','gee'])