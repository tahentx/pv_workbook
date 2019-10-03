
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
series_sum(9)
