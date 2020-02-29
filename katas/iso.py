# codewars kata: https://www.codewars.com/kata/isograms/train/python
def is_isogram(string: str) -> bool():
    x = set(string)
    y = []
    for i in string:
        y.append(i)
    if len(x) == len(y):
        print("True")
    else:
        print("False")

is_isogram("bigger")
