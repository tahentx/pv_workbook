def nb_dig(n, d):
    a = []
    while n > 0:
        a.append(n ** 2)
        n = n - 1
    count = 0
    for i in a:
        if i == d:
            count = count + 1
    print(count)
nb_dig(5,44)
