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

def is_it_possible(field):
    field_as_list = [list(field[:3]), list(field[3:6]), list(field[6:])]
    trans = [list(row) for row in zip(*field_as_list)]
    for row in field_as_list:
        if len(set(row)) < 2:
            return False
    for row in trans:
        if len(set(row)) < 2:
            return False
    exes = field.count("X")
    ohs = field.count("0")
    if exes + 1 > ohs:
        return False
    elif exes - 1 < ohs:
        return False
    else:
        return True

is_it_possible("0XX"+\
               "XX0"+\
               "00X")
