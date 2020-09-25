# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
# def string_transformer(s):
#     if not s:
#         return ''
#     else:
#         s = s.split()
#         return s
    
# string_transformer("Example string")
# from itertools import count
# import string

# def name_value(my_list):
#     alphabet = list(string.ascii_lowercase)
#     total = []
#     for item in my_list:
#         for letter in item:
#             if letter in alphabet:
#                 total.append(alphabet.index(letter))
#     print(total)   

# name_value(['tee','abb','ass','gee'])

# from itertools import accumulate
# def sum_of_n(n):
#     answer = accumulate([value for value in range(0,n)])
#     print(answer)


# sum_of_n(5)
from collections import Counter
def filter_homogeneous(arrays): 
    for element in arrays: 
        type_counts = Counter(type(x) for x in element)
        if len(type_counts) == 1:
            return element
        else:
            pass
        

filter_homogeneous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]])