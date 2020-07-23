from itertools import combinations
def get_best_distances_sum(t, k, ls):
    options = list(combinations(ls, k))
    totals = [sum(x) for x in options]
    less_than_t = list(filter(lambda x: x <= t, totals))
    return max(less_than_t)

get_best_distances_sum(8,3,[1, 2, 3, 4])
