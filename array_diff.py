# codewars kata: https://www.codewars.com/kata/array-dot-diff/train/python
x = [5,6,2]
y = [5,8,10]
def array_diff(a: list, b: list) -> list:
    diff = [a.remove(x) for x in a if x in b]
    print(a)

array_diff(x,y)
