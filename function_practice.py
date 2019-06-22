def return_sum(x,y):
    c = x + y
    return c

# res = return_sum(4,5)
# print(res)

n = [94,61,93,154,78,65,32]

def get_mean(sample):
    mean = sum(sample) / len(sample)
    return mean

avg = get_mean(n)

def diff_from_mean(mean: int, observations: list) -> list:
    differences = []
    for x in observations:
        difference = mean - x
        differences.append(difference)
    return differences

y = diff_from_mean(avg, n)
print(y)
