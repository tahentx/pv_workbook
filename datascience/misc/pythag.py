from itertools import combinations
def pythag(arr):
    high, low = max(arr), min(arr)
    basis = list(range(low,high + 1))
    combo = combinations(basis,3)
    for x in combo:
        legs = x[0]**2 + x[1]**2
        if legs == x[2]**2:
            return True
        else:
            return False
pythag([4,3,9,5])
    