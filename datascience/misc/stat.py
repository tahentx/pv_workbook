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
     
# def solve(arr):
#     duplicate_arr = sorted(arr)
#     end_result_arr = []
#     while duplicate_arr:
#         end_result_arr.append(duplicate_arr.pop())
#         duplicate_arr.reverse()
#     return end_result_arr


# solve([1,2,33,41,5,62])

def spacey(array):
    new_array = []
    indices = [x for x in range(1, len(array) + 1)]
    for slicer in indices:
        new_array.append(''.join(array[:slicer]))
    print(new_array)




spacey(['i','have','no','space'])