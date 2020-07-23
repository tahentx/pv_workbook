import itertools
# Suppose you're given an unsorted array, a. 
# The array is intended to have all integer elements between its minimum and maximum, but could be missing some elements. 
# Write a python function to find the n-th missing element in the array.
# Consider the array in sorted order, then find the n-th missing number. If the n-th missing number does not exist, you can output 'Does not exist'.

def find_missing_element(a, n):
    a = sorted(a)
    b = list(range(min(a),max(a)))
    c = [x for x in b if x not in a]
    z = c[n - 1]
    return z
find_missing_element([2, 3, 11, 9],3)