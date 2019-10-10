
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

def get_big(n):
    foo = [int(x) for x in str(n)]
    foo.insert(0, foo.pop(foo.index(max(foo))))
    print(foo)

get_big("21538")
