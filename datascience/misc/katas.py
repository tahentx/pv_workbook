# def string_letter_count(s):
#     from collections import Counter
#     from operator import itemgetter
#     cnt = Counter()
#     bad = [',' ,'.' ,'{', '}','[', ']', ' ']
#     for word in s.lower():
#         if word in bad:
#             pass
#         else:
#             cnt[word] += 1
#     cnt = dict(cnt)
#     sorted_cnt = sorted(cnt.items(), key=itemgetter(0))
#     reordered = [x[::-1] for x in sorted_cnt]
#     t = []
#     for x in reordered:
#         f = str(x[0])
#         t.append(f)
#         t.append(x[1])
#     answer = ''.join(t)
#     return answer

# string_letter_count("This is a test sentence")

# def sum_even_numbers(seq):
#     return sum(list(filter(lambda x: x % 2 == 0, seq)))
    
# sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# def pyramid(n):
#     container = []
#     while n > 0:
#         g = [1 for _ in range(n)]
#         container.append(g)
#         n -= 1
#     container = container[::-1]
#     return container

# pyramid(5)

# 003def letter_frequency(text):
#     from collections import Counter
#     from operator import itemgetter
#     cnt = Counter()
#     lst = list(text.lower().replace(" ",""))
#     for l in lst:
#         cnt[l] += 1
#     ordered = sorted(cnt.items(), key=itemgetter(1,0), reverse=True)
#     return ordered
    
    
# letter_frequency("aaAabb dddDD hhcc")

# def decipher_this(string):
#     x = string.split()
#     phrase = []
#     for string in x:
#         target = min([string.index(x) for x in string if not x.isdigit()])
#         nums, chars = int(string[:target]),list(string[target:])
#         first, body, last = chars[0], ''.join(chars[1:-1]), chars[-1]
#         to_join = [chr(nums),last,body,first]
#         output = ''.join(to_join)
#         phrase.append(output)
#     phrase = ' '.join(phrase)
#     print(phrase)    
    
# decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")

# def reverse_alternate(string):
#     clean_string = string.strip().split()
#     output = []
#     for word in clean_string:
#         if clean_string.index(word) % 2 != 0:
#             word = word[::-1]
#             output.append(word)
#         else:
#             output.append(word)
#     output = ' '.join(output)
#     return output
# reverse_alternate(" I really hope it works this time... ")
# from itertools import permutations
# def consecutive(arr, a, b):
#     base = (a,b)
#     perm = permutations(arr,2)
#     for p in perm:
#         if p == base:
#             return True
#         elif p == base[::-1]:
#             return True
#         else:
#             return False

# consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)
# from itertools import combinations, groupby, combinations_with_replacement
# def solve(arr):
#     x = 1
#     for a in arr:
#         x *= len(set(a))
#     print(x)
# solve([[1,2],[4],[5,6]])
# from itertools import filterfalse
# def longest_palindrome(s):
#     output = filterfalse(lambda x : x == x[::-1], s)
#     for x in output:
#         print(x)
        
# longest_palindrome("zzbaabcd")

# def character_count(city):
#     from collections import Counter
#     city_list = list(city.replace(' ',''))
#     city_list = [city.lower() for city in city_list]
#     c = Counter()
#     for city in city_list:
#         c[city] += 1
#     output = []
#     for key,value in dict(c).items():
#         entry = key + ':' + ('*' * value) + ','
#         output.append(entry)
#     for x in output:
#         if x is output[-1]:
#             x.replace(',','')
#     print(output)
#     # final_output = ''.join(output)
#     # print(final_output)
#     # return final_output
# character_count("Las Vegas")

# def is_it_possible(field):
#     field_as_list = [list(field[:3]), list(field[3:6]), list(field[6:])]
#     trans = [list(row) for row in zip(*field_as_list)]
#     for row in field_as_list:
#         if len(set(row)) < 2:
#             return False
#     for row in trans:
#         if len(set(row)) < 2:
#             return False
#     exes = field.count("X")
#     ohs = field.count("0")
#     if exes + 1 > ohs:
#         return False
#     elif exes - 1 < ohs:
#         return False
#     else:
#         return True

# is_it_possible("0XX"+\
#                "XX0"+\
#                "00X")

# def get_word_distance(word_1, word_2, your_string):
#     string_list = your_string.split()
#     diff = (string_list.index(word_1) + 1) - string_list.index(word_2)
#     return abs(diff)

# get_word_distance("quick", "field", "the quick rabbit ran through the field with a carrot")

# from itertools import accumulate
# import operator
# def find_the_product(input_list, input_x):
#     value = max(accumulate(input_list,func=operator.mul))
#     return value % input_x
    
# find_the_product([5,2,4,1,5], 6)

# def count_adjacent_pairs(st):
#     st = st.lower().split()
#     # dups = len(set([item for item in st if st.count(item) > 1]))
#     # return dups
#     print(st)
#     z = zip([st.index(y) for y in st], [st.count(x) for x in st])
#     for item in z:
#         print(item)

# count_adjacent_pairs("orange Orange apple kiwi pineapple apple apple plum")
# import numpy as np
# def casino_chips(arr):
#     ones = np.ones((len(arr) ** len(arr), len(arr)))
#     print(ones)
# casino_chips([4,1,1])

# def life_path_number(birthdate):
#     separated_bd = birthdate.split("-")
#     final = []
#     for num in separated_bd:
#         total = sum([int(x) for x in list(num)])
#         new = sum([int(n) for n in str(total)])
#         final.append(new)
#     return sum(final)

# def convergence(seed):
#     from functools import reduce
#     series = []
#     while series:
#         if seed < 10:
#             value = seed + seed
#             series.append(value)
#         else:
#             value = reduce((lambda x, y: x * y), [int(d) for d in str(seed)]) 
#             value = seed + value
#             if value == 26:
#                 break
#             else:
#                 series.append(value)
#     print(series)

# convergence(3)

# def stock_list(art, cat):
#     art = [item.split() for item in art]
#     inventory = []
#     for item in art:
#         if item[0][0] in cat:
#             inventory.append(item)
#     print(inventory)
    

# b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B"]
# stock_list(b, c)

# def solve(a,b):
#     from collections import Counter
#     cnt = Counter()
#     for word in a:
#         cnt[word] += 1
#     tally = []
#     for item in b:
#         for k,v in dict(cnt).items():
#             if item == k:
#                 tally.append(v)
#         if item not in dict(cnt).keys():
#             tally.append(0)
#     return tally
# solve(['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap'])

# def sort_items_by_frequency(arr):
#     from collections import Counter
#     from itertools import repeat, chain
#     result = list(chain.from_iterable(repeat(i, c) 
#          for i, c in Counter(arr).most_common())) 
#     print(result)
# sort_items_by_frequency([4,4,2,5,1,1,3,3,2,8])

# def decrypt(code):
#     import string
#     digits = code.split()
#     values = []
#     for item in digits:
#         y = list(filter(lambda x: x.isdigit(), item))
#         num = sum([int(x) for x in y])
#         values.append(num)
#     print(values)
#     output = []
#     for letter in enumerate(list(string.ascii_lowercase)):
#         for item in values:
#             if item == letter[0]:
#                 output.append(letter[1])
#     print(output)

# def shifted_diff(first, second):
#     legit = []
#     for letter in second:
#         if first.index(letter) > second.index(letter):
#             legit.append(letter)
#         else:
#             pass
#     result = len(first) - len(legit)
#     return result
# shifted_diff("eecoff", "coffee")

def anagram_difference(w1, w2):
    common_letter_lngth = len([x for x in w1 if x in w2])
    total_removed = (len(w1) - common_letter_lngth) + (len(w2) - common_letter_lngth)
    return total_removed    
anagram_difference("codewars", "hackerrank")



# import requests
# response = requests.post("http://127.0.0.1:5000/predict", json=[[5.1, 3.5, 1.4, 0.2]])
# print(response.text)

def what_to_invest_in(name):
    import mod
    print("Hi {}, you should invest in {}".format(name, mod.a))

# what_to_invest_in("Todd")

# print(dir())

# def even_numbers(arr, n):
#     evens = [x for x in arr[::-1] if x % 2 == 0]
#     return evens[:n]
# even_numbers([5,5,5,2,4,5,9,32,55,22,3333,9], 3)

# def maskify(cc):
#     if cc == None:
#         return ' '
#     elif len(cc) < 4:
#         for char in cc:
#             if char.isdigit():
#                 return char
#             else:
#                 return ""
#     else:
#         reversed_cc = cc[::-1]
#         new_cc = list(reversed_cc[:4])
#         print(new_cc)
#         for item in enumerate(reversed_cc):
#             if item[0] > 3:
#                 new_cc.append("#")
#             else:
#                 pass
#         return ''.join(new_cc[::-1])

# maskify("32534")

# def pseudo_sort(st):
#     st = sorted(st.split(), key=str.lower)
#     print(st)    

# pseudo_sort("Hello everybody so glad to see You")

# def merge_sort(a, b):
#     return sorted(a + b)

# merge_sort([2,4,6],[3,9,5])

def order_weight(strng):
    new_list = []
    for item in strng.split(' '):
       num = sum([int(x) for x in str(item)])
       new_list.append(num)
    return sorted(new_list)
    

order_weight("56 65 74 100 99 68 86 180 90")