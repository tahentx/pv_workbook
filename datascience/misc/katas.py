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

def decipher_this(string):
    target = min([string.index(x) for x in string if not x.isdigit()])
    nums, chars = int(string[:target]),list(string[target:])
    first, body, last = chars[0], ''.join(chars[1:-1]), chars[-1]
    to_join = [chr(nums),last,body,first]
    output = ''.join(to_join)
    print(output)
    
    
decipher_this("72olle")