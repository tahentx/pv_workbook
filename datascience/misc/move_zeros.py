# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
    zero = [x for x in array if x == 0]
    zero_new = list(filter(lambda x: isinstance(x, int), zero))
    return array.extend(zero_new)

move_zeros([False,1,0,1,2,0,1,3,"a"])