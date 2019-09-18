# Codewars kata: https://www.codewars.com/kata/sorted-yes-no-how/train/python
def is_sorted_and_how(arr):
    copy = arr.copy()
    arr.sort()
    if copy == arr:
        print("Sorted already")
    else:
        print("Either descending or other")




is_sorted_and_how([63,60,32])
