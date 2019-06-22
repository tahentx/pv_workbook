import math

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

def observations_squared(distances_from_mean: list) -> list:
    squared = []
    for x in distances_from_mean:
        sq = x ** 2
        squared.append(sq)
    sum_of_sq = sum(squared)
    return sum_of_sq

z = observations_squared(y)

def get_the_variance(sq_sum,count):
    variance = sq_sum / count
    return variance

v = get_the_variance(z,len(n))
stdev = math.sqrt(v)
print("The standard deviation of the list is: " + str(stdev) + ", while the mean is: " + str(avg))
