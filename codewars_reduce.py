# Given a non-empty array of integers, return the result of multiplying the values together in order.
ham = [5,5,2,6]
def reduce(ham):
    list = []
    result = 1
    for x in ham:
        result = result * x
        list.append(result)
    print(list[-1])
reduce(ham)
