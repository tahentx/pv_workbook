from itertools import combinations
def get_best_distances_sum(t, k, ls):
    options = list(combinations(ls, k))
    totals = [sum(x) for x in options]
    less_than_t = list(filter(lambda x: x <= t, totals))
    best_option = max(less_than_t) if less_than_t else None
    return best_option
get_best_distances_sum(8,3,[1, 2, 3, 4])
