
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
duplicate("Ball")

# https://www.codewars.com/kata/highest-and-lowest
def high_and_low(numbers):
    x = numbers.replace(" ","")
    y = list(x)
    a = max(y)
    b = min(y)
    answer = str(a) + " " + str(b)
    print(answer)

high_and_low("2 7 6")
