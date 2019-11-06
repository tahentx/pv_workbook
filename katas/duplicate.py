
def duplicate(word):
    word2 = list(word)
    word3 = []
    for x in word2:
        if word.count(x) > 1:
            word3.append(")")
        else:
            word3.append("(")
    answer = ''.join(word3)
    return answer
# duplicate("Ball")

# https://www.codewars.com/kata/highest-and-lowest
def high_and_low(numbers):
    x = numbers.replace(" ","")
    y = list(x)
    a = max(y)
    b = min(y)
    answer = str(a) + " " + str(b)
    print(answer)
# high_and_low("2 7 6")

# https://www.codewars.com/kata/two-sum/python
def two_sum(numbers, target):
    foo = []
    for num in numbers:
        value = target - num
        foo.append(value)
    y = [numbers.index(x) for x in foo if x in numbers]
    print(y)
# two_sum([5,2,9,6],7)
#
# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python
def series_sum(n: int) -> float:
    value = []
    i = 1
    while i < n:
        value.append(i/n)
        n = n + 1
    print(value)
# series_sum(9)

def reverse(x: str) -> str:
    x_list = list(x)
    x_list.reverse()
    x_str = ''.join(x_list)
    return x_str
reverse("Bugle")

def validate_pin(input):
    if len(input) == 4 and input.isdigit():
        return True
    else:
        return False
validate_pin("Mort")

# kata: https://www.codewars.com/kata/iq-test/train/python
def iq_test(numbers):
    no_space = numbers.replace(" ","")
    list_form = list(no_space)
    output = [list_form.index(num) for num in list_form if int(num) % 2 == 0]
    for x in output:
        x = x + 1
        return x
# iq_test("4 6 5 2 8 9")

# kata: https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
def disemvowel(string):
    vow = ["a","e","i","o","u"]
    revised = []
    for x in string:
        if x in vow:
            pass
        else:
            revised.append(x)
    output = ''.join(revised)
    print(output)
# disemvowel("Test that function")

# kata: https://www.codewars.com/kata/form-the-largest/train/python
def get_big(n):
    foo = [int(x) for x in str(n)]
    foo.insert(0, foo.pop(foo.index(max(foo))))
    print(foo)
# get_big("21538")

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#       break
#   i = i + 1

# kata: https://www.codewars.com/kata/bumps-in-the-road/train/python
def bump_checker(road):
    if road.count("n") < 16:
        return "Woohoo!"
    else:
        return "Car Dead!"

bump_checker("none")

# kata: https://www.codewars.com/kata/counting-array-elements/train/python
def unique_counter(list):
    solo = set(list)
    y = [list.count(x) for x in solo]
    z = {(key, value) for (key, value) in zip(solo, y)}
    return z
# unique_counter(["Bob","Joe","Bob"])

# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
def dashatize(num):
    num_list = [int(d) for d in str(num)]
    dashed_list = []
    for x in num_list:
        if x % 2 == 0:
            dashed_list.append(x)
        else:
            x = "-"+ str(x) + "-"
            dashed_list.append(x)
    answer = ''.join(str(n) for n in dashed_list)
    return answer
# dashatize(43264)

# https://www.codewars.com/kata/the-highest-profit-wins/train/python
def min_max(lst):
    output_lst = []
    lst.sort()
    output_lst.append(lst[0])
    output_lst.append(lst[-1])
    print(output_lst)
# min_max([34,23,19,88,53])

# https://www.codewars.com/kata/find-the-unique-number-1/train/python
def find_uniq(arr):
    arr_set = set(arr)
    for n in arr_set:
        if arr.count(n) != 1:
            pass
        else:
            return n

# https://www.codewars.com/kata/meeting/python
def meeting(s):
    s_upper = s.upper()
    s_list = s_upper.split(',')
    print(s_list)

# meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill")

def index_function(word):
    caps = []
    foo = [caps.append(word.index(x)) for x in word if x.isupper()]
    return ordered(caps)

# index_function("DiffTesP")

# kata: https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010/train/python
def lost_sheep(friday: list, saturday: list, total: int):
    friday_sheep = sum(friday)
    saturday_sheep = sum(saturday)
    all_seen_sheep = int(friday_sheep) + int(saturday_sheep)
    all_unseen_sheep = total - all_seen_sheep
    return all_unseen_sheep
# lost_sheep([93,3],[22,9],134)

# https://www.codewars.com/kata/rot13-1/train/python
def rot13(message: str):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    alph_dict = {k: v for v, k in enumerate(alphabet)}
    for x in message:
        if x in alph_dict:
            print(alph_dict.get(x))

# rot13("test")

# kata: https://www.codewars.com/kata/thinkful-string-drills-repeater/python

def repeater(string, number):
    return string * int(number)

# kata: https://www.codewars.com/kata/rotate-for-a-max/train/python

def max_rot(num: int):
    store = []
    #
    num_to_str = str(num)
    str_to_list = list(num_to_str)
    str_to_list.insert(len(str_to_list),str_to_list[0])
    str_to_list.pop(0)
    store.append(str_to_list)
    print(store)
    


max_rot(5832)
