# Codewars kata: https://www.codewars.com/kata/sorted-yes-no-how/train/python
def is_sorted_and_how(arr):
    copy = arr.copy()
    copy2 = sorted(arr,reverse=True)
    arr.sort()
    if copy == arr:
        print("yes, ascending")
    elif copy2 == arr:
        print("yes, descending")
    else:
        print("no")



is_sorted_and_how([5,2,1])
