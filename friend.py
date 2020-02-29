# codewars kata: https://www.codewars.com/kata/friend-or-foe/train/python
def friend(x : list):
    y = [name for name in x if len(name) == 4]
    return y

friend(["Greg","John","Bobby","Lou", "James"])
