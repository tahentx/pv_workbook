# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
# def string_transformer(s):
#     if not s:
#         return ''
#     else:
#         s = s.split()
#         return s
    
# string_transformer("Example string")

def name_value(my_list):
    z = sum([my_list.index(x) + 1 for x in my_list])
    return z