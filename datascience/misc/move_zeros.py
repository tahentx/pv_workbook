# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
import itertools
def move_zeros(array):
    non_zeros = []
    zeros = []
    for x in array:
        if x == 0:
            zeros.append(x)
        else:
            non_zeros.append(x)
    non_zeros.extend(zeros)
    return non_zeros

# move_zeros([False,1,0,1,2,0,1,3,"a"])

def pig_latin(text):
    new_words = []
    for word in text.split():
        front, base = word[0], word[1:]
        new_word = base + front + 'ay'
        new_words.append(new_word)
    output = ' '.join(new_words)
    print(output)
# pig_latin("hello world!")

def solve(s):
    t = s.split()
    u = ' '.join([x[::-1] for x in t[::-1]])
    return u
solve("Blue Blood")