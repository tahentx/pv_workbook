# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
# def string_transformer(s):
#     if not s:
#         return ''
#     else:
#         s = s.split()
#         return s
    
# string_transformer("Example string")

def name_value(my_list):
    for item in my_list:
        if ' ' in item:
            item = item.split()
            for subitem in item:
                my_list.append(subitem)
        else:
            print(item)
    # z = sum([my_list.index(x) + 1 for x in my_list])

name_value(['this', 'is', 'a test'])