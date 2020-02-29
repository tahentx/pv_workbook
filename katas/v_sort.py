# https://www.codewars.com/kata/find-the-vowels/train/python
#
def vowel_indices(word):
    v = ["a","e","i","o","u"]
    x = [word.index(i) for i in v if i in word]
    y = list(x)
    print(y)
print(vowel_indices("Blue"))
