# Codewars kata: https://www.codewars.com/kata/sum-of-pairs/train/python
def sum_pairs(int: list, s: int) -> list:
    y = []
    z = [y.append(s - x) for x in int]
    for i,j in zip(int,y):
        if i + j == s and i != j:
            print(i,j)
sum_pairs([5,8,2,4],10)
