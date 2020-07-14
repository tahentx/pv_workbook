# Data Science Interview Question #112

# Given an array of n distinct elements, can you find all the triplet combinations that sum to zero?

from itertools import combinations

def sum_triplet_to_zero(input):
    base = combinations(input,3)
    zero_sum = filter(lambda x: sum(x) == 0, base)
    print(zero_sum)
    # for x in base:
    #     if sum(x) == 0:
    #         print(x)

sum_triplet_to_zero([5,-1,-4,9,3])