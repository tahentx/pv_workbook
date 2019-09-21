def nb_dig(n, d):
    a = []
    while n > 0:
        a.append(n ** 2)
        n = n - 1
    print(a)
nb_dig(5,8)
