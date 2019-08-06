# kata: https://www.codewars.com/kata/maximum-length-difference/python

def compare(foo):
    box = []
    y = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
    for x in y:
        box.append(len(x))
    print(box)
    print(max(box))

compare("roger")
